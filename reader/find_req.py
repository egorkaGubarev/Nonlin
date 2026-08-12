import pandas as pd
import tqdm


path = 'C:/Users/gubar/OneDrive/Документы/ФИАН/Квантовая Электроника/requests'
data_path = 'access/access.log.7.txt'
ip_path = 'КЭ_список_IP.xlsx'
out_path = 'access/access.log.7.xlsx'
test_records = 10000
test_mode = False

ranges = []

for row in pd.read_excel(f'{path}/{ip_path}').itertuples(index=False):
    record = row.ip

    for range in record.split(';'):
        ranges.append({'index': row._0, 'id': str(row.ОГРН), 'name': row._2, 'range': range})

with open(f'{path}/{data_path}') as data_file:
    requests = data_file.readlines()

if test_mode:
    requests = requests[:test_records]

good_requests = []

for request in tqdm.tqdm(requests):
    ip_end = request.find(' ')
    ip = request[:ip_end]
    no_ip = request[ip_end:]

    time_start = no_ip.find('[') + 1
    time_end = time_start + no_ip[time_start:].find(' ')
    time = no_ip[time_start: time_end]
    no_time = no_ip[time_end:]

    request_data = no_time[no_time.find('"'): -1]

    for range in ranges:
        start, stop = range['range'].split(' - ')

        if start <= ip <= stop:
            good_requests.append({'index': range['index'], 'id': range['id'], 'name': range['name'],
                                  'ip': ip, 'time': time, 'request data': request_data})

pd.DataFrame(good_requests,
             columns=['id', 'name', 'ip', 'time', 'request data']).to_excel(f'{path}/{out_path}',
                                                                            index=False)
