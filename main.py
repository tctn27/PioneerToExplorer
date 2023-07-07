import urllib.request as reader
import re

cardsCountDictionary = dict

page = reader.urlopen("https://melee.gg/Decklist/View/309545")

temp = ""
for i in page:
    temp += str(i)

print(temp)
#print(type(temp))
pattern = r"b'(\d) ([^\\r]*)\\r"
cards = re.findall(pattern, temp)

#print(cards)
for i in cards:
    print(i)