""" 
Voorbeeld:

>>> input() = "Dit is een zin"
>>> Dict    = {"Dit": "tiD", "is": "si", "een": "nee", "zin": "niz"}

Tip: je hebt al in de reeksen gezien hoe een woord om te keren.
"""
omgekeerd_dict = {}
zin = input("Geef een zin op: ")
woorden = zin.split()
for woord in woorden:
    omgekeerd_dict[woord] = woord[::-1]
print(omgekeerd_dict)
