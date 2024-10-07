#ifndef FUNCTIONS_H
#define FUNCTIONS_H

#include <algorithm>
#include <cmath>
#include <fstream>
#include <iostream>
#include <vector>

#include "ut.h"

template <typename type>
type ad_vel(const type temp, const type N) {
    const type vel = std::exp(N / 2 * (1 - 1.0 / temp));
    return vel;
}

template <typename type>
type temp_flame_stab(const type N, const type m) {
    const type res = N / (N - 2 * std::log(m));
    return res;
}

template <typename type>
type x_flame_stab(const type m, const type sigma, const type N) {
    const type temp_stab = temp_flame_stab(N, m);
    const type res = std::log((1 - sigma) / (1 - temp_stab)) / m;
    return res;
}

template <typename type>
type khi(const type m, const type pos) {
    const type arg = m * pos / 2;
    const type res = cth(arg) - arg / std::pow(sh(arg), 2);
    return res;
}

template <typename type>
type phi(const type pos, const type temp, const type m, const type sigma, const type N) {
    const type vel = ad_vel(temp, N);
    const type res = (1 - sigma) * m * vel - std::pow(m, 2) / 2 * (1 + cth(m * pos / 2)) * (temp - sigma);
    return res;
}

template <typename type>
type psi_1(const type pos, const type temp, const type m, const type lew, const type N) {
    const type vel = ad_vel(temp, N);
    const type res = (m - vel) / (1 - std::exp(-m * lew * pos));
    return res;
}

template <typename type>
type psi_2(const type pos, const type temp, const type m, const type lew, const type N, const type sigma) {
    const type phi_val = phi(pos, temp, m, sigma, N);
    const type khi_val = khi(m, pos);
    const type psi_1_val = psi_1(pos, temp, m, lew, N);
    const type res = (phi_val + m * (1 - sigma) * psi_1_val * khi_val) / (1 + khi_val);
    return res;
}

template <typename type>
void evaluate_zero_der(const std::vector<type>& pos_last, const std::vector<type>& temp_last,
    std::vector<type>& pos, std::vector<type>& temp,
    const type m, const type N, const type sigma, const type sigma_w, const type lew, const type np,
    const type time_step, const type dim_step, const bool loss) {

    const size_t points = std::size(temp_last);

    const size_t left_ev_bord = 1;
    const size_t right_ev_bord = points - 1;

    for (size_t point = left_ev_bord; point < right_ev_bord; ++point) {
        const type temp_cent = temp_last[point];
        const type temp_left = temp_last[point - 1];
        const type temp_right = temp_last[point + 1];

        const type pos_cent = pos_last[point];
        const type pos_left = pos_last[point - 1];
        const type pos_right = pos_last[point + 1];

        const type khi_val = khi(m, pos_cent);
        const type a = m / (2 * (1 - std::exp(-m * lew * pos_cent))) - m;
        const type b = m * (1 - sigma) * (1 - lew) * khi_val / (lew * (khi_val + 1));

        const type c = (1 - sigma) * m * (a * khi_val - m) / (khi_val + 1) +
            std::pow((1 - sigma) * m, 2) * khi_val / ((khi_val + 1) * (temp_cent - sigma));

        const type d = -(1 - sigma) * m * khi_val / ((khi_val + 1) * (temp_cent - sigma));

        const type der_2_temp = type((temp_right - 2 * temp_cent + temp_left) / std::pow(dim_step, 2));
        const type der_1_temp = type((temp_right - temp_left) / (2 * dim_step));
        const type der_2_pos = type((pos_right - 2 * pos_cent + pos_left) / std::pow(dim_step, 2));
        const type der_1_pos = type((pos_right - pos_left) / (2 * dim_step));

        const type temp_new = type(temp_cent + time_step * (der_2_temp + b * der_2_pos + c * std::pow(der_1_pos, 2) +
            d * der_1_pos * der_1_temp + psi_2(pos_cent, temp_cent, m, lew, N, sigma)));

        const type pos_new = type(pos_cent + time_step * (der_2_pos / lew + a * std::pow(der_1_pos, 2) +
            psi_1(pos_cent, temp_cent, m, lew, N)));

        temp[point] = temp_new;
        pos[point] = pos_new;
    }

    if (loss){
        temp[0] = (4 * temp[1] - temp[2] + 2 * dim_step * np * sigma_w) / (2 * dim_step * np + 3);
        temp[points - 1] = (4 * temp[points - 2] - temp[points - 3] + 2 * dim_step * np * sigma_w) / (2 * dim_step * np + 3);
    }
    else {
        temp[0] = (4 * temp[1] - temp[2]) / 3;
        temp[points - 1] = (4 * temp[points - 2] - temp[points - 3]) / 3;
    }

    pos[0] = (4 * pos[1] - pos[2]) / 3;
    pos[points - 1] = (4 * pos[points - 2] - pos[points - 3]) / 3;
}

