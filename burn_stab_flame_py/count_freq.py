import numpy as np
import matplotlib.pyplot as plt


def count_ampl(pos_data):
    return np.max(pos_data) - np.min(pos_data)


main_path: str = 'C:/users/gubar/VSProjects/burn_stab_flame/'
directory: str = 'eval/'
subdir: str = 'long/'
time_start: str = '2000'
speed: str = '0.78'
verb: bool = False
old_par_form: int = 8

path: str = main_path + directory + subdir
suffix: str = time_start + '-' + speed + '.txt'

pos = np.loadtxt(path + 'pos-' + suffix)
par = np.loadtxt(path + 'par-' + suffix)

points: int = pos.shape[1]
center_point: int = points // 2
time_sim: float = float(par[1])

if len(par) == old_par_form:
    x_stab: float = float(par[6])
    temp_stab: float = float(par[7])
else:
    x_stab: float = float(par[2])
    temp_stab: float = float(par[3])

center_pos = pos[:, center_point]
frames: int = len(center_pos)
frequencies = np.fft.fftfreq(frames)[1: frames // 2]
# find positive frequency with max coefficient
freq = frequencies[np.argmax(abs(np.fft.fft(center_pos)[1: frames // 2]))] * frames / time_sim

print('Center amplitude:', count_ampl(center_pos))
print('Frequency:', freq)

time = np.linspace(0, time_sim, frames)
fig, ax = plt.subplots()
plt.plot(time, center_pos)
plt.xlabel(r't, $\frac{D_{th}}{U_b^2}$', fontsize=24)
plt.ylabel(r'x, $L_{th}$', fontsize=24)

for axis in ['top', 'bottom', 'left', 'right']:
    ax.spines[axis].set_linewidth(2)

if verb:
    plt.plot(time, pos[:, 0] / x_stab)
    plt.plot(time, pos[:, points - 1] / x_stab)
    plt.plot(time, np.loadtxt(path + 'temp-' + suffix)[:, center_point] / temp_stab)
    plt.legend(['center pos', 'down edge pos', 'up edge pos', 'center temp'])

plt.tight_layout(rect=(-0.07, -0.08, 1, 1))
ax.tick_params(axis='both', which='major', labelsize=20)
plt.show()
