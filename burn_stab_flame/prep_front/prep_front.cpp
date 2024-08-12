#include <fstream>
#include <vector>

#include "../headers/funct.h"
#include "../headers/par.h"
#include "../headers/ut.h"

typedef double my_type;

int main()
{
    const my_type pos_start_marg = -0.01;
    const my_type temp_start_marg = -0.01;
    const my_type freq = 0.5;
    const my_type ampl = 0.01;
    const std::string subdir = "";
    const std::string target_dir = "eval_no_log/";

    const std::string path = main_path + target_dir + subdir;

    const std::string pos_log = path + "pos.txt";
    const std::string temp_log = path + "temp.txt";
    const std::string par = path + "par.txt";

    const size_t points = size_t(width / dim_step);
    std::ofstream out_pos, out_par, out_temp;

    const my_type temp_stab = temp_flame_stab(N, m);
    const my_type pos_stab = x_flame_stab(m, sigma, N);

    const my_type pos_start = pos_stab + pos_start_marg;
    const my_type temp_start = temp_stab + temp_start_marg;

    std::vector<my_type> pos_last(points, 0);
    std::vector<my_type> temp_last(points, temp_start);

    fill_sin(pos_last, pos_start, ampl, freq, dim_step);

    out_par.open(par);
    out_pos.open(pos_log);
    out_temp.open(temp_log);

    out_par  << width << ' ' << points;

    dump<my_type>(out_pos, pos_last);
    dump<my_type>(out_temp, temp_last);

    out_pos.close();
    out_temp.close();
    out_par.close();

    return 0;
}