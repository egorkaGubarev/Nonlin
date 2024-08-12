import numpy as np
import matplotlib.pyplot as plt

upstream: float = 0
downstream: float = 10
frames = [977, 983, 988]
legend = [r'$t = 0 \tau_{th}$', r'$t = 6 \tau_{th}$', r'$t = 11 \tau_{th}$']

pos_path: str = '../../VSProjects/burn_stab_flame/eval/pos-8000-0.78.txt'
par_path: str = '../../VSProjects/burn_stab_flame/eval/par-8000-0.78.txt'

old_par_form: int = 8

pos = np.loadtxt(pos_path)
par = np.loadtxt(par_path)

y_bott: float = 0
width: float = float(par[0])
dim_step: float = width / pos.shape[1]
y_up: float = y_bott + width
y = np.arange(y_bott, y_up, dim_step)
fig, ax = plt.subplots()

for frame in frames:
    init_prof = pos[frame, :]
    plt.plot(init_prof, y, linewidth=2)

plt.xlim(upstream, downstream)
plt.xlabel(r'x, $L_{th}$', fontsize=24)
plt.ylabel(r'y, $L_{th}$', fontsize=24)
plt.legend(legend, prop={'size': 24})

for axis in ['top', 'bottom', 'left', 'right']:
    ax.spines[axis].set_linewidth(2)

ax.tick_params(axis='both', which='major', labelsize=20)
plt.show()