template <typename type>
void do_calcul_at_m(const std::string& main_path, const std::string& subdir,
    const std::string& start_time, const std::string& final_time, const std::string& speed,
    const size_t frames, const type time_simul, const bool loss, const bool use_conf,
    const type width, const type courant, const type dim_step,
    const type m, const type sigma, const type N, const type sigma_w, const type lew, const type np) {
    const size_t verb = 10;
    const size_t points_per_width = 1;

    const size_t points_to_dump = size_t(width * points_per_width);

    const std::string path_in = main_path + "no_log/" + subdir;
    const std::string path_out = main_path + "eval/" + subdir;

    const std::string start_suffix = start_time + '-' + speed + ".txt";
    const std::string final_suffix = final_time + '-' + speed + ".txt";

    const std::string temp_out_name = path_out + "temp-" + start_suffix;
    const std::string pos_out_name = path_out + "pos-" + start_suffix;
    const std::string par_out_name = path_out + "par-" + start_suffix;

    std::string temp_in_name = path_in + "temp-" + start_suffix;
    std::string pos_in_name = path_in + "pos-" + start_suffix;
    std::string par_in_name = path_in + "par-" + start_suffix;

    if (start_time == "0") {

        if (use_conf) {
            temp_in_name = path_in + "temp-conf.txt";
            pos_in_name = path_in + "pos-conf.txt";
            par_in_name = path_in + "par-conf.txt";
        }
        else {
            temp_in_name = path_in + "temp.txt";
            pos_in_name = path_in + "pos.txt";
            par_in_name = path_in + "par.txt";
        }

    }

    const std::string final_temp_name = path_in + "temp-" + final_suffix;
    const std::string final_pos_name = path_in + "pos-" + final_suffix;
    const std::string final_par_name = path_in + "par-" + final_suffix;

    const type time_step = courant * std::pow(dim_step, 2);
    const size_t iters = size_t(time_simul / time_step);
    const size_t iter_log = iters / frames;
    const size_t points = size_t(width / dim_step);
    const size_t iter_progr = iters / 100 * verb;
    const type x_stab = x_flame_stab(m, sigma, N);
    const type temp_stab = temp_flame_stab(N, m);
    std::ofstream out_pos, out_par, out_temp;

    std::vector<type> pos(points, 0);
    std::vector<type> temp(points, 0);

    std::array<std::vector<type>, 2> data = read_profile<type>(temp_in_name, pos_in_name, par_in_name);

    std::vector<type>& pos_last = data[0];
    std::vector<type>& temp_last = data[1];

    out_par.open(par_out_name);
    out_pos.open(pos_out_name);
    out_temp.open(temp_out_name);

    type curr_time = 0;
    size_t curr_iter = 0;

    while (curr_time < time_simul) {
        ++curr_iter;
        curr_time += time_step;

        if (curr_iter % iter_log == 0) {
            dump_n<type>(out_pos, pos_last, points_to_dump);
            dump_n<type>(out_temp, temp_last, points_to_dump);
        }

        evaluate_zero_der(pos_last, temp_last, pos, temp, m, N, sigma, sigma_w, lew, np, time_step, dim_step, loss);

        copy(std::begin(pos), std::end(pos), std::begin(pos_last));
        copy(std::begin(temp), std::end(temp), std::begin(temp_last));

        if (curr_iter % iter_progr == 0) {
            const type progr = std::round(curr_iter * 100.0 / iters);
            std::cout << "m = " << m << ": " << progr << '%' << '\n';
        }
    }

    out_par << width << ' ' << time_simul << ' ' << x_stab << ' ' << temp_stab;

    out_pos.close();
    out_temp.close();
    out_par.close();

    out_par.open(final_par_name);
    out_pos.open(final_pos_name);
    out_temp.open(final_temp_name);

    out_par << width << ' ' << points;

    dump<type>(out_pos, pos_last);
    dump<type>(out_temp, temp_last);

    out_par.close();
    out_pos.close();
    out_temp.close();
}


#endif