import csv

def zapsat_data(data: dict, jmeno_souboru: str) -> None:
    with open(jmeno_souboru, mode="w", encoding="utf-8", newline="") as csv_soubor:
        sloupce = data[0].keys()

        zapis = csv.DictWriter(csv_soubor, fieldnames=sloupce)
        zapis.writeheader()

        zapis.writerows(data)

        print(f"Data se zapsala do souboru: '{jmeno_souboru}'. 🚨")