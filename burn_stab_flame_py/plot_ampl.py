import numpy as np
import matplotlib.pyplot as plt


def update_path(file_type: str):
    if file_type == 'i':
        return main_path + subdir_i, 'i'
    elif file_type == 'n':
        return main_path + subdir_n, 'n'
    elif file_type == 'w':
        return main_path + subdir_w, 'w'
    elif file_type == 'loss':
        return main_path + subdir_loss, r'$\frac{Nu}{Pe} = \frac{1}{100}$'
    else:
        return main_path, '-'


subdir_i: str = 'improved/'
subdir_n: str = 'narrow/'
subdir_w: str = 'wide/'
subdir_loss: str = 'np0.01w100/'

main_path: str = 'D:/VSProjects/burn_stab_flame/data/eval/'

plot_center: bool = True
plot_edge: bool = False

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
np_0_01_w_100: list = [('0.78', '9000', 'loss'), ('0.784', '1000', 'loss'),
                       ('0.788', '7000', 'loss'), ('0.79', '3000', 'loss'), ('0.8', '1000', 'loss')]

data: list = [np_0_01_w_100]
fig, ax = plt.subplots()

for m_t_s_list in data:
    label: str = ''
    m_s: list = []
    center_ampl_list: list = []
    edge_ampl_list: list = []

    for (m, t, file) in m_t_s_list:
        path, label = update_path(file)
        result = np.loadtxt(path + 'result-' + t + '-' + m + '.txt')

        if plot_center:
            center_ampl_list.append(result[0])
        if plot_edge:
            edge_ampl_list.append(result[1])

        m_s.append(m)

    m_float: list = list(map(float, m_s))

    if plot_center:
        plt.plot(m_float, center_ampl_list, marker='x', linewidth=2, label=label)
    if plot_edge:
        plt.plot(m_float, edge_ampl_list, marker='x', linewidth=2, label=label)

plt.title('Amplitude, w = 100', fontsize=24)
plt.xlabel(r'm, $U_b$', fontsize=24)
plt.ylabel(r'Амплитуда, $L_{th}$', fontsize=24)
plt.legend(prop={'size': 24})

for axis in ['top', 'bottom', 'left', 'right']:
    ax.spines[axis].set_linewidth(2)

ax.tick_params(axis='both', which='major', labelsize=20)
plt.show()
