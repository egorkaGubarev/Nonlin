import numpy as np
import matplotlib.pyplot as plt


def update_path(file_type):
    if file_type == 'i':
        return main_path + subdir_np_0_w_100 + subdir_i, 'i'
    elif file_type == 'n':
        return main_path + subdir_n, 'n'
    elif file_type == 'w':
        return main_path + subdir_w, 'w'
    elif file_type == 'l':
        return main_path + subdir_np_0_w_100 + subdir_l, r'$\frac{Nu}{Pe} = 0$'
    elif file_type == 'o':
        return main_path + subdir_np_0_w_100, r'$\frac{Nu}{Pe} = 0$'
    elif file_type == 'loss':
        return main_path + subdir_np_0_01_w_100, r'$\frac{Nu}{Pe} = \frac{1}{100}$'
    else:
        return main_path, '-'


subdir_i = 'improved/'
subdir_n = 'narrow/'
subdir_w = 'wide/'
subdir_l = 'long/'
subdir_np_0_w_100 = 'np0w100/'
subdir_np_0_01_w_100 = 'np0.01w100/'

main_path = 'C:/Users/gubar/VSProjects/Nonlin/burn_stab_flame/data/eval/'

plot_center = True
plot_edge = True
NP = '0'
w = '100'

np_0_w_100 = [('0.77', '1000', 'o'),
              ('0.773', '2000', 'o'), ('0.777', '2000', 'o'), ('0.779', '1000', 'l'), ('0.78', '2000', 'l'),
              ('0.7805', '1000', 'l'), ('0.781', '2000', 'l'), ('0.782', '3000', 'o'),
              ('0.783', '1000', 'l'), ('0.784', '1000', 'l'),
              ('0.785', '1000', 'l'), ('0.786', '4000', 'o'), ('0.787', '6000', 'o'),
              ('0.789', '51000', 'o'), ('0.79', '11000', 'i'), ('0.8', '1000', 'o')]
mts_conf = [('0.7', '3000', 'o'), ('0.71', '1000', 'o'), ('0.72', '1000', 'o'),
            ('0.73', '1000', 'o'), ('0.74', '1000', 'o'), ('0.75', '1000', 'o'),
            ('0.76', '0', 'o'), ('0.77', '0', 'o'), ('0.773', '0', 'o'), ('0.784', '1000', 'l'),
            ('0.785', '1000', 'l'), ('0.786', '4000', 'o'), ('0.787', '6000', 'o'),
            ('0.789', '51000', 'o'), ('0.79', '11000', 'i'), ('0.8', '1000', 'o')]
m_t_s_narrow = [('0.72', '1000', 'n'), ('0.76', '1000', 'n'),
                ('0.78', '3000', 'n'), ('0.789', '12000', 'n'), ('0.79', '10000', 'n')]
m_t_s_wide = [('0.72', '1000', 'w'), ('0.76', '1000', 'w'),
              ('0.78', '2000', 'w'), ('0.789', '12000', 'w'), ('0.79', '9000', 'w')]
np_0_01_w_100 = [('0.782', '2000', 'loss'),
                 ('0.783', '3000', 'loss'), ('0.784', '2000', 'loss'), ('0.785', '5000', 'loss'),
                 ('0.786', '3000', 'loss'), ('0.7865', '3000', 'loss'),
                 ('0.787', '4000', 'loss'), ('0.7875', '4000', 'loss'),
                 ('0.788', '7000', 'loss'), ('0.79', '3000', 'loss'), ('0.8', '1000', 'loss')]

data = [np_0_w_100]
fig, ax = plt.subplots()

for m_t_s_list in data:
    label = ''
    m_s = []
    center_ampl_list = []
    edge_ampl_list = []

    for (m, t, file) in m_t_s_list:
        path, label = update_path(file)
        result = np.loadtxt(path + 'result-' + t + '-' + m + '.txt')

        if plot_center:
            center_ampl_list.append(result[0])
        if plot_edge:
            edge_ampl_list.append(result[1])

        m_s.append(m)

    m_float = list(map(float, m_s))

    if plot_center:
        plt.plot(m_float, center_ampl_list, marker='x', linewidth=2, label='Center')
    if plot_edge:
        plt.plot(m_float, edge_ampl_list, marker='x', linewidth=2, label='Edge')

plt.title(r'Amplitude, $\kappa = $' + NP + r', $w = $' + w + r'$L_{th}$', fontsize=24)
plt.xlabel(r'm, $U_b$', fontsize=24)

if plot_center and plot_edge:
    plt.ylabel(r'Amplitude, $L_{th}$', fontsize=24)
else:
    if plot_center:
        plt.ylabel(r'Center amplitude, $L_{th}$', fontsize=24)
    if plot_edge:
        plt.ylabel(r'Edge amplitude, $L_{th}$', fontsize=24)

plt.legend(prop={'size': 24})

for axis in ['top', 'bottom', 'left', 'right']:
    ax.spines[axis].set_linewidth(2)

ax.tick_params(axis='both', which='major', labelsize=20)
plt.show()
