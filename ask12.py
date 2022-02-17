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

base_16 = int(randomness,16)
binary = bin(base_16)
print(binary)
    
new_list= list(binary)
print(new_list)

#μήκος της μεγαλύτερης ακολουθίας με συνεχόμενα μηδενικά και το μήκος της μεγαλύτερης ακολουθίας με συνεχόμενες μονάδες

plithos_0 = 0
plithos_1 = 0

for i in range(len(new_list)):
    if i == 0:
        max_0 = plithos_0
        max_1 = plithos_1
    if new_list[i] == '0':
        plithos_0 = plithos_0 +1
        plithos_1 = 0
        if plithos_0 > max_0:
            max_0 = plithos_0
    if new_list[i] == '1':
        plithos_0 =0
        plithos_1 = plithos_1+1
        if plithos_1 > max_1 :
            max_1 = plithos_1


print ("Max number of 0 sequence:", max_0)
print ("Max number of 1 sequence:", max_1)