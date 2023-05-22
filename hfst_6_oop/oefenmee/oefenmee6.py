class Hond:
    
    def __init__(self, benoem, wegen):
        self.benoem = benoem
        self.wegen = wegen

    def weegschaal(self):
        print(f'{self.benoem} weegt {self.wegen}kg.')

hond = Hond('Menno', 65)
hond.weegschaal()
hond_2 = Hond('Jef', 70)
hond_2.weegschaal()