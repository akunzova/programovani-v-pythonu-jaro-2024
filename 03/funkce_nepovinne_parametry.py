# Napiš funkci total_price, která vypočte cenu noci v hotelu. Funkce bude mít dva parametry - persons a breakfast. Cena za noc za osobu je 850 Kč a cena za snídani za osobu je 125 Kč. Funkce vrátí výslednou cenu. Parametr breakfast je nepovinný a výchozí hodnota je False.

# Funkci vyzkoušej se zadáním dvou i jedné hodnoty, např. total_price(3), total_price(2, True).

def total_price(persons: int, breakfast:bool = False) -> int:
  price_breakfast = 125
  price_accomodation = 500

  if breakfast:
    return persons * (price_breakfast+price_accomodation)
  else:
    return persons * price_accomodation
  
print(total_price(3))


  