#PERSONE INFORMATICAMENTE STUDIATE CHE VEDETE STA ROBA ORRENDA NON ROMPETE IL CAZZO PERCHÉ SO BENE QUANTO FACCIA SCHIFO

import csv
f = "/Users/luis/libasl/biblioteca-asl/data/catd.csv"

with open(f, newline='') as csvfile:
    booklist=[]
    reader = csv.DictReader(csvfile, fieldnames=["num", "titolo", "autore", "editore","gen"],delimiter=";")
    for row in reader:  
        booklist.append([row['titolo'], row['autore'], row['editore'] if len(row["editore"])>0 else "?", row['gen']])
    booklist=booklist[1:]
print(booklist)

catd = "/Users/luis/libasl/biblioteca-asl/src/catalogodispense.html"
with open(catd, "w") as c:
    count = 1
    c.write("<!DOCTYPE html>\n<html><style>table, th, td {border:1px solid black;}</style><head><title>Catalogo dispense</title></head>\n<body><h1>Catalogo Dispense Aula Studio Liberata </h1>\n<table>")
    c.write("<tr>\n <th>N°</th><th>Titolo</th>\n   <th>Autore</th>\n   <th>Editore</th>\n <th>Area</th>\n</tr>\n")
    for b in booklist:
        c.write("<tr>\n")
        c.write(f"<td>{count}</td>")
        count+=1
        for entry in b:
            c.write(f"  <td>{entry}</td>\n")
        c.write("</tr>\n")
    c.write("</table>\n</body>\n</html>")


f = "/Users/luis/libasl/biblioteca-asl/data/catl.csv"
with open(f, newline='') as csvfile:
    booklist=[]
    reader = csv.DictReader(csvfile, fieldnames=["num", "titolo", "autore", "editore","cas"],delimiter=";")
    for row in reader:  
        booklist.append([row['titolo'], row['autore'] if len(row["autore"])>0 else "?", row['editore'] if len(row["editore"])>0 else "?", row['cas'] if len(row["cas"]) > 0 else "da definire"])
    booklist=booklist[1:]
print(booklist)

catl = "/Users/luis/libasl/biblioteca-asl/src/catalogolibri.html"
with open(catl, "w") as c:
    count = 1
    c.write("<!DOCTYPE html>\n<html><style>table, th, td {border:1px solid black;}</style><head><title>Catalogo libri</title></head>\n<body><h1>Catalogo Libri Aula Studio Liberata </h1>\n<table>")
    c.write("<tr>\n <th>N°</th><th>Titolo</th>\n   <th>Autore</th>\n   <th>Editore</th>\n <th>Scaffale</th>\n</tr>\n")
    for b in booklist:
        c.write(f"<tr>\n<td>{count}</td>")
        count+=1
        for entry in b:
            c.write(f"  <td>{entry}</td>\n")
        c.write("</tr>\n")
    c.write("</table>\n</body>\n</html>")