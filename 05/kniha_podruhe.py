# Vrať se k práci se třídou Book. Pokud jsi ji nestihl(a) v minulé části vytvořit, vrať se nejprve k zadání příkladu na předchozí stránce a třídu si vytvoř.

# U knihy budeme chtít evidovat, kolik kusů bylo prodáno. Přidej atribut sold, jehož hodnotu bude možné nastavit v metodě __init__(). Dále přidej atribut costs, které představují náklady na jednu knihu (např. tisk, doprava do knihkupectví, podíl autora (autorky) atd.).
# Přidej metodu profit(), která vrátí celkový zisk z knihy. Zisk vypočti na základě vzorce: prodané kusy * (cena - náklady).
# Přidej metodu rating(), která vrátí hodnocení knihy na základě jejího zisku. Pokud bude zisk méně než 50 tisíc, vrať hodnotu "propadák". Pokud bude zisk mezi 50 tisíc a 500 tisíc, vrať hodnotu "průměr". Pokud bude vyšší než 500 tisíc, vrať hodnotu "bestseller".

class Book:
  def __init__(self, title, pages, price, sold):
    self.title = title
    self.pages = pages
    self.price = price
    self.sold = sold
    cena_za_distribuce = 100
    podil_autora = self.pages * 1
    self.cost = cena_za_distribuce  + podil_autora

  def get_info(self):
    return print(f"Kniha s názvem {self.title} ma celkem {self.pages} stránek a stojí {self.price} Kč.")
  
  def get_time_to_read(self, read_spead=4):
    """
    Čas potřebný k přečtení knihy
    """
    time = round(self.pages*read_spead / 60,2)
    return time 
  
  def profit(self):
    return self.sold * (self.price - self.cost)
  
  def rating(self):
    if self.profit() < 50000:
      return "Propadak"
    elif self.profit() >= 50000 and self.profit() < 500000:
      return "Prumer"
    else:
      return "bestseller"


jmeno_ruze = Book(title="Jméno Růže", pages=430, price=535, sold=26000)

print (jmeno_ruze.profit())
print (jmeno_ruze.rating())