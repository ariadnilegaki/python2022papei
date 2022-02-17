f = open('text.txt')
data = str(f.read())
data = data.replace('.',' ')
data = data.replace('\n','')
data = data.replace(',',' ')
data = data.replace('#','')
data = data.replace('[','')
data = data.replace(']','')
data = data.replace('0','')
data = data.replace('1','')
data = data.replace('2','')
data = data.replace('3','')
data = data.replace('4','')
data = data.replace('5','')
data = data.replace('6','')
data = data.replace('7','')
data = data.replace('8','')
data = data.replace('9','')
data = data.replace('(','')
data = data.replace(')','')
data = data.replace('*','')
data = data.replace('-','')
data = data.replace('!',' ')
data = data.replace(';','')
data = data.replace('?','')
data = data.replace(',','')
data = data.replace(':','')
data = data.replace('"',' ')
data = data.replace('_',' ')
data = data.replace("'",' ')
data = data.lower()
#print(data)
words = data.split(" ")
words = list(filter(('').ne, words))          


print("10 Most popular words:")
lekseis = set(words)
lekseis = list(lekseis)
n=[]
for item in lekseis:
    s = 0
    for i in range (len(words)):
        if words[i]==item:
            s += 1
    n.append(s)
#print(lekseis)
#print(n)
#print(len(words))
#print(len(lekseis))
copy_n=n

maxl=[]
for i in range (len(copy_n)):
    maximum = max(copy_n)
    copy_n.remove(maximum) 
    maxl.append(maximum)                #finds the frequency of each individual word
copy_maxl=maxl
maxl = set(maxl)
maxl = list(maxl)                       #creates a set->list with all the frequencies
#print(maxl)
k = len(maxl)
#print(k)
if k<10:
    for item in reversed(maxl):
        flag=False
        i=0
        while i<len(lekseis) and flag==False:
            if len(lekseis[i])==item:
                print(lekseis[i])
                lekseis.pop(i)
                flag=True
            i+=1

    for item in reversed(maxl):
        flag=False
        i=0
        while i<len(lekseis) and flag==False:
            if len(lekseis[i])==item:
                k+=1
                print(lekseis[i])
                lekseis.pop(i)
                flag=True
                if k==10:
                    break
            i+=1 
        if k==10:
            break
else:
    j=0
    for item in reversed(maxl):
        j+=1
        flag=False
        i=0
        while i<len(lekseis) and flag==False:
            if len(lekseis[i])==item:
                print(lekseis[i])
                lekseis.pop(i)
                flag=True
            i+=1
        if j==10:
            break                               

print("3 Most popular 2 first letters:")
let_b=[]
i=0
for item in lekseis:
   let_b.append(item[:2])

let_b_Copy=let_b
let_b=set(let_b)
let_b=list(let_b)
let_b_F=[]
for item in let_b:
    s = 0
    for i in range (len(let_b_Copy)):
        if let_b_Copy[i]==item:
            s += 1
    let_b_F.append(s) 
for i in range (3):
    maxL2=max(let_b_F)
    pos = let_b_F.index(maxL2)
    print(let_b[pos])
    let_b.pop(pos)
    let_b_F.pop(pos)


print("3 Most popular 3 first letters:")
let_c=[]
i=0
for item in lekseis:
   let_c.append(item[:3])

let_c_Copy=let_c
let_c=set(let_c)
let_c=list(let_c)
let_c_F=[]
for item in let_c:
    s = 0
    for i in range (len(let_c_Copy)):
        if let_c_Copy[i]==item:
            s += 1
    let_c_F.append(s) 
for i in range (3):
    maxL3=max(let_c_F)
    pos = let_c_F.index(maxL3)
    print(let_c[pos])
    let_c.pop(pos)
    let_c_F.pop(pos)

