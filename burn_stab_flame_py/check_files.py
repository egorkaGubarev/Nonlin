import numpy as np
from os import listdir
from os.path import isfile, join


main_path: str = 'C:/users/gubar/VSProjects/burn_stab_flame/'
file_type: str = 'eval/'
subdir: str = 'loss/'
speed: str = '0.78'
sep: str = '-'

len_speed: int = len(speed)
path: str = main_path + file_type + subdir
files: list = [file for file in listdir(path) if isfile(join(path, file)) and file[0:3] == 'par']

times: list = []
time_sims: list = []

for file in files:
    seps: list = [pos for pos, char in enumerate(file) if char == sep]

    if len(seps) > 0:
        last_sep: int = seps[1]
        speed_index: int = last_sep + 1
        point_index = speed_index + len_speed

        if file[speed_index: point_index] == speed and file[point_index] == '.':
            times.append(file[seps[0] + 1: last_sep])

            if file_type == 'eval/':
                time_sims.append(float(np.loadtxt(path + file)[1]))

if len(times) > 0:
    times: list = list(map(float, times))
    times, time_sims = zip(*sorted(zip(times, time_sims)))
    print('Time:')
    print(times)

    if file_type == 'eval/':
        print('Simulation time:')
        print(time_sims)
else:
    print('No files')
