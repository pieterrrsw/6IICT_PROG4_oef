import requests

antwoord = requests.get("https://api.covid19api.com/world/total").text
print(antwoord)
