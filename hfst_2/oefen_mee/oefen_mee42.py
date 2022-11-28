
eruptions_ld_verwerkt = []

for index, rij in enumerate(eruptions_ld):
    dictionary = {}
    dictionary["Year"] = abs(int(rij["Year"]))
    dictionary["Name"] = rij["Name"].lower()
    eruptions_ld_verwerkt.append(dictionary)