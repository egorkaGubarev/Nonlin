import json
import pandas as pd


path = 'C:/Users/gubar/OneDrive/Документы/ФИАН/Квантовая Электроника/requests'
in_path = 'good.json'
ip_path = 'КЭ_список_IP.xlsx'

with open(f'{path}/{in_path}') as in_file:
    for number, org in json.load(in_file).items():
        print(org)
