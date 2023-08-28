import sys
from nacteni_promennych import validovat_promenne
from rozdelani_html import ziskat_odpoved, rozdelat_html, najit_vsechny_tagy, vytvorit_odkaz_k_obci, najit_konkretni_tag, vratit_vysledek
from vygenerovani_vystupu import zapsat_data

def spustit_scraper(): 
    strany = dict()
    vystup_txt: list() = []
    obec_odkaz = ""

    promenne_lze_nacist = validovat_promenne(sys.argv)
    
    if promenne_lze_nacist:
        odkaz_stranky = sys.argv[1]
        nazev_souboru = sys.argv[2]
    else:
        quit()

    odpoved = ziskat_odpoved(odkaz_stranky)
    rozdelene_html = rozdelat_html(odpoved)
    tables = najit_vsechny_tagy(rozdelene_html, 'table')

    for table in tables:
        tr_tags = najit_vsechny_tagy(table, 'tr')
        for row in tr_tags:
            # TODO def
            td_tags = row.find_all('td', ['cislo', 'overflow_name'])
            if(td_tags != []):
                obec_odkaz = vytvorit_odkaz_k_obci("https://volby.cz/pls/ps2017nss/", td_tags[0].a.get("href"))
                odpoved = ziskat_odpoved(obec_odkaz)
                rozdelene_html = rozdelat_html(odpoved)
                tables = najit_vsechny_tagy(rozdelene_html, 'table')

                for table in tables[1::]:
                    rows = najit_vsechny_tagy(table, 'tr')
                    for row in rows:
                        column = najit_vsechny_tagy(row, 'td')
                        if column != [] and column[1].text != "-":
                            klic = column[1].text
                            hodnota = column[2].text
                            strany.update({klic: hodnota})

                vystup_txt = vratit_vysledek(td_tags[0].text,
                                        td_tags[1].text,
                                        najit_konkretni_tag(tables[0], 'td', {"headers": "sa2"}),
                                        najit_konkretni_tag(tables[0], 'td', {"headers": "sa3"}),
                                        najit_konkretni_tag(tables[0], 'td', {"headers": "sa6"}),
                                        strany)

    zapsat_data(vystup_txt, nazev_souboru)