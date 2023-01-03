from dobihtml import DobiHtml

from bs4 import BeautifulSoup

odziv = DobiHtml.dobi_html('http://www.cbz.si/zzzs/pao/bazazdr2.nsf/pregled13?openview&count=20000%27')
soup = BeautifulSoup(odziv, 'html.parser')
vrstice_zdravila = soup.find_all('tr', valign = 'top')


# pridobivamo podatke iz cbz.si

for vrstica_zdravilo in vrstice_zdravila:
    td_ime = vrstica_zdravilo.find_all('td', class_ = 'textbarva0 gen-5')[0]
    td_sifra = vrstica_zdravilo.find_all('td', class_ = 'textbarva0 ts-s-4-6 ts-sez-c')[0]
    td_imetnik_dovoljenja = vrstica_zdravilo.find_all('td', class_ = "textbarva1")[1]
    td_cena = vrstica_zdravilo.find_all('td', class_ = 'textbarva4', width = '165')[0]
    td_pakiranje = vrstica_zdravilo.find_all('td', class_ = 'textbarva02', width = '380')[0]


    a = td_ime.find_all('a')[1]
    ime = a.contents[0]
    sifra = td_sifra.contents[0]
    imetnik_dovoljenja = None if td_imetnik_dovoljenja.contents == [] else td_imetnik_dovoljenja.contents[0]
    cena = td_cena.find_all('center')[0].contents[0]
    # pakiranje = td_pakiranje.find_all('title')[0].contents
    # print(pakiranje)

    print(ime,sifra, imetnik_dovoljenja, cena) 




# for vrstica_zdravilo in vrstice_zdravila:
#     td_sifra = vrstica_zdravilo.find_all('td', class_ = 'textbarva0 ts-s-4-6 ts-sez-c')[0] # ce ni indeksou vrne tabelo z 1 el, ti pa isces vrednost el
#     #a = td_ime.find_all('a')[1]
#     sifra = td_sifra.contents[0]
#     print(sifra)