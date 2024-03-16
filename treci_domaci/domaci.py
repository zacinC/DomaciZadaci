import math

def zad1(s, c):
    br = 0
    lista = []
    rijeci = ()
    size = len(s)
    poc = 0

    for i in range(size):
        if i < size-1:
            if i==0 or s[i-1].isspace():
                poc = i
            if s[i]==c and s[i+1].isspace():
                br += 1
                rijeci += (s[poc:i+1],)
            elif s[i]==c and s[i+1] in '.!?':
                br += 1
                rijeci += (s[poc:i+1], br)
                lista.append(rijeci)
                rijeci = ()
                br = 0
            elif i==size-2 and s[i+1] in '.!?':
                rijeci += (br,)
                lista.append(rijeci)
                rijeci = ()
                br = 0
                
    return lista

#print(zad1('aj ti vidi!', 'j'))
#print(zad1('Print only the words that end with the chosen letter in those sentences? Example can contains one or more sentences!', 's'))

def zad2(lista):
    size = len(lista)
    poc = 0
    poc_max = 0
    kraj = 0
    el = lista[0]
    tmp = el
    proizvod = 1
    brojac = 1

    for i in range(1, size):
        if lista[i] == el:
            tmp *= el
            brojac += 1
        else:
            el = lista[i]
            if brojac > 1 and proizvod < tmp:
                proizvod = tmp
                poc_max = poc
                kraj = i
            tmp = el
            brojac = 1
            poc = i
        if i==size-1 and proizvod < tmp:
            proizvod = tmp
            poc_max = poc
            kraj = i+1
    
    return lista[poc_max:kraj], proizvod
            
#print(zad2([1,2,2,2,4,4]))

def zad3(niz):
    brojac = 0
    max_brojac = 0
    kraj = 0
    for i in range(len(niz)-1):
        if i%2==0:
            if niz[i] < niz[i+1]:
                brojac += 1
            else:
                max_brojac = brojac if max_brojac < brojac else max_brojac
                brojac = 0
                kraj = i+1
        else:
            if niz[i] > niz[i+1]:
                brojac += 1
            else:
                max_brojac = brojac if max_brojac < brojac else max_brojac
                brojac = 0
                kraj = i+1
    if max_brojac < brojac:
        kraj = len(niz)-1
        max_brojac = brojac
    return niz[kraj-max_brojac:kraj+1]

print(zad3([1,1,2,3,1,2,1,2]))

def zad4(s):
    br = 1
    maxbr = 1
    maxchar = s[0]
    size = len(s)

    for i in range(size):
            if i < size-1 and s[i] == s[i+1]:
                br += 1
            else:
                if maxbr < br:
                    maxbr = br
                    maxchar = s[i]
                br = 1

    return maxchar, maxbr

#print(zad4('aabaaabcccbcccc'))

def zad5(niz):
    odnos = 0
    najgori = math.inf
    naziv = ''
    for el in niz:
        odnos = el['br_pozitivni']/el['br_negativni']
        if odnos < najgori:
            najgori = odnos
            naziv = el['naziv']
    return naziv

# print(zad5([{'naziv':'Español para principiantes', 'br_pozitivni':1000,'br_negativni':10},
# {'naziv':'Philophize This!', 'br_pozitivni':500,'br_negativni': 30}, {'naziv':'Science VS.',
# 'br_pozitivni':600,'br_negativni': 45}]))