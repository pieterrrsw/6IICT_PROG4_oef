class Hond:
    def init(self, naam, massa):
        self.naam = naam
        self.massa = massa

    def weegschaal(self):
        print(f"{self.naam} weegt {self.massa}kg")

    def wijzig_naam(self, hernoem):
        print(f"{self.naam} heet nu {hernoem}")
        self.naam = hernoem

    def eten(self, hoeveelheid):
        self.massa += hoeveelheid*0.6
        print(f"{self.naam} weegt nu {self.massa}")

honden = Hond("Lucky", 5)
honden.weegschaal()
honden.wijzig_naam("Bolly")
honden.eten(0.7)