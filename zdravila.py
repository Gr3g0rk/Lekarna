from bralnik import Bralnik
from bs4 import BeautifulSoup
odziv = Bralnik.pridobi_html('http://www.cbz.si/zzzs/pao/bazazdr2.nsf/pregled13?openview&count=20000%27')
soup = BeautifulSoup(odziv, 'html.parser')
vrstice_zdravila = soup.find_all('tr', valign = 'top')


for vrstica_zdravilo in vrstice_zdravila:
    td_ime = vrstica_zdravilo.find_all('td', class_ = 'textbarva0 gen-5')[0]
    a = td_ime.find_all('a')[1]
    ime = a.contents[0]
    print(ime)

