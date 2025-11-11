import matplotlib.pyplot as plt

zero = ()

stable_points = ((0.81, 1.25),)
flat = ()
fault = ()

plot_fault = True

m_min = 0.74
m_max = 0.75

marker_area = 80
figure_borders_width = 2
font_size = 24
axis_tick_size = 20
line_width = 2

left = -0.03
bottom = -0.01
right = 1.02
top = 1.05

_, ax = plt.subplots()

plt.plot([phi for (phi, m) in zero], [m for (phi, m) in zero],
         label='0 mode', color='black', linewidth=line_width)

plt.scatter([phi for (phi, m) in stable_points], [m for (phi, m) in stable_points],
            s=marker_area, label='stable', color = 'blue')
plt.scatter([phi for (phi, m) in flat], [m for (phi, m) in flat],
            s=marker_area, label='flat', color = 'green')
if plot_fault:
    plt.scatter([phi for (phi, m) in fault], [m for (phi, m) in fault],
                s=marker_area, label='fault', color = 'black')

plt.legend(prop={'size': font_size}, frameon=False)
plt.title('Calculated oscillation types', fontsize=font_size)
ax.tick_params(axis='both', which='major', labelsize=axis_tick_size)
plt.tight_layout(rect=(left, bottom, right, top))

plt.xlabel('m', fontsize=font_size)
plt.ylabel(r'$\phi$', fontsize=font_size)

for axis in ['top', 'bottom', 'left', 'right']:
    ax.spines[axis].set_linewidth(figure_borders_width)

plt.show()