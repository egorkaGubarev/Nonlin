import matplotlib.pyplot as plt
import numpy as np

all_data = {'m = 0.8': {'data': ((0, -0.007, 0.2394), (0.011, -0.0071, 0.2395),
                                 (0.022, -0.0074, 0.2398), (0.033, -0.008, 0.2404),
                                 (0.044, -0.0087, 0.2412), (0.056, -0.0096, 0.2422), (0.067, -0.0107, 0.2434),
                                 (0.078, -0.0121, 0.2448), (0.089, -0.0136, 0.2465), (0.1, -0.0154, 0.2483)),
                        'legend': 'm = 0.800'},
            'm = 0.79': {'data': ((0, -0.0007, 0.2413), (0.011, -0.0008, 0.2414),
                                  (0.022, -0.0011, 0.2418), (0.033, -0.0016, 0.2423),
                                  (0.044, -0.0023, 0.243), (0.056, -0.0033, 0.244), (0.067, -0.0044, 0.2452),
                                  (0.078, -0.0057, 0.2466), (0.089, -0.0073, 0.2482), (0.1, -0.009, 0.25)),
                         'legend': 'm = 0.79'},
            'm = 0.789': {'data': ((0, -0.000085, 0.2415), (0.011, -0.00019, 0.2416),
                                   (0.022, -0.0005, 0.2419), (0.033, -0.001, 0.2425),
                                   (0.044, -0.0017, 0.2432), (0.056, -0.0027, 0.2442), (0.067, -0.0038, 0.2454),
                                   (0.078, -0.0051, 0.2467), (0.089, -0.0067, 0.2483), (0.1, -0.0084, 0.2501)),
                          'legend': 'm = 0.789'},
            'm = 0.788': {'data': ((0, 0.00053, 0.2416), (0.011, 0.00042, 0.2417),
                                   (0.022, 0.00016, 0.2421), (0.033, -0.0004, 0.2426),
                                   (0.044, -0.0011, 0.2434), (0.056, -0.002, 0.2443), (0.067, -0.0032, 0.2455),
                                   (0.078, -0.0045, 0.2469), (0.089, -0.0061, 0.2485), (0.1, -0.0078, 0.2502)),
                          'legend': 'm = 0.788'},
            'm = 0.787': {'data': ((0, 0.0011, 0.2418), (0.011, 0.001, 0.2419),
                                   (0.022, 0.00073, 0.2422), (0.033, 0.00021, 0.2428),
                                   (0.044, -0.00051, 0.2435), (0.056, -0.0014, 0.2445), (0.067, -0.0026, 0.2456),
                                   (0.078, -0.0039, 0.247), (0.089, -0.0054, 0.2486), (0.1, -0.0072, 0.2504)),
                          'legend': 'm = 0.787'},
            'm = 0.786': {'data': ((0, 0.0017, 0.2419), (0.011, 0.0016, 0.2421),
                                   (0.022, 0.0013, 0.2424), (0.033, 0.00082, 0.2429),
                                   (0.044, 0.000097, 0.2437), (0.056, -0.00083, 0.2446), (0.067, -0.002, 0.2458),
                                   (0.078, -0.0033, 0.2472), (0.089, -0.0048, 0.2487), (0.1, -0.0066, 0.2505)),
                          'legend': 'm = 0.786'},
            'm = 0.785': {'data': ((0, 0.0023, 0.2421), (0.011, 0.0022, 0.2422),
                                   (0.022, 0.0019, 0.2425), (0.033, 0.0014, 0.2431),
                                   (0.044, 0.0007, 0.2438), (0.056, -0.00023, 0.2448), (0.067, -0.0014, 0.2459),
                                   (0.078, -0.0027, 0.2473), (0.089, -0.0042, 0.2489), (0.1, -0.006, 0.2506)),
                          'legend': 'm = 0.785'},
            'm = 0.784': {'data': ((0, 0.0029, 0.2422), (0.011, 0.0028, 0.2423),
                                   (0.022, 0.0025, 0.2427), (0.033, 0.002, 0.2432),
                                   (0.044, 0.0013, 0.2439), (0.056, 0.00037, 0.2449), (0.067, -0.00076, 0.2461),
                                   (0.078, -0.0021, 0.2474), (0.089, -0.0036, 0.249), (0.1, -0.0054, 0.2507)),
                          'legend': 'm = 0.784'},
            'm = 0.782': {'data': ((0, 0.0041, 0.2425), (0.011, 0.004, 0.2426),
                                   (0.022, 0.0037, 0.2429), (0.033, 0.0032, 0.2435),
                                   (0.044, 0.0025, 0.2442), (0.056, 0.0016, 0.2451), (0.067, 0.00043, 0.2463),
                                   (0.078, -0.0009, 0.2477), (0.089, -0.0024, 0.2492), (0.1, -0.0042, 0.251)),
                          'legend': 'm = 0.782'},
            'm = 0.78': {'data': ((0, 0.0053, 0.2427), (0.011, 0.0052, 0.2429),
                                  (0.022, 0.0049, 0.2432), (0.033, 0.0044, 0.2437),
                                  (0.044, 0.0037, 0.2444), (0.056, 0.0027, 0.2454), (0.067, 0.0016, 0.2465),
                                  (0.078, 0.00027, 0.2479), (0.089, -0.0013, 0.2494), (0.1, -0.003, 0.2512)),
                         'legend': 'm = 0.78'},
            'm = 0.779': {'data': ((0, 0.0059, 0.2429), (0.011, 0.0058, 0.243),
                                  (0.022, 0.0055, 0.2433), (0.033, 0.005, 0.2438),
                                  (0.044, 0.0043, 0.2445), (0.056, 0.0033, 0.2455), (0.067, 0.0022, 0.2466),
                                  (0.078, 0.00086, 0.248), (0.089, -0.00068, 0.2495), (0.1, -0.0024, 0.2513)),
                          'legend': 'm = 0.779'},
            'm = 0.77': {'data': ((0, 0.0055, 0.2405), (0.011, 0.0054, 0.2405),
                                  (0.022, 0.005, 0.2405), (0.033, 0.0044, 0.2405),
                                  (0.044, 0.0036, 0.2405), (0.056, 0.0025, 0.2405), (0.067, 0.0011, 0.2405),
                                  (0.078, -0.00051, 0.2405), (0.089, -0.0024, 0.2405), (0.1, -0.0045, 0.2405)),
                         'legend': 'm = 0.77, N = 14, Le = 1'},
            'm = 0.77, N = 10': {'data': ((0, 0.011, 0.2437), (0.022, 0.0106, 0.2441),
                                          (0.044, 0.0094, 0.2454), (0.067, 0.0073, 0.2474),
                                          (0.089, 0.0044, 0.2502), (0.11, 0.00074, 0.2538), (0.13, -0.0038, 0.2582),
                                          (0.16, -0.0091, 0.2632), (0.18, -0.015, 0.2688), (0.2, -0.022, 0.2751)),
                                 'legend': 'm = 0.77, N = 10, Le = 1.5'},
            'm = 0.72': {'data': ((0, 0.0143, 0.2475), (0.022, 0.0138, 0.2475),
                                  (0.044, 0.012, 0.2475), (0.067, 0.0098, 0.2475),
                                  (0.089, 0.0064, 0.2475), (0.11, 0.0019, 0.2475), (0.13, -0.0035, 0.2475),
                                  (0.16, -0.0099, 0.2475), (0.18, -0.017, 0.2475), (0.2, -0.026, 0.2475)),
                         'legend': 'm = 0.72, N = 11.4, Le = 1'},
            'm = 0.72, N = 10': {'data': ((0, 0.00499, 0.253), (0.011, 0.00487, 0.253), (0.022, 0.0045, 0.253),
                                          (0.033, 0.00388, 0.253), (0.044, 0.00302, 0.253),
                                          (0.056, 0.00191, 0.253), (0.067, 0.00055, 0.253), (0.078, -0.00105, 0.253),
                                          (0.089, -0.00291, 0.253), (0.1, -0.00501, 0.253)),
                                 'legend': 'm = 0.72, N = 10, Le = 1'}
            }

