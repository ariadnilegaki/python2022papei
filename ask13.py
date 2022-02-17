from urllib.request import Request, urlopen
import json


req = Request('https://drand.cloudflare.com/public/latest', headers={'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:31.0) Gecko/20130401 Firefox/31.0'})
data = urlopen(req).read()

print(data)
x= json.loads(data)
print(x)

tel_round = x["round"]

for round in range(tel_round, tel_round-100, -1):
    req= Request('https://drand.cloudflare.com/public/latest', headers={'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:31.0) Gecko/20130401 Firefox/31.0'})
    data= urlopen(req).read()
    x=json.loads(data)
    randomness= x["randomness"]

#σπάω ανά 2

split_randomness = []
n  = 2
for index in range(0, len(randomness), n):
    split_randomness.append(randomness[index : index + n])

print("Splited randomness by 2=", split_randomness)


#μετατρέπω σε ακεραίους

for i in range(0, len(split_randomness)):
    split_randomness[i] = int(split_randomness[i],16)

print("Int randomness=", split_randomness)

#modulo 80

for i in range(0, len(split_randomness)):
    split_randomness[i] = split_randomness[i] % 80

print ("Modulo 80=", split_randomness)

#κρατάω το καθένα μια φορά
split_randomness = list(set(split_randomness))
print("Final randomness=", split_randomness)

#ελεγχος με kino


req= Request('https://api.opap.gr/draws/v3.0/1100/last-result-and-active')
data= urlopen(req).read()
kino = json.loads(data)

knumbers=[]
kino2 = kino['last']["winningNumbers"]['list']
for i in kino2:
    knumbers.append(i)

print("Kino numbers are:", knumbers)

for i in range(0, len(split_randomness)):
    for j in range(0, len(knumbers)):
        if split_randomness[i] == knumbers[j]:
            print("Same number found:", split_randomness[i])

print("Telos")


