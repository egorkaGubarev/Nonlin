import numpy as np
import matplotlib.pyplot as plt

subdir_i: str = 'improved/'
subdir_n: str = 'narrow/'
subdir_w: str = 'wide/'
subdir_loss: str = 'loss/'
subdir_long: str = 'long/'

main_path: str = 'C:/users/gubar/VSProjects/burn_stab_flame/eval/'
compare: bool = False

m_t_s: list = [('0.75', '1000', 'ln'), ('0.76', '0', 'o'), ('0.77', '0', 'o'),
               ('0.773', '0', 'ln'), ('0.777', '0', 'ln'),
               ('0.779', '1000', 'ln'), ('0.78', '2000', 'ln'), ('0.781', '1000', 'ln'), ('0.784', '0', 'ln'),
               ('0.785', '4000', 'ln'), ('0.786', '3000', 'ln'), ('0.787', '6000', 'o'),
               ('0.789', '51000', 'o'), ('0.79', '11000', 'i'), ('0.8', '1000', 'o')]
m_t_s_narrow: list = [('0.72', '1000', 'n'), ('0.76', '1000', 'n'),
                      ('0.78', '3000', 'n'), ('0.789', '12000', 'n'), ('0.79', '10000', 'n')]
m_t_s_wide: list = [('0.72', '1000', 'w'), ('0.76', '1000', 'w'),
                    ('0.78', '2000', 'w'), ('0.789', '12000', 'w'), ('0.79', '9000', 'w')]
m_t_s_loss: list = [('0.7', '1000', 'loss'), ('0.75', '2000', 'loss'), ('0.78', '2000', 'loss'),
                    ('0.788', '7000', 'loss'), ('0.79', '3000', 'loss'), ('0.8', '1000', 'loss')]

if compare:
    data: list = [m_t_s, m_t_s_narrow, m_t_s_wide]
else:
    data: list = [m_t_s]

fig, ax = plt.subplots()

for m_t_s_list in data:
    m_s: list = []
    error_list: list = []

    freq_list: list = []
    freq_list_edge: list = []

    for (m, t, file) in m_t_s_list:
        if file == 'i':
            path: str = main_path + subdir_i
        elif file == 'n':
            path: str = main_path + subdir_n
        elif file == 'w':
            path: str = main_path + subdir_w
        elif file == 'loss':
            path: str = main_path + subdir_loss
        elif file == 'ln':
            path: str = main_path + subdir_long
        else:
            path: str = main_path

        pos = np.loadtxt(path + 'pos-' + t + '-' + m + '.txt')
        time_sim: float = float(np.loadtxt(path + 'par-' + t + '-' + m + '.txt')[1])
        points: int = pos.shape[1]

        center_pos = pos[:, points // 2]
        edge_pos = pos[:, 0]

        frames: int = len(center_pos)
        frequencies = np.fft.fftfreq(frames)[1: frames // 2]

        # find positive frequency with max coefficient
        freq_list.append(frequencies[np.argmax(abs(np.fft.fft(center_pos)[1: frames // 2]))] * frames / time_sim)
        freq_list_edge.append(frequencies[np.argmax(abs(np.fft.fft(edge_pos)[1: frames // 2]))] * frames / time_sim)

        error_list.append(1 / (2 * time_sim))

        m_s.append(m)

    m_float: list = list(map(float, m_s))

    ax.errorbar(m_float, freq_list, yerr=error_list, marker='x')
    ax.errorbar(m_float, freq_list_edge, yerr=error_list, marker='x')

ax.set_xlabel(r'm, $U_b$', fontsize=24)
ax.set_ylabel(r'Частота, $\frac{1}{T_{th}}$', fontsize=24)

for axis in ['top', 'bottom', 'left', 'right']:
    ax.spines[axis].set_linewidth(2)

ax.tick_params(axis='both', which='major', labelsize=20)
ax.legend(['Центр', 'Граница'], prop={'size': 24})
plt.tight_layout(rect=(-0.15, -0.09, 1, 1))
plt.show()
