import matplotlib.pyplot as plt
import numpy as np
import scipy


save_path = ('C:/Users/gubar/OneDrive/Документы/МФТИ/Нелинейная динамика/Отчётность/Статья/Эволюционные уравнения/'
             'Картинки/eps/no_long.eps')

zero = ((0.788, 80), (0.788, 100))
first = ((0.785, 80), (0.786, 100))
second = ((0.778, 80), (0.782, 100))

stable_points = ((0.789, 100),)
flat = ((0.788, 100),)
curve = ((0.778, 80), (0.779, 80), (0.78, 80), (0.784, 80), (0.785, 80),
         (0.784, 100), (0.785, 100), (0.786, 100), (0.787, 100))
beat = ((0.777, 80),
        (0.776, 100), (0.777, 100), (0.778, 100), (0.779, 100), (0.78, 100), (0.781, 100), (0.782, 100), (0.783, 100))
fault = ()

plot_fault = False
plot_points = True
plot_long_beat_separately = True
need_title = False
need_stable = True
need_save = False
need_lines = True
geom = 'cylinder'

osc_label = 'flat'
long_label = 'curve'

m_min = 0.74
m_max = 0.75

y_max = 100
y_min = 80
interp_points = 100

marker_area = 80
figure_borders_width = 3
font_size = 36
axis_tick_size = 30
line_width = 3
legend_size = 29

left = -0.06
bottom = -0.01
right = 1.02
top = 1.03

_, ax = plt.subplots()

if need_lines:
    zero_interp = scipy.interpolate.CubicSpline([phi for (m, phi) in zero], [m for (m, phi) in zero])
    first_interp = scipy.interpolate.CubicSpline([phi for (m, phi) in first], [m for (m, phi) in first])
    second_interp = scipy.interpolate.CubicSpline([phi for (m, phi) in second], [m for (m, phi) in second])
    phi_axis = np.linspace(y_min, y_max, interp_points)

    plt.plot(zero_interp(phi_axis), phi_axis,
             label='0 mode', color='black', linewidth=line_width)
    plt.plot(first_interp(phi_axis), phi_axis,
             label='1 mode', color='black', linewidth=line_width, linestyle='--')
    plt.plot(second_interp(phi_axis), phi_axis, label='2 mode',
             color='black', linewidth=line_width, linestyle='-.')

if plot_points:
    if need_stable:
        plt.scatter([phi for (phi, m) in stable_points], [m for (phi, m) in stable_points],
                    s=marker_area, label='stable', color='blue')
    plt.scatter([phi for (phi, m) in flat], [m for (phi, m) in flat],
                s=marker_area, label=osc_label, color='green')
    if plot_long_beat_separately:
        plt.scatter([phi for (phi, m) in curve], [m for (phi, m) in curve],
                    s=marker_area, label=long_label, color='orange')
    else:
        plt.scatter([phi for (phi, m) in curve], [m for (phi, m) in curve],
                    s=marker_area, color='green')
    plt.scatter([phi for (phi, m) in beat], [m for (phi, m) in beat],
                s=marker_area, label='beat', color='red')
    if plot_fault:
        plt.scatter([phi for (phi, m) in fault], [m for (phi, m) in fault],
                    s=marker_area, label='fault', color='black')

plt.legend(prop={'size': legend_size}, frameon=False)
ax.tick_params(axis='both', which='major', labelsize=axis_tick_size)
plt.tight_layout(rect=(left, bottom, right, top))

plt.xlabel('m', fontsize=font_size)
plt.ylabel('R', fontsize=font_size)

for axis in ['top', 'bottom', 'left', 'right']:
    ax.spines[axis].set_linewidth(figure_borders_width)

if need_title:
    plt.title('Calculated oscillation types', fontsize=font_size)

if need_save:
    plt.savefig(save_path)

plt.grid()
plt.show()
