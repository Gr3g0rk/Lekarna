import sqlite3
import projekt
# SAMO V TEM FILU SE LAHKO POGOVARJAS DIREKTNO Z BAZO, DRUGE SAMO PREKO model.py fila

conn = sqlite3.connect("lekarna.sqlite3")

projekt.pripravi_vse(conn)



class Model:
    def dobi_vse_uporabnike(self):
        with conn:
            cur = conn.execute("""
            Select * from zdravila
            """)
            return cur.fetchall
