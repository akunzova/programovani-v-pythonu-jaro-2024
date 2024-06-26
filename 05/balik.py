# Uvažuj, že navrhuješ software pro zásilkovou společnost.

# Vytvoř třídu Package, která bude mít tři atributy - address, weight a state. Vytvoř metodu __init__, která uloží hodnoty parametrů metody do atributů.
# Přidej metodu get_info(), která vrátí informace o balíku jako řetězec. Uvažuj například větu "Balík na adresu Václavské Náměstí 12, Praha má hmotnost 0.25 kg je ve stavu nedoručen".
# Zkus si vytvořit alespoň dva objekty ze třídy Balik. U address uvažujeme typ řetězec (str), u weight desetinné číslo. U atributu state zadávej pro zjednodušení pouze dva stavy: doručen a nedoručen.
# Vypiš informace, které generuje metoda get_info(), na obrazovku, a ověř, že je vše v pořádku.
# Vytvoř metodu delivery_price(), která vypočítá cenu přepravy balíku. Cena přepravy je daná hmotností balíku. Cena přepravy balíku do 10 kg je 129 Kč, cena přepravy balíku od 10 kg do 20 kg je 159 Kč a cena přepravy balíků těžších než 20 kg je 359 Kč. Metoda spočítá cenu a vrátí ji jako číslo.

class Package:
  def __init__(self, address, weight, state):
    self.address = address
    self.weight = weight
    self.state = state

  def get_info(self):
    return f"Balík na adresu {self.address} má hmotnost {self.weight} kg je ve stavu {self.state}."
  
  def delivery_price(self):
    if self.weight < 10:
      price = 129
    elif self.weight < 20:
      price = 159
    else:
      price = 359
    return price
  

prvni_objekt = Package("Smetanova 7, Opava", 6.6, "doručeno")
druhy_objekt = Package("Malovanka 1, Veselí nad Lužnicí", 18, "nedoručeno")

print (prvni_objekt.get_info())
print(prvni_objekt.delivery_price())

print(druhy_objekt.get_info())
print(druhy_objekt.delivery_price())