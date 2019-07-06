import csv

#var inf , open file1
with open("ki.xyz") as inf:
    data = list(csv.reader(inf, delimiter=','))
#sort by first array [0]
m = sorted(data, key=lambda data_entry: int(data_entry[0]))
#var outf, open file2
with open("sorted.txt", "a") as outf:
    csv.writer(outf, delimiter=',').writerows(m)