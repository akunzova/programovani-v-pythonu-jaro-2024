class Package:
    def __init__ (self, address, weight, state):
        self.address = address
        self.weight = weight
        self.state = state
        
    def __str__ (self):
        return f"Balík na adresu {self.address} má hmotnost {self.weight} je ve stavu {self.state}"
    
    def kontrola_stavu(self):
        if self.state in ["doruceno","dfsd"]:
            print("zadane spravne hodnoty")
        else:
            print("Toto neocekavana hodnota")

    def deliver (self):
        if self.state == "doručen":
            print("Balík již byl doručen")
        else:
            self.state = "doručen"
            print("Doručení uloženo")    


balik1 = Package ("Václavské Náměstí 12, Praha", 0.25, "doručen")
balik2 = Package ("Karlovo náměstí 34, Praha", 0.6, "nedoručen")
print(balik1)
balik1.deliver()
print(balik2)
balik2.deliver()
print(balik2)