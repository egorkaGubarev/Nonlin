#include <algorithm>
#include <array>
#include <cmath>
#include <fstream>
#include <iostream>
#include <vector>

#include "../headers/funct.h"
#include "../headers/par.h"
#include "../headers/ut.h"

typedef double my_type;

int main()
{
    const size_t frames = 100;
    const size_t verb = 10;
    const my_type time_simul = 100;
    const std::string source_dir = "eval_no_log/";
    const std::string subdir_in = "";
    const std::string subdir_out = "";
    const std::string speed = "0.75";

    const std::string start_time = "0";
    const std::string final_time = "100";

    const std::string path_in = main_path + source_dir + subdir_in;

    const std::string start_suffix = start_time + '-' + speed + ".txt";
    const std::string start_suffix_bin = start_time + '-' + speed + ".bin";
    const std::string final_suffix = final_time + '-' + speed + ".txt";

    const std::string temp_out_name = subdir_out + "temp-" + start_suffix;
    const std::string pos_out_name = subdir_out + "pos-" + start_suffix;
    const std::string par_out_name = subdir_out + "par-" + start_suffix_bin;

    std::string temp_in_name = path_in + "temp-" + start_suffix;
    std::string pos_in_name = path_in + "pos-" + start_suffix;
    std::string par_in_name = path_in + "par-" + start_suffix;

    if (start_time == "0") {
        temp_in_name = path_in + "temp.txt";
        pos_in_name = path_in + "pos.txt";
        par_in_name = path_in + "par.txt";
    }

    const std::string final_temp_name = path_in + "temp-" + final_suffix;
    const std::string final_pos_name = path_in + "pos-" + final_suffix;
    const std::string final_par_name = path_in + "par-" + final_suffix;

    const my_type time_step = courant * std::pow(dim_step, 2);
    const size_t iters = size_t(time_simul / time_step);
    const size_t iter_log = iters / frames;
    const size_t points = size_t(width / dim_step);
    const size_t iter_progr = iters / 100 * verb;
    const my_type x_stab = x_flame_stab(m, sigma, N);
    const my_type temp_stab = temp_flame_stab(N, m);
    std::ofstream out_pos, out_par, out_temp;

    std::vector<my_type> pos(points, 0);
    std::vector<my_type> temp(points, 0);

    std::array<std::vector<my_type>, 2> data = read_profile<my_type>(temp_in_name, pos_in_name, par_in_name);

    std::vector<my_type>& pos_last = data[0];
    std::vector<my_type>& temp_last = data[1];

    out_par.open(par_out_name, std::ios::binary);
    out_pos.open(pos_out_name);
    out_temp.open(temp_out_name);

    const std::string par_string = std::to_string(width) + ' ' + std::to_string(time_simul) +
        ' ' + std::to_string(x_stab) + ' ' + std::to_string(temp_stab);
    out_par.write((char*)&par_string, sizeof(par_string));

    my_type curr_time = 0;
    size_t curr_iter = 0;

    while (curr_time < time_simul) {
        ++curr_iter;
        curr_time += time_step;

        if (curr_iter % iter_log == 0) {
            dump<my_type>(out_pos, pos_last);
            dump<my_type>(out_temp, temp_last);
        }

        evaluate_zero_der(pos_last, temp_last, pos, temp, m, N, sigma, lew, time_step, dim_step);

        copy(std::begin(pos), std::end(pos), std::begin(pos_last));
        copy(std::begin(temp), std::end(temp), std::begin(temp_last));

        if (curr_iter % iter_progr == 0) {
            const my_type progr = std::round(curr_iter * 100.0 / iters);
            std::cout << progr << " %" << '\n';
        }
    }

    out_pos.close();
    out_temp.close();
    out_par.close();

    out_par.open(final_par_name);
    out_pos.open(final_pos_name);
    out_temp.open(final_temp_name);

    out_par << width << ' ' << points;

    dump<my_type>(out_pos, pos_last);
    dump<my_type>(out_temp, temp_last);

    out_par.close();
    out_pos.close();
    out_temp.close();

    return 0;
}
