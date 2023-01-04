from dobihtml import DobiHtml
import time
from bs4 import BeautifulSoup
import json


odziv = DobiHtml.dobi_html('http://www.cbz.si/zzzs/pao/bazazdr2.nsf/pregled13?openview&count=20000%27')
soup = BeautifulSoup(odziv, 'html.parser')
vrstice_zdravila = soup.find_all('tr', valign = 'top')


# pridobivamo podatke iz cbz.si

zdravila = dict()

for vrstica_zdravilo in vrstice_zdravila:
    podatki_zdravila = dict()
    
    td_ime = vrstica_zdravilo.find_all('td', class_ = 'textbarva0 gen-5')[0]
    td_sifra = vrstica_zdravilo.find_all('td', class_ = 'textbarva0 ts-s-4-6 ts-sez-c')[0]
    td_imetnik_dovoljenja = vrstica_zdravilo.find_all('td', class_ = "textbarva1")[1]
    td_cena = vrstica_zdravilo.find_all('td', class_ = 'textbarva4', width = '165')[0]
    
    
    td_pakiranje = vrstica_zdravilo.find_all('td', class_ = 'textbarva02')[0]
    
    a_pakiranje = td_pakiranje.find_all('a', class_ = '', href = '#')[0]
    pakiranje = a_pakiranje.contents[0]
    

    a = td_ime.find_all('a')[1]
    ime = a.contents[0]
    sifra = td_sifra.contents[0]
    imetnik_dovoljenja = None if td_imetnik_dovoljenja.contents == [] else td_imetnik_dovoljenja.contents[0]
    cena = td_cena.find_all('center')[0].contents[0]
    
    
    podatki_zdravila['Šifra'] = sifra
    podatki_zdravila['Imetnik dovoljenja'] = imetnik_dovoljenja
    podatki_zdravila['Cena'] = cena
    podatki_zdravila['Pakiranje'] = pakiranje
    # print(ime,sifra, imetnik_dovoljenja, cena) 

    zdravila[ime] = podatki_zdravila

with open('zdravila.json', 'w', encoding='UTF-8') as file:
    json.dump(zdravila,file)

