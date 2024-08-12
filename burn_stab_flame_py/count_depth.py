import numpy as np
import matplotlib.pyplot as plt


main_path: str = 'C:/users/gubar/VSProjects/burn_stab_flame/'
directory: str = 'eval/'
subdir: str = 'long/'
time_start: str = '2000'
speed: str = '0.782'

path: str = main_path + directory + subdir
suffix: str = time_start + '-' + speed + '.txt'

pos = np.loadtxt(path + 'pos-' + suffix)
par = np.loadtxt(path + 'par-' + suffix)

center_pos = pos[:, pos.shape[1] // 2]
delta = center_pos - pos[:, 0]
print('Depth: ', np.mean(np.abs(delta)))
time = np.linspace(0, par[1], len(center_pos))
plt.plot(time, delta)
plt.xlabel(r't, $\frac{D_{th}}{U_b^2}$', fontsize=16)
plt.ylabel(r'x, $L_{th}$', fontsize=16)
plt.title('Depth', fontsize=16)
plt.grid()
plt.show()
