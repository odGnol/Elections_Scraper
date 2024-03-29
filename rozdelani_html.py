
def ziskat_odpoved(odkaz):
    import requests as r
    return r.get(odkaz)

def rozdelat_html(res):
    import bs4 as bs
    return bs.BeautifulSoup(res.text, features="html.parser")

def najit_tag(tag, vars):
    return tag.find_all(vars)

def najit_vsechny_tagy(tag, typ):
    return tag.find_all(typ)

def vytvorit_odkaz_k_obci(base_url, cast_odkazu):
   return f"{base_url}{cast_odkazu}"

def najit_konkretni_tag(tag, hledanyTag: str, attr: dict):
    return tag.find(hledanyTag, attr)

def vratit_vysledek(kod_obce, nazev_obce, volici_v_seznamu, vydane_obalky, platne_hlasy, strany):
    vysledek = dict()
    vysledek.update({"Kód obce": kod_obce,
                             "Název obce": nazev_obce,
                             "Voliči v seznamu": volici_v_seznamu.text,
                             "Vydané obálky": vydane_obalky.text,
                             "Platné hlasy": platne_hlasy.text})
    for klic in strany.keys():
        vysledek.update({klic: strany[klic]})

    return vysledek