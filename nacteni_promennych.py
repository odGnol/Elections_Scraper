# TODO je možné zlepšit validaci ?
def validovat_odkaz(odkaz):
   import requests as r

   ziskat_odkaz = r.get(odkaz)
   
   if ziskat_odkaz.status_code != 200:
      return False

   return True

def validovat_promenne(sys_argv: list) -> bool:
   nazev_souboru_py = sys_argv[0]
   
   if len(sys_argv) != 3:
      print(f"Soubor: {nazev_souboru_py} potřebuje povinné argumenty, tj. odkaz na stránky a název CSV souboru.")
      return False
    
   odkaz_stranky = sys_argv[1]
   nazev_souboru_csv = sys_argv[2]

   if "https://volby.cz/pls/ps2017nss/" not in odkaz_stranky:
      print(f"Odkaz stránky: {odkaz_stranky} nemá validní adresu.")
      return False

   odkaz_je_validni = validovat_odkaz(odkaz_stranky)

   if odkaz_je_validni is False:
      print(f"Zkontrolujte odkaz stránky: {odkaz_stranky}, nemá validní adresu.")
      return False
   
   if not nazev_souboru_csv.endswith(".csv"):
      print(f"Název souboru: {nazev_souboru_csv} není ve formátu CSV!")
      return False
   
   print("Nechť scraping započne... 👾")
   
   return True