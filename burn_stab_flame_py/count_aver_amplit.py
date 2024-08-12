import numpy as np
import matplotlib.pyplot as plt
import scipy.signal as signal


def count_ampl(pos_data):
    return np.average(pos_data[signal.argrelmax(pos_data)]) - np.average(pos_data[signal.argrelmin(pos_data)])


main_path: str = 'C:/users/gubar/VSProjects/burn_stab_flame/'
directory: str = 'eval/'
subdir: str = ''
time_start: str = '8000'
speed: str = '0.78'
old_par_form: int = 8

path: str = main_path + directory + subdir
suffix: str = time_start + '-' + speed + '.txt'

pos = np.loadtxt(path + 'pos-' + suffix)
par = np.loadtxt(path + 'par-' + suffix)

center_pos = pos[:, pos.shape[1] // 2]
edge_pos = pos[:, 0]

points: int = len(center_pos)
time_sim = par[1]

center_ampl = count_ampl(center_pos)
edge_ampl = count_ampl(edge_pos)
aver_ampl = (center_ampl + edge_ampl) / 2

print('Center amplitude:', round(center_ampl, 2))
print('Edge amplitude:', round(edge_ampl, 2))
print('Average amplitude:', round(aver_ampl, 2))

fig, ax = plt.subplots()

plt.plot(np.linspace(0, time_sim, points), center_pos)
# plt.plot(np.linspace(0, time_sim, points), edge_pos)

plt.xlabel(r't, $\tau_{th}$', fontsize=24)
plt.ylabel(r'F, $L_{th}$', fontsize=24)

for axis in ['top', 'bottom', 'left', 'right']:
    ax.spines[axis].set_linewidth(2)

ax.tick_params(axis='both', which='major', labelsize=20)
plt.tight_layout(rect=(-0.06, -0.09, 1, 1))

# plt.legend(['center', 'edge'])
# plt.grid()
plt.show()
