import urllib.request as reader
import re

page = reader.urlopen("https://melee.gg/Decklist/View/309545")

temp = ""
for i in page:
    temp += str(i)

#print(temp)
print(type(temp))
cards = re.findall("/b'\d ([^\\r]*)\\r/g", temp)

print(cards)
for i in cards:
    print(i)