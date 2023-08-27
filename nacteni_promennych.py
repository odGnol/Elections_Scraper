def validovat_promenne(sys_argv):
   nazev_souboru_py = sys_argv[0] 
   odkaz_stranky = sys_argv[1]
   nazev_souboru_csv = sys_argv[2]

   if len(sys_argv) != 3:
      print(f"Soubor: {nazev_souboru_py} potřebuje povinné argumenty s odkazem na stránky a se jménem CSV souboru.")
      quit()
   elif "https://volby.cz/pls/ps2017nss/" not in odkaz_stranky:
      print(f"Odkaz stránky: {odkaz_stranky} nemá validní adresu.")
      quit()
   elif not nazev_souboru_csv.endswith(".csv"):
      print(f"Název souboru: {nazev_souboru_csv} není ve formátu CSV!")
      quit()
   
   print("Spouštím soubor!")
   
   return [odkaz_stranky, nazev_souboru_csv]

# testovani
# okres_odkaz = "https://volby.cz/pls/ps2017nss/ps32?xjazyk=CZ&xkraj=12&xnumnuts=7103"
# nazev_souboru = f"vysledky_tst.csv"