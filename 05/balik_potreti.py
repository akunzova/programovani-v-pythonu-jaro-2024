# Vrať se k návrhu software pro zásilkovou společnost. U třídy Package uprav atribut state tak, aby byl chráněný. Ověř, že vytváření objektů i výpisy informací o něm fungují.


class Package:
  def __init__(self, address, weight, state):
    self.address = address
    self.weight = weight
    self._state = state

  def __str__(self):
    return f"Balík na adresu {self.address} má hmotnost {self.weight} kg je ve stavu {self._state}."
  
  def delivery_price(self):
    if self.weight < 10:
      price = 129
    elif self.weight < 20:
      price =  159
    else:
      price =  359
    return price 
  
  def deliver(self):
    if self._state == "nedoručeno":
      self._state = "doručeno"
      return "Doručení uloženo"
    else:
      return "Balík již byl doručen."
  

prvni_objekt = Package("Smetanova 7, Olomouc", 9.0, "doručeno")
druhy_objekt = Package("Malovanka 1, Praha", 18, "nedoručeno")

print(prvni_objekt.deliver())
print(druhy_objekt.deliver())