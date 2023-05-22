class Hond:

    def benoem(self, benaming):
        self.naam = benaming
    
    def wegen(self, massa):
        self.gewicht = massa
    
    def blaf(self):
        print(f'{self.naam} zegt blaf.')

    def weegschaal(self):
        print(f'{self.naam} weegt {self.gewicht}kg.')

dier = Hond()
dier.benoem("Menno")
dier.wegen(65)
dier.weegschaal()