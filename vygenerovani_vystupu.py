# Ve výstupu (soubor .csv) každý řádek obsahuje informace pro konkrétní obec.

# kód obce
# název obce
# voliči v seznamu
# vydané obálky
# platné hlasy
# kandidující strany (co sloupec, to počet hlasů pro stranu pro všechny strany).

# codelab
import csv
import traceback


def zapis_data(data: list, jmeno_souboru: str) -> str:
    """
    Zkus zapsat udaje z par. 'data' do souboru formatu .csv.
    """
    with open(jmeno_souboru, mode="w", encoding="utf-8", newline="") as csv_soubor:
        sloupce = data[0].keys()

        zapis = csv.DictWriter(csv_soubor, fieldnames=sloupce)
        zapis.writeheader()
        zapis.writerows(data)