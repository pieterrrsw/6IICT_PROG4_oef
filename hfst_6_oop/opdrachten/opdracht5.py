class Rechthoek:
    def __init__(self, breedte, hoogte, x, y):
        self.breedte = breedte
        self.hoogte = hoogte
        self.x = x
        self.y = y

    def omtrek(self):
        return 2*self.breedte + 2*self.hoogte
    def oppervlakte(self):
        return self.breedte*self.hoogte
    
    def overlapt_met(self, rechthoek):
        if type(rechthoek) != Rechthoek:
            return "Argument is geen Rechthoek"
        
        return ((self.x+self.breedte)> rechthoek.x and self.x < (rechthoek.x+rechthoek.breedte) and (self.y+self.hoogte) > self.y and self.y < (rechthoek.y+rechthoek.hoogte))

class Punt:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def zit_in(self, rechthoek):
        if not (rechthoek.x <= self.x <= rechthoek.x+rechthoek.breedte):
            return False
        if not (rechthoek.y <= self.y <= rechthoek.x+rechthoek.hoogte):
            return False
        return True   
    
r1 = Rechthoek(breedte=4, hoogte=5, x=3, y=3)
r2 = Rechthoek(breedte=4, hoogte=4, x=0, y=0)
r3 = Rechthoek(breedte=4, hoogte=4, x=100, y=100)
p1 = Punt(x=5, y=7)

print(r1.overlapt_met(r2)) # True
print(r1.overlapt_met(r3)) # False
print(r1.overlapt_met(p1)) # Argument is geen Rechthoek