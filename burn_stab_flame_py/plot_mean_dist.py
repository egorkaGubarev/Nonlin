import numpy as np
import matplotlib.pyplot as plt


def update_path(file_type):
    if file_type == 'i':
        return main_path + subdir_i
    if file_type == 'n':
        return main_path + subdir_n
    if file_type == 'w':
        return main_path + subdir_w
    if file_type == 'loss':
        return main_path + subdir_loss, 'orange', r'$\frac{Nu}{Pe} = \frac{1}{100}$'
    return main_path, '#1f77b4', r'$\frac{Nu}{Pe} = 0$'


bif_point: float = 0.79

subdir_i: str = 'improved/'
subdir_n: str = 'narrow/'
subdir_w: str = 'wide/'
subdir_loss: str = 'np0.01w100/'

main_path: str = 'C:/users/gubar/VSProjects/Nonlin/burn_stab_flame/data/eval/'

np_0_w_100: list = [('0.7', '0', 'o'), ('0.74', '0', 'o'), ('0.76', '0', 'o'), ('0.788', '0', 'o'),
                    ('0.789', '0', 'o'), ('0.79', '0', 'o'),
                    ('0.8', '0', 'o'), ('0.85', '1000', 'o'), ('0.9', '1000', 'o'), ('0.95', '1000', 'o')]
np_0_01_w_100: list = [('0.782', '2000', 'loss'),
                       ('0.783', '3000', 'loss'), ('0.784', '2000', 'loss'), ('0.785', '5000', 'loss'),
                       ('0.786', '3000', 'loss'), ('0.7865', '3000', 'loss'),
                       ('0.787', '4000', 'loss'), ('0.7875', '4000', 'loss'),
                       ('0.788', '7000', 'loss'), ('0.79', '3000', 'loss'), ('0.8', '1000', 'loss')]

data: list = [np_0_01_w_100]
fig, ax = plt.subplots()

for m_t_s_list in data:
    m_s: list = []
    dist_list = []
    color = ''
    label = ''

    for (m, t, file) in m_t_s_list:
        path, color, label = update_path(file)
        dist_list.append(np.loadtxt(path + 'result-' + t + '-' + m + '.txt')[2])
        m_s.append(m)

    dist_list = np.array(dist_list)
    m_float = np.array(list(map(float, m_s)))
    stable_idx = np.where(m_float >= bif_point)

    plt.plot(m_float, dist_list, marker='x', linestyle='dashed', color=color)
    plt.plot(m_float[stable_idx], dist_list[stable_idx], marker='x', color=color, label=label)

plt.title('Distance, w = 100', fontsize=24)
ax.set_xlabel(r'm, $U_b$', fontsize=24)
ax.set_ylabel(r'Distance, $L_{th}$', fontsize=24)

for axis in ['top', 'bottom', 'left', 'right']:
    ax.spines[axis].set_linewidth(2)

ax.tick_params(axis='both', which='major', labelsize=20)
ax.legend(prop={'size': 24})
plt.show()
