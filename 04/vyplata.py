# Zatím jsme výplatu počítali za předpokladu, že každý měsíc odpracujeme stejný počet hodin, což není příliš realistické. Stáhněte si textový soubor vykaz.txt, který obsahuje 12 řádků a na každém řádku počet odpracovaných hodin za každý měsíc za poslední rok.

# Otevřete tento soubor ve svém programu a načtěte hodnoty na řádcích do seznamu vykaz. Vytiskněte tento seznam do terminálu funkcí print() abyste si ověřili, že jste soubor načetli správně.
# Nechte uživatele zadat na příkazovém řádku hodinovou mzdu. Spočítejte a na výstup vytiskněte celkovou výplatu za celý rok a průměrnou výplatu na jeden měsíc.

import sys

prehled_odpracovanych_hodin = list() 

with open ('vykaz.txt', encoding = 'utf-8') as file:
  for line in file:
    prehled_odpracovanych_hodin.append(int(line.strip()))

print (prehled_odpracovanych_hodin)

# nacteni mzdy
mzda = int(sys.argv[1])

vyplata = [ c * mzda for c in prehled_odpracovanych_hodin]
print(vyplata)


rocni_vyplata = sum(vyplata)
print ('Roční výplata: ', rocni_vyplata)

prumerna_vyplata = round(sum(vyplata) /len(vyplata),2)
print ('Průměrná výplata: ', prumerna_vyplata)