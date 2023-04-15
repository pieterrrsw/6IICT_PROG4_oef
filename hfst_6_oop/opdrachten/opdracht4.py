class Rechthoek:
    def __init__(self, breedte, hoogte):
        self.breedte = breedte
        self.hoogte = hoogte

    def omtrek(self):
        return 2*self.breedte + 2*self.hoogte
    def oppervlakte(self):
        return self.breedte*self.hoogte
    
    def vergelijk_omtrek(self, omtrek):
        if omtrek < self.omtrek():
            print("Getal is kleiner dan omtrek rechthoek.")
        elif omtrek > self.omtrek():
            print("Getal is groter dan omtrek rechthoek.")
        else:
            print("Getal is gelijk aan omtrek rechthoek.")
    def vergelijk_oppervlakte(self, oppervlakte):
        if oppervlakte < self.oppervlakte():
            print("Getal is kleiner dan opp rechthoek.")
        elif oppervlakte > self.omtrek():
            print("Getal is groter dan opp rechthoek.")
        else:
            print("Getal is gelijk aan opp rechthoek.")
    
    
r1 = Rechthoek(breedte=4, hoogte=5)
r1.vergelijk_omtrek(15)         # Getal is kleiner dan omtrek rechthoek.
r1.vergelijk_oppervlakte(20)    # Getal is groter dan opp rechthoek.