import numpy as np
import matplotlib.pyplot as plt


bif_point: float = 0.79

subdir_i: str = 'improved/'
subdir_n: str = 'narrow/'
subdir_w: str = 'wide/'
subdir_loss: str = 'loss/'

main_path: str = 'C:/users/gubar/VSProjects/burn_stab_flame/eval/'

m_t_s: list = [('0.7', '0', 'o'), ('0.74', '0', 'o'), ('0.76', '0', 'o'), ('0.788', '0', 'o'),
               ('0.789', '0', 'o'), ('0.79', '0', 'o'),
               ('0.8', '0', 'o'), ('0.85', '1000', 'o'), ('0.9', '1000', 'o'), ('0.95', '1000', 'o')]
m_t_s_loss: list = [('0.7', '0', 'loss'), ('0.75', '0', 'loss'), ('0.784', '0', 'loss'),
                    ('0.786', '0', 'loss'), ('0.787', '0', 'loss'),
                    ('0.788', '0', 'loss'), ('0.79', '0', 'loss'),
                    ('0.8', '0', 'loss'), ('0.85', '0', 'loss'), ('0.9', '0', 'loss'), ('0.95', '0', 'loss')]

data: list = [m_t_s, m_t_s_loss]
fig, ax = plt.subplots()

for m_t_s_list in data:
    m_s: list = []
    dist_list = []
    color = ''
    label = ''

    for (m, t, file) in m_t_s_list:
        if file == 'i':
            path: str = main_path + subdir_i
        elif file == 'n':
            path: str = main_path + subdir_n
        elif file == 'w':
            path: str = main_path + subdir_w
        elif file == 'loss':
            path: str = main_path + subdir_loss
            color = 'orange'
            label = r'$\frac{Nu}{Pe} = \frac{1}{100}$'
        else:
            path: str = main_path
            color = '#1f77b4'
            label = r'$\frac{Nu}{Pe} = 0$'

        pos = np.loadtxt(path + 'pos-' + t + '-' + m + '.txt')
        points: int = pos.shape[1]
        center_pos = pos[:, points // 2]
        dist: float = np.mean(center_pos)

        dist_list.append(dist)
        m_s.append(m)

    dist_list = np.array(dist_list)
    m_float = np.array(list(map(float, m_s)))

    unstable_idx = np.where(m_float < bif_point)
    stable_idx = np.where(m_float >= bif_point)

    plt.plot(m_float[unstable_idx], dist_list[unstable_idx], marker='x', linestyle='dashed', color=color)
    plt.plot(m_float[stable_idx], dist_list[stable_idx], marker='x', color=color, label=label)

ax.set_xlabel(r'm, $U_b$', fontsize=24)
ax.set_ylabel(r'Среднее положение фронта пламени, $L_{th}$', fontsize=24)

for axis in ['top', 'bottom', 'left', 'right']:
    ax.spines[axis].set_linewidth(2)

ax.tick_params(axis='both', which='major', labelsize=20)
ax.legend(prop={'size': 24})
plt.show()
