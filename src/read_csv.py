import csv


def read_csv(csvfile):
    with open(csvfile, 'r') as csv_file:
        reader = list(csv.reader(csv_file))
        line_162 = reader[162]
        print(line_162)

read_csv(r'C:\Users\archa\Documents\bellevue_University\msds510\data\interim\avengers_utf8.csv')