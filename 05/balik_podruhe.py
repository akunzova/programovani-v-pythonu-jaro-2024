# Vrať se k návrhu software pro zásilkovou společnost.

# U třídy Package přejmenuj metodu get_info() na __str__() a vyzkoušej, jestli nyní stačí k získání informací o balíku funkce print().
# Přidej metodu deliver(). Půjde o obdobu tlačítka, které řidič nebo řidička zmáčkne při doručení balíku a zaznamená tak jeho doručení. Metoda nejprve zkontroluje, zda balík náhodou již není ve stavu doručen. Pokud ano, metoda vrátí zprávu "Balík již byl doručen". Tím bude řidič (řidička) informován(a) o tom, že se pravděpodobně spletl(a) a snaží se zaznamenat doručení u špatného balíku. Pokud balík není ve stavu doručen, změň jeho stav právě na doručen a vrať zprávu "Doručení uloženo".
# Vyzkoušej metodu deliver(). Co se stane, pokud ji u jednoho balíku zavoláš dvakrát?

class Package:
  def __init__(self, address, weight, state):
    self.address = address
    self.weight = weight
    self.state = state

  def __str__(self):
    return f"Balík na adresu {self.address} má hmotnost {self.weight} kg je ve stavu {self.state}."
  
  def delivery_price(self):
    if self.weight < 10:
      price = 129
    elif self.weight < 20:
      price =  159
    else:
      price =  359
    return price 
  
  def deliver(self):
    if self.state == "nedoručeno":
      self.state = "doručeno"
      return "Doručení uloženo"
    else:
      return f"Balík na adresu: {self.address} již byl doručen."
  

prvni_objekt = Package("Smetanova 7, Olomouc", 9.0, "doručeno")
druhy_objekt = Package("Malovanka 1, Praha", 18, "nedoručeno")

print("zakladni_info prvni objekt:", prvni_objekt)
print("prvni balik: ",prvni_objekt.deliver())
print("druhy balik poprve", druhy_objekt.deliver())
print("druhy balik podruhe", druhy_objekt.deliver())