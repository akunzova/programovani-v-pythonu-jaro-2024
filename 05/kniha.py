# Zkus pro nakladatelství vytvořit software s využitím tříd a objektů. Vytvoř tedy třídu Book, která reprezentuje knihu. Každá kniha bude mít atributy title, pages a price. Hodnoty nastav ve funkci __init__.

# Přidej knize funkci get_info(), která vypíše informace o knize v nějakém pěkném formátu.
# Přidej metodu get_time_to_read(). Metoda vrátí čas potřebný na přečtení knihy v hodinách. S využitím atributu pages vypočítej čas na přečtení knihy. Metoda bude mít nepovinný parametr, který udává počet minut potřebných pro přečtení jedné stránky knihy. Dobu potřebnou na přečtení knihy získáš jako násobek doby potřebné na přečtení jedné stránky knihy a počet stránek knihy. Výchozí hodnota nepovinného parametru je 4.

class Book:
  def __init__(self, title, pages, price):
    self.title = title
    self.pages = pages
    self.price = price

  def get_info(self):
    """
    Vrací základní info o knizce v čitelné podobě.
    """
    return print(f"Kniha s názvem {self.title} ma celkem {self.pages} stránek a stojí {self.price} Kč.")
  
  def get_time_to_read(self, read_spead=4):
    """
    Vypočítá čas potřebný k přečtení vybrané knížky v hodinách.
    """
    time_to_read = round(self.pages*read_spead / 60, 2)
    return time_to_read 
  
# vytvoreni instance jmeno_ruze 
jmeno_ruze = Book("Jméno Růže", 430, 535)

print(f"Knihu {jmeno_ruze.title} stihnete přečíst za {jmeno_ruze.get_time_to_read(5)} hodin.")