modes_to_plot = (('m = 0.79', 'blue'), ('m = 0.785', 'green'), ('m = 0.77, N = 10', 'red'))
width = 258
kn = (3.83, 7.02)
plot_imaginary = False
plot_real = True
need_title = False
need_legend = True
need_second_axis = False
need_save = False
k_lim = np.array([0, 0.1])
w_lim = np.array([0.23, 0.26])
w_lim_real = np.array([-0.01, 0.01])

font_size = 48
line_width = 4
figure_borders_width = 4
axis_tick_size = 40
tick_width_factor = 8
legend_size = 28

fig_width = 15
fig_height = 7

k_style = 'dotted'
zero_style = '-.'

pad = 15

if plot_imaginary:
    _, ax = plt.subplots(figsize=(fig_width, fig_height))
    ax.tick_params(axis='x', pad=pad)
else:
    _, ax = plt.subplots(figsize=(fig_width, fig_height))
    ax.tick_params(axis='x', pad=pad)


for (mode, color) in modes_to_plot:
    data_to_plot = all_data[mode]

    data = data_to_plot['data']
    legend = data_to_plot['legend']

    points = len(data)

    k = np.zeros(points)
    real_w = np.zeros(points)
    imaginary_w = np.zeros(points)

    for i in range(points):
        (k[i], real_w[i], imaginary_w[i]) = data[i]

    if plot_real:
        ax.plot(k, real_w, label=legend, linewidth=line_width, color=color)

        if need_second_axis:
            ax_2 = ax.twinx()
            ax_2.plot(k, real_w / (2 * np.pi), label=(r'Re($\omega$), ' + legend),
                      linewidth=line_width, color=color)

    if plot_imaginary:
        ax.plot(k, imaginary_w, label=legend, linewidth=line_width, color=color)

        if need_second_axis:
            ax_2.plot(k, imaginary_w / (2 * np.pi), label=(r'Im($\omega$), ' + legend), linewidth=line_width)

