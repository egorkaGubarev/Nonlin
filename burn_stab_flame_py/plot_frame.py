import numpy as np
import matplotlib.pyplot as plt

main_path: str = 'C:/Users/gubar/VSProjects/Nonlin/burn_stab_flame/data/eval/'
subdir: str = 'np0.01w100/'
start_time: str = '1000'
speed: str = '0.8'
NP: str = '0.01'
upstream: float = 0
downstream: float = 10
frames = [999]

# legend = [r'$t = 0 \tau_{th}$', r'$t = 6 \tau_{th}$', r'$t = 11 \tau_{th}$']

path = main_path + subdir
suffix = start_time + '-' + speed + '.txt'

pos = np.loadtxt(path + 'pos-' + suffix)
par = np.loadtxt(path + 'par-' + suffix)

old_par_form: int = 8
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
plt.title('Front position, m = ' + speed + r', $\kappa$ = ' + NP, fontsize=24)
# plt.legend(legend, prop={'size': 24})

for axis in ['top', 'bottom', 'left', 'right']:
    ax.spines[axis].set_linewidth(2)

ax.tick_params(axis='both', which='major', labelsize=20)
plt.show()
