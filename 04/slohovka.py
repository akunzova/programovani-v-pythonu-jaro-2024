# Stáhněte si odevzdanou slohovou práci. Zadání bylo sepsat text o nejméně 150ti slovech pojednávající o našem hlavním městě. Napište program, který spočítá počet slov v tomto textu, abychom věděli, zda bylo zadání formálně splněno. Nechte se vést následujícím návodem.

# Nechte váš program otevřít soubor a načíst jednotlivé řádky do seznamu
# Každý řádek převeďte na seznam slov. Slovem se rozumí vše, co je odděleno mezerou nebo novým řádkem
# Vypište na výstup počty slov na každém řádku
# Vypište na výstup celkový počet všech slov v souboru


with open ('slohova_prace.txt', encoding = 'utf-8') as file:
  radky_jako_seznamy_slov = [line.strip().split(' ') for line in file]


#print (radky_jako_seznamy_slov)

pocty_slov_per_radek = [len(radek) for radek in radky_jako_seznamy_slov]
print(pocty_slov_per_radek)


print ("Celkový počet slov v souboru je:",sum(pocty_slov_per_radek))