from csv import writer
import csv

def checkdata(e):
    new_list = [e[1], e[2], e[34], e[35], e[37], e[55], e[61], e[64]]
    if '' in new_list:
        return [False, []]
    else:
        return [True, new_list]


def count(start=0, step=1):
    # count(10) --> 10 11 12 13 14 ...
    # count(2.5, 0.5) -> 2.5 3.0 3.5 ...
    n = start
    while True:
        yield n
        n += step

result = []
counter = count()
with open('car_db_metric.csv', 'r') as read_obj:from csv import reader
# open file in read mode

def checkdata(e):
    new_list = [e[1], e[2], e[34], e[35], e[37], e[55], e[61], e[64]]
    if '' in new_list:
        return [False, []]
    else:
        return [True, new_list]


def count(start=0, step=1):
    # count(10) --> 10 11 12 13 14 ...
    # count(2.5, 0.5) -> 2.5 3.0 3.5 ...
    n = start
    while True:
        yield n
        n += step

if False:
    result = []
    counter = count()
    with open('car_db_metric.csv', 'r') as read_obj:
        # pass the file object to reader() to get the reader object
        csv_reader = list(reader(read_obj))[1:]
        # Iterate over each row in the csv using reader object
        for row in csv_reader:
            #row variable is a list that represents a row in csv
            b, element = checkdata(row)
            if b:
                result.append([next(counter)] + element)

        with open('cardb.csv', mode='wb') as car_db_file:
            cardb_writer = csv.writer(car_db_file, delimiter=',')
            cardb_writer.writerow(['make', 'model', 'cylinder_layout', 'number_of_cylinders', 'engine_type', 'mixed_fuel_consumption_per_100km', 'city_fuel_per_100km', 'highway_fuel_per_100km'])
            for row in result:
                cardb_writer.writerow(row)


with open('cardb.csv', 'r') as read_obj:
    lst = list(reader(read_obj))
    r = []
    for e in lst:
        if e[5] not in r:
            r.append(e[5])

    del r[0]
    for e in r:
        print(e)

