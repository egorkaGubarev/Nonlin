import numpy as np
import matplotlib.pyplot as plt
import scipy.signal as signal


def count_ampl(pos_data):
    return np.average(pos_data[signal.argrelmax(pos_data)]) - np.average(pos_data[signal.argrelmin(pos_data)])


def count_aver(list_1, list_2, list_3, list_4, list_5):
    return (list_1 + list_2 + list_3 + list_4 + list_5) / 5


subdir_i: str = 'improved/'
subdir_n: str = 'narrow/'
subdir_w: str = 'wide/'
subdir_loss: str = 'loss/'

main_path: str = 'C:/users/gubar/VSProjects/burn_stab_flame/eval/'
compare: bool = False

m_t_s: list = [('0.7', '3000', 'o'), ('0.71', '1000', 'o'), ('0.72', '1000', 'o'),
               ('0.73', '1000', 'o'), ('0.74', '1000', 'o'), ('0.75', '1000', 'o'),
               ('0.76', '0', 'o'), ('0.77', '0', 'o'),
               ('0.773', '0', 'o'), ('0.777', '2000', 'o'), ('0.779', '1000', 'l'), ('0.78', '2000', 'l'),
               ('0.7805', '1000', 'l'), ('0.781', '2000', 'l'), ('0.782', '3000', 'o'),
               ('0.783', '1000', 'l'), ('0.784', '1000', 'l'),
               ('0.785', '1000', 'l'), ('0.786', '4000', 'o'), ('0.787', '6000', 'o'),
               ('0.789', '51000', 'o'), ('0.79', '11000', 'i'), ('0.8', '1000', 'o')]
mts_conf: list = [('0.7', '3000', 'o'), ('0.71', '1000', 'o'), ('0.72', '1000', 'o'),
                  ('0.73', '1000', 'o'), ('0.74', '1000', 'o'), ('0.75', '1000', 'o'),
                  ('0.76', '0', 'o'), ('0.77', '0', 'o'), ('0.773', '0', 'o'), ('0.784', '1000', 'l'),
                  ('0.785', '1000', 'l'), ('0.786', '4000', 'o'), ('0.787', '6000', 'o'),
                  ('0.789', '51000', 'o'), ('0.79', '11000', 'i'), ('0.8', '1000', 'o')]
m_t_s_narrow: list = [('0.72', '1000', 'n'), ('0.76', '1000', 'n'),
                      ('0.78', '3000', 'n'), ('0.789', '12000', 'n'), ('0.79', '10000', 'n')]
m_t_s_wide: list = [('0.72', '1000', 'w'), ('0.76', '1000', 'w'),
                    ('0.78', '2000', 'w'), ('0.789', '12000', 'w'), ('0.79', '9000', 'w')]
m_t_s_loss: list = [('0.7', '1000', 'loss'), ('0.75', '2000', 'loss'), ('0.78', '2000', 'loss'),
                    ('0.788', '7000', 'loss'), ('0.79', '3000', 'loss'), ('0.8', '1000', 'loss')]

if compare:
    data: list = [m_t_s, m_t_s_loss]
else:
    data: list = [mts_conf]

fig, ax = plt.subplots()

for m_t_s_list in data:
    m_s: list = []
    center_ampl_list: list = []
    edge_ampl_list: list = []
    ampl_list_3: list = []
    ampl_list_4: list = []
    ampl_list_5: list = []

    for (m, t, file) in m_t_s_list:
        if file == 'i':
            path: str = main_path + subdir_i
        elif file == 'n':
            path: str = main_path + subdir_n
        elif file == 'w':
            path: str = main_path + subdir_w
        elif file == 'loss':
            path: str = main_path + subdir_loss
        else:
            path: str = main_path

        pos = np.loadtxt(path + 'pos-' + t + '-' + m + '.txt')
        points: int = pos.shape[1]

        center_ampl_list.append(count_ampl(pos[:, points // 2]))
        edge_ampl_list.append(count_ampl(pos[:, 0]))
        ampl_list_3.append(count_ampl(pos[:, points // 4]))
        ampl_list_4.append(count_ampl(pos[:, points // 8]))
        ampl_list_5.append(count_ampl(pos[:, 3 * points // 8]))

        m_s.append(m)

    m_float: list = list(map(float, m_s))
    plt.plot(m_float, list(map(count_aver,
                               center_ampl_list, edge_ampl_list, ampl_list_3, ampl_list_4, ampl_list_5)), linewidth=2)

plt.xlabel(r'm, $U_b$', fontsize=24)
plt.ylabel(r'Амплитуда, $L_{th}$', fontsize=24)

if compare:
    plt.legend(['No heat loss', 'Heat loss'])
    plt.legend(['No heat loss', 'Heat loss'])

for axis in ['top', 'bottom', 'left', 'right']:
    ax.spines[axis].set_linewidth(2)

ax.tick_params(axis='both', which='major', labelsize=20)
plt.show()
