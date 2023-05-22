class Hond:
    naam = "Ollie"
    massa = 25

hond = Hond()


print(hond.naam)
print(hond.massa)

honden = []

for _ in range(10):
    honden.append(Hond())

for index,hond in enumerate (honden):
    print(f'Hond {index} heet {hond.naam}')
