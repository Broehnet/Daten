from _csv import reader
from csv import writer
import csv



def count(start=0, step=1):
    # count(10) --> 10 11 12 13 14 ...
    # count(2.5, 0.5) -> 2.5 3.0 3.5 ...
    n = start
    while True:
        yield n
        n += step

result = []
counter = count()


def checkdata(e):
    new_list = [e[1], e[2], e[7],  e[34], e[35], e[37], e[55], e[61], e[64]]
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

if __name__ == '__main__':
    result = []
    counter = count()
    result2 = ['d']
    with open('car_db_metric.csv', 'r') as read_obj:
        # pass the file object to reader() to get the reader object
        csv_reader = list(reader(read_obj))[1:]
        # Iterate over each row in the csv using reader object
        for row in csv_reader:
            #row variable is a list that represents a row in csv
            b, element = checkdata(row)
            if b:
                result.append(element)
        b = False
        for e in result:
            for f in result2:
                if ','.join(e[:3]) == ','.join(f[:3]):
                    b = True
            if not b:
                result2.append(e)
            b = False

        del result2[0]



        with open('cardbe.csv', mode='wb') as car_db_file:
            cardb_writer = csv.writer(car_db_file, delimiter=',')
            cardb_writer.writerow(['make', 'model', 'trim', 'cylinder_layout', 'number_of_cylinders', 'engine_type', 'mixed_fuel_consumption_per_100km', 'city_fuel_per_100km', 'highway_fuel_per_100km'])
            for row in result2:
                cardb_writer.writerow(row)








