import csv


with open(r'C:\Users\archa\Documents\bellevue_University\msds510\data\raw\avengers.csv', 'r') as csv_file:
    reader = csv.reader(csv_file)
    with open(r'C:\Users\archa\Documents\bellevue_University\msds510\data\interim\avengers_utf8.csv', 'w', encoding='utf-8', newline="") \
        as csv_file_w:
        writer = csv.writer(csv_file_w)
        writer.writerows(reader)


