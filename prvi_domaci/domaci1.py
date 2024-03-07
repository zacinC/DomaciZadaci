import  math, datetime

def distance(a,b):
    return round(math.sqrt((a[0]-b[0])**2 + (a[1]-b[1])**2), 2)

#---------------------------------------------

def pravougaonik(a,b):
    return {"obim": 2*(a+b), "povrsina": a*b}

def kvadratna(a,b,c):
    return {"x1": -b + (b**2 - 4*a*c), "x2": -b - (b**2 - 4*a*c)}

def razlika_kvadrata(x,y):
    return x**2 - y**2

def sportista(d,s):
    return 8*(d+s)

def papir(a,b):
    return a*b/10

def trinom(a,b,c):
    return a**2 + b**2 + c**2 + 2*a*b + 2*a*c + 2*b*c

def biciklizam(h):
    return int(math.floor(h*0.5))

def stoljnjak(P):
    r_pi = math.sqrt(P)
    return round(2*r_pi,2)

def duzina_ograde(d, s, r):
    # pretpostavio sam da treba da bude udaljena za r od stranica a ne po dijagonali, tj. od tjemena 
    return 2 * (d + s + 4 * r)

def zid(a,b):
    gd = (a[0],b[1])
    dl = (b[0], a[1])
    d = a[0] - dl[0]
    s = gd[1] - a[1]

    return {"obim": 2*(d+s), "povrsina": d*s}

def godine(N):
    return datetime.date.today().year - N

def mapa(G,K):
    blago = (K[0]+2, K[1]-3)
    rastojanje = distance(G,K)
    Kk = K[0]+1, K[1]+1
    zaobidji = distance(G,Kk) + distance(Kk,blago)

    return (blago, rastojanje, zaobidji)

def heronov_obrazac(A,B,C):
    a = distance(A,B)
    b = distance(B,C)
    c = distance(A,C)
    s = (a + b + c) / 2
    area = math.sqrt(s * (s - a) * (s - b) * (s - c))
    return area

def euclide_distance(a,b):
    if type(a) and type(b) is tuple and len(a)==2 and len(b)==2:
        return round(math.sqrt((a[1]-a[0])**2 + (b[1]-b[0])**2), 2)
    else:
        return "Pogresan unos"

def taxi(k):
    return 1 + k*0.5

def bukvarnica(cijena, popust):
    return cijena - cijena*popust/100

def playstation(cijena):
    cijena += cijena*0.1
    cijena -= cijena*0.1
    return cijena

# Ovo je zadatak 19 ali sam prosirio da radi za bilo koji broj
def zbir_cifara(n):
    tmp = n%10
    while n//10:
        n //= 10
        tmp += n%10
    return tmp

def zad20(n):
    zbir = zbir_cifara(n)
    tmp = n%10
    while n//10:
        n //= 10
        tmp *= n%10
    return tmp - zbir

def sef(n):
    c4 = n%10
    n //= 10
    c3 = n%10
    n //= 10
    c2 = n%10
    n //= 10
    c1 = n%10

    return (c1 + c4)**2 - (c2**2 - c3**2)

def prosecan_broj_poena(N, K, p1, p2):
    return (p1 * N + p2 * K) / (N + K)

def srednja_vrijednost(a,b):
    return (a+b)/2

def zamjena(x,y):
    tmp = x
    x = y
    y = tmp
    return x,y

# x = 7
# y = 10
# x,y = zamjena(x,y)
# print(x,y)

def centimetri_u_metre(cm):
    return cm//100

def sprat(k):
    return (k//10)%10

def zad27(n):
    return zbir_cifara(n)**2

def zad28(n):
    c4 = n%10
    n //= 10
    c3 = n%10
    n //= 10
    c2 = n%10
    n //= 10
    c1 = n%10
    n = c4*1000
    n += c2*100
    n += c3*10
    n += c1
    return n

def zad29(a,b):
    if type(a) and type(b) is tuple and len(a)==2 and len(b)==2:
        c = ((a[0] + b[0])/2, (a[1] + b[1])/2)
    else:
        return "Pogresan unos"
    return {"tacka susreta": c, "rastojanje": distance(a,c)}


def zad30(a,b,r):
    return math.floor(a/r) * math.floor(b/r)

def zad31(d=50):
    x = math.sqrt((d**2)/337)
    y = 9*x / 16
    return x*y

def zad32(n):
    s = str(n)
    if int(s[0]) * int(s[2]) + 2 + int(s[5]) == int(s[1]) + int(s[3])*int(s[4]):
        return True
    else:
        return False

#zadatak 33 sam vec implementirao kao zadatak 30

def zad34(n):
    s = str(n)
    return (int(s[0]) + int(s[1]) + int(s[2]) + int(s[3]) + int(s[4]) + int(s[5]))**2 - int(s[2])*int(s[3])

def zad35(n):
    s = str(n)
    k = int(s[2])+int(s[4])
    return k


