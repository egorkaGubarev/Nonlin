import numpy as np
import matplotlib.pyplot as plt


main_path: str = 'D:/VSProjects/burn_stab_flame/data/eval/'
subdir: str = 'np0.01w100/'
start_time: str = '1000'
speed: str = '0.784'
NP: str = r'$\frac{1}{100}$'
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

with open(path + 'result-' + suffix, 'w') as result:
    result.write(str(center_amplit) + ' ' + str(edge_amplit))

print('Center amplitude: ', round(center_amplit, 2))
print('Edge amplitude: ', round(edge_amplit, 2))

time_axis = np.linspace(int(start_time), int(start_time) + time_simul, time_simul)

plt.plot(time_axis, center, linewidth=2, label='center')
plt.plot(time_axis, edge, linewidth=2, label='edge')

plt.title('Front position, m = ' + speed + r', $\frac{Nu}{Pe}$ = ' + NP + ', w = ' + str(int(par[0])), fontsize=24)
plt.xlabel(r'm, $U_b$', fontsize=24)
plt.ylabel(r'F, $L_{th}$', fontsize=24)
plt.legend(prop={'size': 24})

for axis in ['top', 'bottom', 'left', 'right']:
    ax.spines[axis].set_linewidth(2)

ax.tick_params(axis='both', which='major', labelsize=20)
plt.show()
