import json
import csv

def json2csv(filename):
    json_file = open(filename)
    data = json.load(json_file)
    json_file.close()
        
    csv_data = data['data']
    data_file = open('data.csv', 'w')

    csv_writer = csv.writer(data_file)
    count = 0

    for item in csv_data:
        if count == 0:
            header = item.keys()
            csv_writer.writerow(header)
            count += 1

        csv_writer.writerow(item.values())

    data_file.close()
