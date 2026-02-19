import numpy as np


def count_speed(out_pressure, pressure_delta, cp, cv, rho):
    in_pressure = out_pressure + pressure_delta
    pressure_ratio = out_pressure / in_pressure
    gamma = cp / cv

    if pressure_ratio < (2 / (gamma + 1)) ** (gamma / (gamma - 1)):
        return np.sqrt(2 * gamma / (gamma + 1) * in_pressure / rho * pressure_ratio ** (1 / gamma))
    else:
        return np.sqrt(2 * gamma / (gamma - 1) * out_pressure / rho * (pressure_ratio ** ((1 - gamma) / gamma) - 1))


diam = 210 # mcm
pressure = 1.1 # bar
atmos = 1 # bar
density = 1.796 #kg / m^3
heat_capac_volume = 1.49 # kJ / (kg * K)
heat_capac_pressure = 1.692 # kJ / (kg * K)
heat_of_combust = 93.4 # MJ / m^3

diam *= 1e-6
pressure *= 1e5
atmos *= 1e5
heat_of_combust *= 1e6

speed = count_speed(atmos, pressure, heat_capac_pressure, heat_capac_volume, density)
flow = 2 * speed * np.pi * (diam / 2) ** 2

print(f'Flow: {np.round(flow * 3600, 3)} m^3 / h')
print(f'Speed: {np.round(speed)} m / s')
print(f'Power: {np.round(flow * heat_of_combust * 1e-3, 1)} kW')
