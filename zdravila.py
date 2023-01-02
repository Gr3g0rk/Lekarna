from bralnik import Bralnik
import time
from bs4 import BeautifulSoup
odziv = Bralnik.pridobi_html('http://www.cbz.si/zzzs/pao/bazazdr2.nsf/pregled13?openview&count=20000%27')
soup = BeautifulSoup(odziv, 'html.parser')
vrstice_zdravila = soup.find_all('tr', valign = 'top')


for vrstica_zdravilo in vrstice_zdravila:
    td_ime = vrstica_zdravilo.find_all('td', class_ = 'textbarva0 gen-5')[0]
    td_sifra = vrstica_zdravilo.find_all('td', class_ = 'textbarva0 ts-s-4-6 ts-sez-c')[0]
    td_imetnik_dovoljenja = vrstica_zdravilo.find_all('td', class_ = "textbarva1")[1]


    a = td_ime.find_all('a')[1]
    ime = a.contents[0]
    sifra = td_sifra.contents[0]
    imetnik_dovoljenja = None if td_imetnik_dovoljenja.contents == [] else td_imetnik_dovoljenja.contents[0]
    print(ime,sifra, imetnik_dovoljenja) 

# for vrstica_zdravilo in vrstice_zdravila:
#     td_sifra = vrstica_zdravilo.find_all('td', class_ = 'textbarva0 ts-s-4-6 ts-sez-c')[0] # ce ni indeksou vrne tabelo z 1 el, ti pa isces vrednost el
#     #a = td_ime.find_all('a')[1]
#     sifra = td_sifra.contents[0]
#     print(sifra)