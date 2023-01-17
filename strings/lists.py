apparel = ["shoes","shirt"]
apparel.append("tie")
extra = ["sunnies", "pants"]
apparel.extend(extra)
print(apparel[:2])
print(apparel[-1])
srt = "running, cycling, swimming"
sports_list = srt.split(",")
print(sports_list)
print(len(sports_list))
sports_length = []
for i in sports_list:
    sports_length.append(len(i))
print(sports_length)