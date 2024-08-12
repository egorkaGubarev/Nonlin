import numpy as np


main_path: str = 'C:/users/gubar/VSProjects/burn_stab_flame/'
directory: str = 'eval/'
subdir_out: str = 'long/'
times: list = [('1000', 'o'), ('2000', 'o'), ('3000', 'o'), ('4000', 'o'),
               ('5000', 'o'), ('6000', 'o'), ('7000', 'o'), ('8000', 'o')]
speed: str = '0.781'

global_time_sim: float = 0

subdir_l: str = 'long/'
subdir_w: str = 'wide/'
subdir_wl: str = 'wide/long/'
subdir_loss: str = 'loss/'

main_path_in: str = main_path + directory
path_out: str = main_path + directory + subdir_out
suffix_out: str = times[0][0] + '-' + speed + '.txt'

for file_type in ['pos-', 'temp-']:

    with open(path_out + file_type + suffix_out, 'w') as outfile:

        for (time_start, subdir) in times:
            path_in: str = main_path_in

            if subdir == 'l':
                path_in += subdir_l
            elif subdir == 'w':
                path_in += subdir_w
            elif subdir == 'wl':
                path_in += subdir_wl
            elif subdir == 'loss':
                path_in += subdir_loss

            with open(path_in + file_type + time_start + '-' + speed + '.txt') as infile:

                for line in infile:
                    outfile.write(line)

for (time_start, subdir) in times:
    path_in: str = main_path_in

    if subdir == 'l':
        path_in += subdir_l
    elif subdir == 'w':
        path_in += subdir_w
    elif subdir == 'wl':
        path_in += subdir_wl
    elif subdir == 'loss':
        path_in += subdir_loss

    global_time_sim += float(np.loadtxt(path_in + 'par-' + time_start + '-' + speed + '.txt')[1])

subdir = times[0][1]
path_in: str = main_path_in

if subdir == 'l':
    path_in += subdir_l
elif subdir == 'w':
    path_in += subdir_w
elif subdir == 'wl':
    path_in += subdir_wl
elif subdir == 'loss':
    path_in += subdir_loss

par = np.loadtxt(path_in + 'par-' + suffix_out)

with open(path_out + 'par-' + suffix_out, 'w') as outfile:
    outfile.write(str(par[0]) + ' ')
    outfile.write(str(global_time_sim) + ' ')

    for param in range(2, len(par)):
        outfile.write(str(par[param]) + ' ')
