eruptions_ll_verwerkt = []

for index, rij in enumerate(eruptions_ll):
    if index == 0:
        eruptions_ll_verwerkt.append([rij[1], rij[4]])
    else: 
        eruptions_ll_verwerkt.append([abs(int(rij[1])), rij[4].lower()])

print(eruptions_ll_verwerkt)