engels_nederlands = { "last":"laatste", "week":"week", "the":"de",
"royal":"koninklijk", "festival":"feest", "hall":"hal",
"saw":"zaag", "first":"eerst", "performance":"optreden",
"of":"van", "a":"een", "new":"nieuw", "symphony":"symfonie",
"by":"bij", "one":"een", "world":"wereld", "leading":
"leidend", "modern":"modern", "composer":"componist",
"composers":"componisten", "two":"twee", "shed":"schuur",
"sheds":"schuren" }

zin = input("Geef een zin in het engels: ")
nieuwe_zin = ""
woorden = zin.split() 

for woord in woorden:
    if woord in engels_nederlands:
        nieuwe_zin += f"{engels_nederlands[woord]}"
        nieuwe_zin += " "
print(nieuwe_zin)




