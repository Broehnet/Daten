from csv import reader
import csv

with open('cardbe.csv', 'r') as obj:
    csv_reader = list(reader(obj))
    del csv_reader[0]

    csv_reader = [','.join(x) for x in csv_reader]

    csv_reader.sort()

    csv_reader = [x.split(',') for x in csv_reader]

    with open('cardbf.csv', mode='wb') as car_db_file:
        cardb_writer = csv.writer(car_db_file, delimiter=',')
        cardb_writer.writerow(['make', 'model', 'trim', 'cylinder_layout', 'number_of_cylinders', 'engine_type', 'mixed_fuel_consumption_per_100km', 'city_fuel_per_100km', 'highway_fuel_per_100km'])
        for row in csv_reader:
            cardb_writer.writerow(row)
