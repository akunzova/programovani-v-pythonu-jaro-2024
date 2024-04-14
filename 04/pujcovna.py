# Půjčovna aut má v každém kraji ČR jedno auto s danou SPZ. Ke konci roku chce zjistit, kolik všechna auta najezdila dohromady kilometrů. V souboru auta.txt je pro každou SPZ zaznamenáno kolik dané auto ujelo kilometrů za daný rok. Hodnoty jsou v tisících kilometrů. Bohužel se v jednotlivých krajích blbě zkoordinovali a někdo používal desetinnou čárku, někdo zase tečku.

# Pozor! V souboru s daty je ještě jeden problém, který není na první pohled vidět!

# Napište program, který na výstup vypíše součet všech ujetých kilometrů. Jistě se vám bude hodit metoda řetězců jménem replace().

import sys
file = open ('auta.txt', encoding = 'utf-8')
data = [line.strip() for line in file]
file.close()


print(data)
uprava_dat = [d.replace(',', '.') for d in data]

#print(uprava_dat)
seznam_dat = [d.split(' ') for d in uprava_dat]

print(seznam_dat)

kilometry = [ float(s[1]) for s in seznam_dat]
pocet_kilometru = sum(kilometry)
print ('Počet ujetých kilometrů', pocet_kilometru, 'km')

