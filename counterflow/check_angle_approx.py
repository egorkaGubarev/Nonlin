import matplotlib.pyplot as plt
import numpy as np


flux_03 = np.array([8.2, 10.5, 11.9, 13.3])  # mW / cm^2
angle_03 = np.array([53.0, 34.0, 21.0, 0.0])  # deg

flux_06 = np.array([15.5, 21.8, 26.1, 29.3])  # mW / cm^2
angle_06 = np.array([55.0, 38.0, 22.0, 0.0])  # deg

flux_09 = np.array([21.3, 28.0, 33.5, 35.0])  # mW / cm^2
angle_09 = np.array([55.0, 35.0, 17.0, 0.0])  # deg

flux_11 = np.array([26.0, 36.0, 42.0, 49.1])  # mW / cm^2
angle_11 = np.array([52.0, 34.0, 22.0, 0.0])  # deg

interp_points = 100

flux = flux_11 * 10.0
angle = angle_11 * np.pi / 180

angle_ax = np.linspace(np.min(angle), np.max(angle), interp_points)

plt.plot(angle * 180 / np.pi, flux, label='experiment')
plt.plot(angle_ax * 180 / np.pi, np.max(flux) * np.cos(angle_ax), label=r'$J = J_0 cos(\alpha)$')

plt.xlabel(r'$\alpha$')
plt.ylabel(r'$J, \frac{W}{m^2}$')
plt.title('Flux')
plt.legend()
plt.show()
