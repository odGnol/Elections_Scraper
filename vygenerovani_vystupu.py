import csv

def zapsat_data(data: dict, jmeno_souboru: str) -> str:
    with open(jmeno_souboru, mode="w", encoding="utf-8", newline="") as csv_soubor:
        sloupce = data.keys()

        zapis = csv.DictWriter(csv_soubor, fieldnames=sloupce)
        zapis.writeheader()

        zapis.writerow(data)