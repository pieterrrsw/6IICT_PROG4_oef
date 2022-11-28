import json
fp = open("C:/Users/SWPI190304/Desktop/programmeren/prog4/6IICT_PROG4_oef/hfst_2/oefen_mee/oefen_mee13.json", "r")
lijst = json.load(fp)
fp.close()

print(lijst)

for index, dag in enumerate(lijst):
    if index == 0:
        print(f"{dag['Date']} zijn er 0 nieuwe cases.")
    else:
        verschil = dag["Cases"] - aantal_vorige_dag
        print(verschil)
    aantal_vorige_dag = dag["Cases"]

