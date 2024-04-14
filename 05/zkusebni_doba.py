# U zaměstnanců budeme nově evidovat, jestli jsou ve zkušební době.

# Rozšiř metodu __init__ třídy Employee o parametr probation_period. Tuto hodnotu ulož jako atribut třídy Employee.
# Uprav metodu __str__. Pokud je zaměstnanec ve zkušební době, přidej k jeho/jejímu výpisu text Je ve zkušební době.

class Employee:
  def __init__(self, probation_period):
    self.probation_period = probation_period
  
  def __str__(self):
    if self.probation_period:
      return "Zaměstnanec je ve zkušební době"
    return "Zaměstnanec není ve zkušební době"
  

eva = Employee(True)

print(eva)