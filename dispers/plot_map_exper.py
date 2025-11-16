import matplotlib.pyplot as plt
import numpy as np
import scipy


def exclude_large_phi(data):
    result = []
    for point in data:
        phi = point[1]
        if phi <= phi_max:
            result.append((point[0], phi))
    return result


save_path = ('C:/Users/gubar/OneDrive/Документы/МФТИ/Нелинейная динамика/Отчётность/Статья/Эволюционные уравнения/'
             'Картинки/eps/no_long.eps')

zero = ((0.8049, 1.25), (0.8062, 1.3), (0.8076, 1.35), (0.809, 1.4), (0.8104, 1.45))
first = ((0.8047, 1.25), (0.806, 1.3), (0.8071, 1.35), (0.8083, 1.4), (0.8094, 1.45))
second = ((0.8042, 1.25), (0.8051, 1.3), (0.8057, 1.35), (0.8059, 1.38), (0.806, 1.4), (0.8061, 1.43), (0.8061, 1.45))
third = ((0.8029, 1.25), (0.8034, 1.28), (0.8036, 1.3), (0.8037, 1.33), (0.8035, 1.35), (0.802, 1.4), (0.8005, 1.45))

zero_cylinder = ((0.8049, 1.25), (0.8062, 1.3), (0.8075, 1.35), (0.8087, 1.4), (0.8108, 1.45), (0.8118, 1.5))
first_cylinder = ((0.8046, 1.25), (0.8058, 1.3), (0.8068, 1.35), (0.8076, 1.4), (0.8092, 1.45), (0.8097, 1.5))
second_cylinder = ((0.804, 1.25), (0.8049, 1.3), (0.8052, 1.35), (0.8048, 1.4), (0.8054, 1.45), (0.8047, 1.5))

stable_points = ((0.81, 1.25), (0.807, 1.3), (0.808, 1.35), (0.81, 1.4), (0.811, 1.45))
oscillations = ((0.8045, 1.25), (0.8056, 1.3), (0.8074, 1.35), (0.807, 1.4), (0.809, 1.4), (0.81, 1.45))
long_beat = ((0.8035, 1.25), (0.804, 1.25), (0.8048, 1.25), (0.804, 1.3), (0.805, 1.3), (0.806, 1.3), (0.8061, 1.3),
             (0.8045, 1.35), (0.805, 1.35), (0.806, 1.35), (0.804, 1.4), (0.805, 1.4), (0.806, 1.4), (0.808, 1.4),
             (0.804, 1.45), (0.805, 1.45), (0.806, 1.45), (0.807, 1.45), (0.808, 1.45), (0.809, 1.45))
beat = ((0.802, 1.25), (0.803, 1.25), (0.802, 1.35), (0.803, 1.3), (0.8035, 1.3),
        (0.803, 1.35), (0.8035, 1.35), (0.804, 1.35),
        (0.802, 1.4), (0.803, 1.4), (0.8035, 1.4), (0.8, 1.45),
        (0.801, 1.45), (0.802, 1.45), (0.8035, 1.45), (0.803, 1.45))
fault = ()

stable_points_cylinder = ((0.805, 1.25), (0.81, 1.25), (0.807, 1.3), (0.808, 1.35), (0.809, 1.4))
flat_cylinder = ((0.8049, 1.25), (0.8062, 1.3), (0.8074, 1.35))
curve_cylinder = ((0.8048, 1.25), (0.806, 1.3), (0.8061, 1.3), (0.807, 1.35), (0.8073, 1.35), (0.808, 1.4))
beat_cylinder = ((0.802, 1.25), (0.803, 1.25), (0.8035, 1.25), (0.804, 1.25), (0.8045, 1.25),
                 (0.804, 1.3), (0.805, 1.3),
                 (0.805, 1.35), (0.806, 1.35), (0.804, 1.4), (0.805, 1.4), (0.806, 1.4), (0.807, 1.4))

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

phi_max = 1.4
phi_min = 1.25
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

if geom == 'cylinder':
    stable_points = stable_points_cylinder
    oscillations = flat_cylinder
    long_beat = curve_cylinder
    beat = beat_cylinder

    zero = zero_cylinder
    first = first_cylinder
    second = second_cylinder

zero = exclude_large_phi(zero)
first = exclude_large_phi(first)
second = exclude_large_phi(second)
third = exclude_large_phi(third)

stable_points = exclude_large_phi(stable_points)
oscillations = exclude_large_phi(oscillations)
long_beat = exclude_large_phi(long_beat)
beat = exclude_large_phi(beat)

_, ax = plt.subplots()

if need_lines:
    zero_interp = scipy.interpolate.CubicSpline([phi for (m, phi) in zero], [m for (m, phi) in zero])
    first_interp = scipy.interpolate.CubicSpline([phi for (m, phi) in first], [m for (m, phi) in first])
    second_interp = scipy.interpolate.CubicSpline([phi for (m, phi) in second], [m for (m, phi) in second])
    third_interp = scipy.interpolate.CubicSpline([phi for (m, phi) in third], [m for (m, phi) in third])
    phi_axis = np.linspace(phi_min, phi_max, interp_points)

    plt.plot(zero_interp(phi_axis), phi_axis,
             label='0 mode', color='black', linewidth=line_width)
    plt.plot(first_interp(phi_axis), phi_axis,
             label='1 mode', color='black', linewidth=line_width, linestyle='--')
    plt.plot(second_interp(phi_axis), phi_axis, label='2 mode',
             color='black', linewidth=line_width, linestyle='-.')
    if geom == 'slit':
        plt.plot(third_interp(phi_axis), phi_axis,
                 label='3 mode', color='black', linewidth=line_width, linestyle=':')

if plot_points:
    if need_stable:
        plt.scatter([phi for (phi, m) in stable_points], [m for (phi, m) in stable_points],
                    s=marker_area, label='stable', color='blue')
    plt.scatter([phi for (phi, m) in oscillations], [m for (phi, m) in oscillations],
                s=marker_area, label=osc_label, color='green')
    if plot_long_beat_separately:
        plt.scatter([phi for (phi, m) in long_beat], [m for (phi, m) in long_beat],
                    s=marker_area, label=long_label, color='orange')
    else:
        plt.scatter([phi for (phi, m) in long_beat], [m for (phi, m) in long_beat],
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
plt.ylabel(r'$\phi$', fontsize=font_size)

for axis in ['top', 'bottom', 'left', 'right']:
    ax.spines[axis].set_linewidth(figure_borders_width)

if need_title:
    plt.title('Calculated oscillation types', fontsize=font_size)

if need_save:
    plt.savefig(save_path)

plt.grid()
plt.show()