ax.plot(k_lim, (0, 0), linewidth=line_width, color='black', linestyle=zero_style)

for n in kn:
    if plot_imaginary:
        ax.plot([n / width] * 2, w_lim, linewidth=line_width, color='black', linestyle=k_style)
    if plot_real:
        ax.plot([n / width] * 2, w_lim_real, linewidth=line_width, color='black', linestyle=k_style)

for axis in ['top', 'bottom', 'left', 'right']:
    if plot_imaginary:
        ax.spines[axis].set_linewidth(figure_borders_width)
    if plot_real:
        ax.spines[axis].set_linewidth(figure_borders_width)

if need_title:
    ax.set_title('Dispersion', fontsize=font_size)

if need_legend:
    ax.legend(prop={'size': legend_size}, frameon=False, ncols=len(modes_to_plot))

if plot_imaginary:
    ax.set_xlabel('k', fontsize=font_size)
ax.set_xlabel('k', fontsize=font_size)

if plot_imaginary:
    ax.set_ylabel(r'$\omega$', fontsize=font_size)
if plot_real:
    ax.set_ylabel(r'$\sigma$', fontsize=font_size)

if plot_imaginary:
    ax.set_xlim(k_lim)
    ax.set_ylim(w_lim)

if plot_real:
    ax.set_xlim(k_lim)
    ax.set_ylim(w_lim_real)

if plot_imaginary:
    ax.tick_params(axis='both', which='major', labelsize=axis_tick_size)
if plot_real:
    ax.tick_params(axis='both', which='major',
                   labelsize=axis_tick_size, length=axis_tick_size,
                   width=axis_tick_size / tick_width_factor, direction='inout')
plt.tight_layout(rect=(-0.01, -0.04, 1.01, 1.02))

if need_second_axis:
    ax_2.set_ylabel(r'$\nu$', fontsize=font_size)
    ax_2.set_ylim(w_lim / (2 * np.pi))
    ax_2.tick_params(axis='both', which='major', labelsize=axis_tick_size)

if need_save:
    plt.savefig('C:/Users/gubar/OneDrive/Документы/МФТИ/Нелинейная динамика/Отчётность/Статья/Эволюционные уравнения'
                '/Картинки/eps/omega_N=10_Le=1.5_w=100.eps')
plt.show()
