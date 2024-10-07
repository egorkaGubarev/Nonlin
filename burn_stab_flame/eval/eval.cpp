#include <array>
#include <omp.h>
#include <string>

#include "../headers/funct.h"
#include "../headers/par.h"

typedef double my_type;

int main()
{
    const size_t frames = 1000;
    const my_type time_simul = 1000;
    const size_t calc = 1;
    const bool loss = false;
    const bool use_conf = false;
    const std::string subdir = "np0w100/";
    const std::string start_type = "";

    const std::string start_time = "10000";
    const std::string final_time = "11000";

    const std::array<const my_type, calc> ms = { 0.784 };
    const std::array<const std::string, calc> speeds = { "0.784" };

    const std::string result_dir = subdir + start_type;

    #pragma omp parallel for
    for (int i = 0; i < calc; ++i) {
        const my_type m = ms[i];
        const std::string& speed = speeds[i];

        do_calcul_at_m(main_path, result_dir, start_time, final_time, speed, frames, time_simul, loss, use_conf, width, courant, dim_step, m, sigma, N, sigma_w, lew, np);
    }

    return 0;
}
