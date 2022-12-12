import sqlite3 
import csv 

db = sqlite3.connect('lekarna.sqlite3')
with db as cursor: #automatsko zapre kurzor
    cursor.execute("""CREATE TABLE IF NOT EXISTS zdravila 
    (nacionalnaSifra INTEGER PRIMARY KEY,
    imeZdravila TEXT,
    pakiranje TEXT, 
    imetnikDovoljenja TEXT,
    cena INTEGER""")
    pass

with db as conn:
    cursor = conn.cursor()
    with open('zdravila.csv','r',encoding= 'UTF-8') as f:
        # definiramo header
        file_reader = csv.DictReader(f,fieldnames= ['nacionalnaSifra', 'imeZdravila', 'pakiranje', 'imetnikDovoljenja', 'cena'], delimiter=';')
        
        # se znembimo headerja
        next(file_reader) 

        #dodamo ostale elemente v bazo
        for row in file_reader:
            nacionalnaSifra = row['nacionalnaSifra']
            imeZdravila = row['imeZdravila']
            pakiranje = row['pakiranje']
            imetnikDovoljenja = row['imetnikDovoljenja']
            cena = row['cena']
            cursor.execute(''' INSERT INTO zdravila (nacionalnaSifra, imeZdravila, pakiranje, imetnikDovoljenja, cena)
                                VALUES (?,?,?,?,?)''', (nacionalnaSifra, imeZdravila, pakiranje, imetnikDovoljenja, cena))

# print(podatki)
# def napolni_zdravila():
#     with db as cursor:
#         for (nacionalnaSifra, imeZdravila, pakiranje, imetnikDovoljenja, cena) in podatki:
#             cursor.execute(''' INSERT INTO zdravila (nacionalnaSifra, imeZdravila, pakiranje, imetnikDovoljenja, cena)
#                                     VALUES (?,?,?,?,?)''', (nacionalnaSifra, imeZdravila, pakiranje, imetnikDovoljenja, cena))
#             #print(cursor.lastrowid)


