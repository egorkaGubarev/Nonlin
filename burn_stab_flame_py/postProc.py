import numpy as np
import matplotlib.pyplot as plt


def count_frequency(pos_array):
    frames: int = len(pos_array)
    frequencies = np.fft.fftfreq(frames)[1: frames // 2]
    freq = frequencies[np.argmax(abs(np.fft.fft(pos_array)[1: frames // 2]))] * frames / time_simul
    return freq


main_path: str = 'C:/Users/gubar/VSProjects/Nonlin/burn_stab_flame/data/eval/'
subdir: str = 'np0w100/'
start_type = ''
start_time: str = '10000'
speed: str = '0.784'
NP: str = '0'
fig, ax = plt.subplots()
path = main_path + subdir
suffix = start_time + '-' + speed + '.txt'

pos = np.loadtxt(path + 'pos-' + suffix)
par = np.loadtxt(path + 'par-' + suffix)

time_simul: int = pos.shape[0]

center = pos[:, pos.shape[1] // 2]
edge = pos[:, 0]

center_amplit = np.max(center) - np.min(center)
edge_amplit = np.max(edge) - np.min(edge)
distance = np.mean(center)
center_frequency = count_frequency(center)
edge_frequency = count_frequency(edge)
frequency_error = 1 / (2 * time_simul)
depth = np.mean(np.abs(center - edge))

with open(path + 'result-' + suffix, 'w') as result:
    result.write(str(center_amplit) + ' ' + str(edge_amplit) + ' ' + str(distance) + ' '
                 + str(center_frequency) + ' ' + str(edge_frequency) + ' ' + str(frequency_error))

print('Center amplitude:', round(center_amplit, 2))
print('Edge amplitude:', round(edge_amplit, 2))
print('Distance:', round(distance, 2))
print('Center frequency:', round(float(center_frequency), 4))
print('Edge frequency:', round(float(edge_frequency), 4))
print('Frequency error:', round(frequency_error, 4))
print('Depth:', round(depth, 2))

time_axis = np.linspace(int(start_time), int(start_time) + time_simul, time_simul)

plt.plot(time_axis, center, linewidth=2, label='center')
plt.plot(time_axis, edge, linewidth=2, label='edge')

plt.title('Front position, m = ' + speed + r', $\kappa$ = ' + NP + ', w = ' + str(int(par[0])), fontsize=24)
plt.xlabel(r't, $\tau_{th}$', fontsize=24)
plt.ylabel(r'F, $L_{th}$', fontsize=24)
plt.legend(prop={'size': 24})

for axis in ['top', 'bottom', 'left', 'right']:
    ax.spines[axis].set_linewidth(2)

ax.tick_params(axis='both', which='major', labelsize=20)
plt.show()
