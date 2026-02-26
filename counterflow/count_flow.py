import numpy as np


def count_speed(out_pressure, pressure_delta, cp, cv, rho):
    in_pressure = out_pressure + pressure_delta
    pressure_ratio = out_pressure / in_pressure
    gamma = cp / cv

    if pressure_ratio < (2 / (gamma + 1)) ** (gamma / (gamma - 1)):
        return np.sqrt(2 * gamma / (gamma + 1) * in_pressure / rho * pressure_ratio ** (1 / gamma))
    else:
        return np.sqrt(2 * gamma / (gamma - 1) * out_pressure / rho * (pressure_ratio ** ((1 - gamma) / gamma) - 1))


diam = 210  # mcm
pressure = 0.3  # bar
atmos = 1  # bar
density = 1.796  # kg / m^3
heat_capac_volume = 1.49  # kJ / (kg * K)
heat_capac_pressure = 1.692  # kJ / (kg * K)
heat_of_combust = 93.4  # MJ / m^3
viscosity = 8  # mcPa * s
length = 21  # mm
flux = 13.3  # mW / cm^2
flux_radius = 25.5  # cm
re_crit = 4000

tolerance = 0.001
convergence_rate = 0.1

diam *= 1e-6
pressure *= 1e5
atmos *= 1e5
heat_of_combust *= 1e6
viscosity *= 1e-6
length *= 1e-3
flux_radius *= 1e-2
flux *= 10

speed = 0
re = 0
iteration = 0
error = 1
active_pressure = pressure / 2
friction_pressure = pressure / 2

while error > tolerance:
    iteration += 1
    speed = count_speed(atmos, active_pressure, heat_capac_pressure, heat_capac_volume, density)
    re = density * diam * speed / viscosity

    friction_coefficient = 0
    if re < re_crit:
        friction_coefficient = 0.3164 / re ** 0.25
    else:
        friction_coefficient = 1 / (1.8 * np.log10(re) - 1.64) ** 2

    friction_pressure = (friction_coefficient * length / diam + 0.5 + 1) * density * speed ** 2 / 2
    discrepancy = pressure - active_pressure - friction_pressure
    error = np.abs(discrepancy) / pressure
    active_pressure += discrepancy * convergence_rate

flow = 2 * speed * np.pi * (diam / 2) ** 2
power = flow * heat_of_combust
radiation = flux * np.pi ** 2 * flux_radius ** 2

print(f'Flow: {np.round(flow * 3600, 3)} m^3 / h')
print(f'Speed: {np.round(speed)} m / s')
print(f'Power: {np.round(power)} W')
print(f'Radiation: {np.round(radiation)} W')
print(f'Convertion: {np.round(100 * radiation / power)}%')
print(f'Re: {np.round(re)}')
print(f'Friction pressure: {np.round(friction_pressure * 1e-5, 2)} bar')
print(f'Active pressure: {np.round(active_pressure * 1e-5, 2)} bar')
print(f'Iterations: {iteration}')
