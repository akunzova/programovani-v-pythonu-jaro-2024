# https://kodim.cz/czechitas/uvod-do-progr-2/uvod-do-programovani-2/vlastni-funkce/excs
# 1. Násobení
# Napiš funkci mult, která bude mít dva číselné parametry. Funkce oba parametry vynásobí a vrátí výsledek.

def mult(cislo1: int, cislo2: int):
  vysledek = cislo1 * cislo2
  return vysledek


print(f"Vysledek me mult funkce {mult(3,1)}")

# 2. Funkce pro převody jednotek
# https://kodim.cz/czechitas/uvod-do-progr-2/uvod-do-programovani-2/vlastni-funkce/excs/prevody-jednotek

# Staci treba dve, vsechny jsou na stejny princip :)

def kilometry_na_mile(kilometry: int):
  return kilometry*0.621371

def mile_na_kilometry(mile: int):
  return mile / 0.621371

print(f"Prevod kilometru na mile: {kilometry_na_mile(1)}")
print(f"Prevod mile na kilometr: {mile_na_kilometry(8.1)}")

# [BONUS] 3. Rámeček

# Zadej slovo: ahoj
# ********
# * ahoj *
# ********

def ramecek(slovo, znak_ramecku):
  radek_znaku = (len(slovo)*znak_ramecku) + 4*znak_ramecku
  print (radek_znaku)
  print (f"{znak_ramecku} {slovo} {znak_ramecku}")
  print(radek_znaku)


ramecek("ahoj", "*")


# [BONUS] 4. Měsíc narození

# Napiš funkci month_of_birth, která bude mít jeden parametr - rodné číslo. Funkce ze zadaného rodného čísla určí měsíc narození, které vrátí jako výstup. Nezapomeň, že pro ženy je k měsíci připočtena hodnota 50.

#Příklad: Pro hodnotu 9207054439 vrátí 7. Pro hodnotu 9555125899 vrátí 5.

def month_of_birth(rc):
  mesic = str(rc)[2:4]
  if int(mesic) > 50:
    return int(mesic)-50
  return mesic

#print(month_of_birth(9555125899))
