#include <array>

#include "../headers/par.h"
#include "../headers/ut.h"

int main()
{
	const std::string source_time = "1000";
    const std::string target_time = "2000";
	const std::string speed = "0.75";
	const std::string source_dir = "eval/";
	const std::string target_dir = "eval_no_log/";

    const std::string pos_log = main_path + target_dir + "pos-" + target_time + '-' + speed + ".txt";
    const std::string par = main_path + target_dir + "par-" + target_time + '-' + speed + ".txt";
    const std::string temp_log = main_path + target_dir + "temp-" + target_time + '-' + speed + ".txt";

    const std::string temp_in_name = main_path + source_dir + "temp-" + source_time + '-' + speed + ".txt";
    const std::string pos_in_name = main_path + source_dir + "pos-" + source_time + '-' + speed + ".txt";
    const std::string par_in_name = main_path + source_dir + "par-" + source_time + '-' + speed + ".txt";

    std::ofstream out_pos, out_par, out_temp;
    std::ifstream counter, par_in;
    counter.open(pos_in_name);
    const size_t lines = std::count(std::istreambuf_iterator<char>(counter), std::istreambuf_iterator<char>(), '\n');
    counter.close();
    std::array<std::vector<my_type>, 2> data = read_profile_from_line<my_type>(temp_in_name, pos_in_name, par_in_name, lines - 1);

    std::vector<my_type>& pos_last = data[0];
    std::vector<my_type>& temp_last = data[1];

    my_type skip_type = 0;
    size_t skip_size_t = 0;
    size_t points = 0;
    par_in.open(par_in_name);
    par_in >> skip_type >> skip_type >> skip_size_t >> skip_type >> skip_type >> points;
    par_in.close();

    out_par.open(par);
    out_pos.open(pos_log);
    out_temp.open(temp_log);

    out_par << width << ' ' <<  points;

    
    dump<my_type>(out_pos, pos_last);
    dump<my_type>(out_temp, temp_last);

    out_pos.close();
    out_temp.close();
    out_par.close();

    return 0;
}
