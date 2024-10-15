import csv
f = "/Users/luis/libasl/biblioteca-asl/data/cat.csv"

with open(f, newline='') as csvfile:
    l=[]
    reader = csv.DictReader(csvfile, fieldnames=["num", "titolo", "autore", "editore","gen"],delimiter=";")
    for row in reader:
        l.append([row['titolo'], row['autore'], row['editore'], row['gen']])
    l=l[1:]
print(l)