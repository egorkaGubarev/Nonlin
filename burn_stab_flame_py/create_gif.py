import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation


hold_pos: float = 0
y_bott: float = 0
x_upstream_limit: float = 2
downstream: float = 5
fps: int = 24

main_path: str = 'C:/users/gubar/VSProjects/Nonlin/burn_stab_flame/data/'
directory: str = 'eval/'
subdir: str = 'np0w100/'
start_type = ''
time_start: str = '8000'
speed: str = '0.784'
NP = '0'

path: str = main_path + directory + subdir + start_type
suffix: str = time_start + '-' + speed + '.txt'
par = np.loadtxt(path + 'par-' + suffix)

width: float = float(par[0])

pos = np.loadtxt(path + 'pos-' + suffix)

y_up: float = y_bott + width
y = np.linspace(y_bott, y_up, pos.shape[1])
y[-1] = width
fig, ax = plt.subplots()
front_plot, = plt.plot([], [])


def init():
    ax.set_xlim(x_upstream_limit, downstream)
    ax.set_ylim(y_bott, y_up)

    plt.xlabel(r'x, $L_{th}$', fontsize=24)
    plt.ylabel(r'y, $L_{th}$', fontsize=24)

    for axis in ['top', 'bottom', 'left', 'right']:
        ax.spines[axis].set_linewidth(2)

    ax.tick_params(axis='both', which='major', labelsize=20)
    plt.tight_layout(rect=(-0.02, -0.02, 1, 0.94))
    return [front_plot]


def update_plot(frame):
    front_plot.set_data(pos[frame, :], y)

    plt.title('Front, t = ' + str(int(time_start) + frame) + r' $\tau_{th}$,'
                                                             r' m = ' + speed + r', $\kappa = $' + NP)
    return [front_plot]


animation = FuncAnimation(fig, update_plot, frames=pos.shape[0], init_func=init)
animation.save('front_m=' + speed + '_np=' + NP + '_w=' + str(width) + '_t=' + time_start + '.gif',
               writer='pillow', fps=fps)
