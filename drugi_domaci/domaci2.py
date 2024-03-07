# Zadatak 1: Provjera da li je broj paran
def provjeri_paran_broj(broj):
    # if broj % 2 == 0:
    #     print("Portal se otvara!")
    # else:
    #     print("Portal ostaje zatvoren.")
    print("Portal se otvara!" if broj % 2 == 0 else "Portal ostaje zatvoren")

# Zadatak 2: Provjera ko je ubrao više jabuka
def pobjednik_u_berbi_jabuka(p, m):
        print("Pobjednik je Petar!" if p > m else "Pobjednik je Miloš!")

# Zadatak 3: Provjera uslova za pristup ispitu
def provjeri_pristup_ispitu(prisustvo, seminarski):
    print("Student može pristupiti ispitu." if prisustvo > 75 and seminarski == 1 else "Student ne može pristupiti ispitu.")

# Zadatak 4: Provjera dozvole za bučne radove
def provjeri_bucne_radove(sati):
    if 6 <= sati < 13 or 17 <= sati <= 22:
        print("Možete izvoditi bučne radove.")
    else:
        print("Ne možete izvoditi bučne radove.")

# Zadatak 5: Provjera mogućnosti pravljenja bašte u obliku trougla
def provjeri_bastu(a, b, c):
    if a + b > c and a + c > b and b + c > a:
        print("Bašta u obliku trougla se može napraviti.")
    else:
        print("Bašta u obliku trougla se ne može napraviti.")

# Zadatak 6: Provjera kretanja pčele po žici
def provjeri_kretanje_pcele(x, y):
    if y == 2 * x + 5:
        print("Pčela se kreće po žici.")
    else:
        print("Pčela ne ide po žici.")

# Zadatak 7: Određivanje pobjednika takmičenja
def odredi_pobjednika(matematika, programiranje):
    if matematika > programiranje:
        print("Pobjednik je matematika.")
    elif programiranje > matematika:
        print("Pobjednik je programiranje.")
    else:
        print("Nema pobednika, izjednačeno je.")

# Zadatak 8: Određivanje uspjeha učenika
def odredi_uspjeh(prosjek):
    if prosjek >= 4.5:
        print("Odličan uspjeh.")
    elif 3.5 <= prosjek < 4.5:
        print("Vrlo dobar uspjeh.")
    elif 2.5 <= prosjek < 3.5:
        print("Dobar uspjeh.")
    elif 2 <= prosjek < 2.5:
        print("Dovoljan uspjeh.")
    else:
        print("Nedovoljan uspjeh.")

# Zadatak 9: Provjera prekrivanja zavjese i prozora
def provjeri_prekrivanje(zavjesa, prozor):
    if zavjesa[0] <= prozor[0] and zavjesa[1] >= prozor[1] and zavjesa[2] >= prozor[2] and zavjesa[3] <= prozor[3]:
        print("Zavjesa prekriva prozor.")
    else:
        print("Zavjesa ne prekriva prozor.")

# Zadatak 10: Provjera pogotka strelice u pikado tabli
def provjeri_pogodak(tabla, strelica):
    udaljenost = ((tabla[0] - strelica[0])**2 + (tabla[1] - strelica[1])**2)**0.5
    if udaljenost <= tabla[2]:
        print("Strelica je pogodila pikado tablu.")
    else:
        print("Strelica nije pogodila pikado tablu.")

# Zadatak 11: Provjera da li se mrav kreće po ivici stola
def provjeri_kretanje_mrava(mrav, ivica_stola):
    if ivica_stola[0][0] <= mrav[0] <= ivica_stola[1][0] and ivica_stola[0][1] >= mrav[1] >= ivica_stola[1][1]:
        print("Mrav se kreće po ivici stola.")
    else:
        print("Mrav se ne kreće po ivici stola.")

# Zadatak 12: Obrada dvocifrenog broja
def obradi_dvocifreni_broj(broj):
    prva_cifra = broj // 10
    druga_cifra = broj % 10
    if prva_cifra > druga_cifra:
        print("Razlika prve i druge cifre je:", prva_cifra - druga_cifra)
    elif prva_cifra < druga_cifra:
        print("Zbir prve i druge cifre je:", prva_cifra + druga_cifra)
    else:
        print("Proizvod prve i druge cifre je:", prva_cifra * druga_cifra)

# Zadatak 13: Izračun obima stola sa većom površinom
def izracunaj_obim_stola(r1, r2):
    obim1 = 2 * 3.14 * r1
    obim2 = 2 * 3.14 * r2
    if obim1 > obim2:
        print("Obim stola 1 je veći:", obim1)
    elif obim2 > obim1:
        print("Obim stola 2 je veći:", obim2)
    else:
        print("Obimi su jednaki:", obim1)

# Zadatak 14: Pronalaženje najmanje vrijednosti zbira parova proizvoda
def najmanja_vrijednost_zbira_cijena(cijene):
    min_zbir = float('inf')
    par = ()
    
    for i in range(len(cijene)):
        for j in range(i+1, len(cijene)):
            zbir = cijene[i] + cijene[j]
            if zbir < min_zbir:
                min_zbir = zbir
                par = (cijene[i], cijene[j])
    
    return par

# Zadatak 15: Provjera da li je godina prestupna
def provjeri_prestupnu_godinu(godina):
    if (godina % 4 == 0 and godina % 100 != 0) or (godina % 400 == 0):
        return True
    else:
        return False

# Zadatak 16: Provjera da li se tačka nalazi unutar pravougaonika
def provjeri_tačku_u_pravougaoniku(tačka, pravougaonik):
    if (pravougaonik[0][0] < tačka[0] < pravougaonik[1][0]) and (pravougaonik[1][1] < tačka[1] < pravougaonik[0][1]):
        print("Tačka se nalazi unutar pravougaonika.")
    else:
        print("Tačka se ne nalazi unutar pravougaonika.")

# Zadatak 17: Provjera mogućnosti pravljenja dva kvadrata iz pravougaonika
def provjeri_kvadrate_iz_pravougaonika(a, b):
    if a == b:
        print("Mogu se napraviti dva kvadrata.")
    elif a % 2 == 0 and b % 2 == 0:
        print("Mogu se napraviti dva kvadrata.")
    else:
        print("Ne mogu se napraviti dva kvadrata.")

# Zadatak 18: Određivanje agregatnog stanja vode na osnovu temperature
def odredi_agregatno_stanje_vode(temperatura):
    if temperatura > 0 and temperatura < 100:
        print("Agregatno stanje je tečno.")
    elif temperatura <= 0:
        print("Agregatno stanje je čvrsto.")
    else:
        print("Agregatno stanje je gasovito.")

# Zadatak 19: Određivanje iznosa popusta za upis u školu
def iznos_popusta(iznos_skolarine, prosjek, nagrada):
    if prosjek >= 4.5:
        popust = 0.4
    elif 3.5 <= prosjek < 4.5:
        popust = 0.2
    elif 2.5 <= prosjek < 3.5:
        popust = 0.1
    else:
        popust = 0
    
    if nagrada == 1:
        popust = max(popust, 0.3)
    
    iznos_placanja = iznos_skolarine * (1 - popust)
    return round(iznos_placanja)

# Zadatak 20: Računanje zbira parnih cifara ili proizvoda neparnih cifara četvorocifrenog broja
def izracunaj_zbir_ili_proizvod(broj):
    if broj < 1000 or broj > 9999:
        return "Broj nije četvorocifren."

    zbir = 0
    proizvod = 1
    for cifra in str(broj):
        cifra = int(cifra)
        if cifra % 2 == 0:
            zbir += cifra
        else:
            proizvod *= cifra
    
    if broj % 2 == 0:
        return zbir
    else:
        return proizvod

# Zadatak 24: Skraćivanje teksta na tačno 30 karaktera
def skrati_tekst(tekst):
    if len(tekst) > 30:
        skraceni_tekst = tekst[:30] + "..."
        print(len(skraceni_tekst))
        return skraceni_tekst
    else:
        return tekst

# Zadatak 25: Uklanjanje prvog i poslednjeg karaktera teksta
def ukloni_prvi_i_poslednji_karakter(tekst):
    return tekst[1:-1]

# Zadatak 26: Provjera formata unesenog broja
def provjeri_format_broja(broj):
    if broj.startswith("0b"):
        return "Binarni broj"
    elif broj.startswith("0o"):
        return "Oktalni broj"
    elif broj.startswith("0x"):
        return "Heksadecimalni broj"
    else:
        return "Dekadni broj"

# Zadatak 27: Provjera da li string sadrži barem jedan samoglasnik
def sadrzi_samoglasnik(tekst):
    samoglasnici = "aeiouAEIOU"
    for slovo in tekst:
        if slovo in samoglasnici:
            return True
    return False

# Zadatak 28: Provjera da li se string završava sa target stringom
def provjeri_zavrsetak(tekst, target):
    if tekst.endswith(target):
        return "Da"
    else:
        return "Ne"

# Zadatak 29: Provjera da li je uneseni string binarni broj
def provjeri_binarni_broj(tekst):
    if all(bit == '0' or bit == '1' for bit in tekst):
        return True
    else:
        return False

# Zadatak 30: Računanje zbira parnih i proizvod neparnih brojeva od 1 do n
def izracunaj_zbir_i_proizvod(n):
    zbir = 0
    proizvod = 1
    for i in range(1, n+1):
        if i % 2 == 0:
            zbir += i
        else:
            proizvod *= i

    print("Zbir parnih brojeva:", zbir)
    print("Proizvod neparnih brojeva:", proizvod)

# Zadatak 31: Kvadriranje elemenata segmenta i njihova suma
def kvadriraj_i_sumiraj(start, end):
    suma = 0
    for broj in range(start, end):
        if broj % 2 == 0 and broj % 4 != 0:
            suma += broj ** 2
    return suma

# Zadatak 32: Suma i broj elemenata djeljivih sa djeliocem u segmentu (a, b)
def suma_i_broj_djeljivih(a, b, djelilac):
    suma = 0
    broj_djeljivih = 0
    for broj in range(a+1, b):
        if broj % djelilac == 0:
            suma += broj
            broj_djeljivih += 1
    return suma, broj_djeljivih

# Zadatak 33: Sabiranje svih cifara unesenog broja
def saberi_cifre(broj):
    return sum(int(cifra) for cifra in str(broj))

# Zadatak 34: Računanje proizvoda cifara iz teksta
def proizvod_cifara_iz_teksta(tekst):
    # cifre = [int(cifra) for cifra in tekst if cifra.isdigit()]
    proizvod = 1
    # for cifra in cifre:
    #     proizvod *= cifra
    for cifra in tekst:
        if cifra.isdigit():
            proizvod *= int(cifra) 
    return proizvod

# Zadatak 35: Broj cifara u stringu i kreiranje integera od njih
def broj_cifara_i_kreiranje_integera(tekst):
    broj_cifara = ''.join(cifra for cifra in tekst if cifra.isdigit())
    return int(broj_cifara), len(broj_cifara)

# Zadatak 36: Enkripcija stringa prema specifikaciji
def enkriptuj_string(s):
    enkriptovan_string = ""
    samoglasnici = "aeiouAEIOU"
    for karakter in s:
        if karakter in samoglasnici:
            enkriptovan_string += "1"
        else:
            enkriptovan_string += "0"
    return enkriptovan_string

# Zadatak 37: Provjera da li je igrač u plusu
def provjeri_poenove(lista):
    poeni = sum(1 if x == '1' else (-1 if x == '*' else 0) for x in lista)
    return poeni > 0

# Zadatak 38: Enkripcija stringa sa ciframa prema specifikaciji
def enkriptuj_string_cifre(s):
    enkriptovan_string = ""
    for karakter in s:
        if int(karakter) % 2 == 0:
            enkriptovan_string += "0"
        else:
            enkriptovan_string += "1"
    return enkriptovan_string

# Zadatak 39: Provjera da li je broj Narcissistic
def narcissistic_number(broj):
    broj_cifara = len(str(broj))
    suma = sum(int(cifra) ** broj_cifara for cifra in str(broj))
    return suma == broj

# Zadatak 40: Apsolutna suma negativnih parnih elemenata niza
def apsolutna_suma_negativnih_parnih(niz):
    return sum(abs(broj) for broj in niz if broj < 0 and broj % 2 == 0)

# Zadatak 41: Broj elemenata manjih od max u listi
def broj_elemenata_manjih_od_max(lista, max_vrijednost):
    return sum(1 for broj in lista if broj < max_vrijednost)

# Zadatak 42: Razlika u zaradi nakon sniženja cijena proizvoda
def razlika_u_zaradi(cijene):
    originalna_zarada = sum(cijena for cijena in cijene)
    nova_zarada = sum(cijena * 0.9 for cijena in cijene)
    return originalna_zarada - nova_zarada

# Zadatak 43: Prebrojavanje učenika sa ocjenama 1 i 2
def broj_ocjena_1_2(ocjene):
    return sum(1 for ocjena in ocjene if ocjena == 1 or ocjena == 2)

# Zadatak 44: Najveći broj posjeta na jednom danu
def najveci_broj_posjeta(posjete):
    return max(posjete)

# Zadatak 45: Broj zaposlenih sa većim platama od prosjeka
def broj_zaposlenih_sa_vecim_platama(plate):
    prosjek = sum(plate) / len(plate)
    return sum(1 for plata in plate if plata > prosjek)

# Zadatak 66: Provjera da li ima više dvocifrenih ili trocifrenih brojeva u listi
def vise_dvocifrenih_ili_trocifrenih(lista):
    brojac_dvocifrenih = 0
    brojac_trocifrenih = 0
    for broj in lista:
        if 10 <= broj <= 99:
            brojac_dvocifrenih += 1
        elif 100 <= broj <= 999:
            brojac_trocifrenih += 1
    if brojac_dvocifrenih > brojac_trocifrenih:
        return "Više dvocifrenih brojeva."
    elif brojac_dvocifrenih < brojac_trocifrenih:
        return "Više trocifrenih brojeva."
    else:
        return "Ista količina dvocifrenih i trocifrenih brojeva."

# Zadatak 67: Broj ponavljanja određenog broja u listi
def broj_ponavljanja(lista, broj):
    return lista.count(broj)

# Zadatak 68: Uvećavanje zarade većih od prosjeka za X eura
def uvecanje_zarade(plate, X):
    prosjek = sum(plate) / len(plate)
    return [zarada + X if zarada > prosjek else zarada for zarada in plate]

# Zadatak 69: Manipulacija zaradama prema specifikaciji
def manipulacija_zaradama(plate):
    prosjek = sum(plate) / len(plate)
    nova_lista = []
    for zarada in plate:
        if zarada > prosjek:
            nova_lista.append(zarada * 0.9)  # Smanjuje zaradu za 10%
        else:
            nova_lista.append(zarada * 1.1)  # Uvećava zaradu za 10%
    iznad_prosjeka = sum(1 for zarada in nova_lista if zarada > prosjek)
    return nova_lista, iznad_prosjeka

# Zadatak 70: Zbir kvadrata elemenata djeljivih sa 3
def zbir_kvadrata_djeljivih_sa_3(lista):
    return sum(x ** 2 for x in lista if x % 3 == 0)

# Zadatak 71: Broj brojeva čiji je kvadratni korijen cijeli broj
def broj_cijelih_kvadratnih_korijena(lista):
    brojac = 0
    for broj in lista:
        if (broj ** 0.5).is_integer():
            brojac += 1
    return brojac

# Zadatak 72: Broj studenata sa ocjenama iznad prosjeka
def broj_ocjena_iznad_prosjeka(ocene):
    ocjene_bez_petice = [ocjena for ocjena in ocene if ocjena < 5]
    prosjek = sum(ocjene_bez_petice) / len(ocjene_bez_petice)
    return sum(1 for ocjena in ocjene_bez_petice if ocjena > prosjek)

# Zadatak 73: Simulacija inventara igrača u RPG igri
def simulacija_inventara(inventar, pozicija):
    if pozicija >= 0 and pozicija < len(inventar):
        return inventar[pozicija]
    else:
        return "Pozicija izvan opsega inventara."

# Zadatak 74: Računanje prosječne vrijednosti plata u dolarima
def prosjecna_vrijednost_plata_u_dolarima(plate):
    return sum(plate) * 1.1 / len(plate)

# Zadatak 75: Računanje ukupnog gubitka banke od kamate na štednju
def gubitak_banke_od_kamate(novac, kamata):
    ukupan_gubitak = sum(novac) * kamata
    return ukupan_gubitak

# Zadatak 76: Zamjena određenog elementa u listi drugim elementom
def zamjena_elementa(lista, stari, novi):
    return [novi if x == stari else x for x in lista]

# Zadatak 77: Provjera da li je lista sortirana u rastućem poretku
def provjera_sortiranja(lista):
    return lista == sorted(lista)

# Zadatak 78: Pronalaženje vrijednosti drugog najskupljeg proizvoda
def drugi_najskuplji_proizvod(cijene):
    cijene.sort()
    return cijene[-2]

# Zadatak 79: Broj elemenata koji imaju suprotnu vrijednost u listi
def broj_elemenata_sa_suprotnom_vrijednoscu(lista):
    suprotni = set(-x for x in lista)
    return sum(1 for broj in lista if broj in suprotni)

# Zadatak 80: Razlika između najdužeg i najkraćeg skoka
def razlika_najduzeg_i_najkraceg_skoka(skokovi):
    return max(skokovi) - min(skokovi)

# Zadatak 81: Najveći pad i najveći porast cijena za susjedne vrijednosti
def analiza_promjene_cijena(cijene):
    najveci_pad = min(cijene[i] - cijene[i + 1] for i in range(len(cijene) - 1))
    najveci_porast = max(cijene[i + 1] - cijene[i] for i in range(len(cijene) - 1))
    return najveci_pad, najveci_porast

# Zadatak 82: Pronalazak najboljeg reda za grupu osoba
def najbolji_red_za_grupu(sjedista, n):
    najbolji_red = max(range(len(sjedista)), key=lambda x: sjedista[x] - n if sjedista[x] >= n else float('-inf'))
    return najbolji_red

# Zadatak 91: Pronalaženje drugog najvećeg elementa u listi
def second_max(a):
    a.remove(max(a))
    return max(a)

# Zadatak 92: Unos proizvoda i pretraga proizvoda po nazivu
def unos_proizvoda(n):
    proizvodi = []
    for _ in range(n):
        naziv = input("Unesite naziv proizvoda: ")
        opis = input("Unesite opis proizvoda: ")
        cijena = float(input("Unesite cijenu proizvoda: "))
        broj_artikala = int(input("Unesite broj dostupnih artikala: "))
        proizvod = {"naziv": naziv, "opis": opis, "cijena": cijena, "broj_artikala": broj_artikala}
        proizvodi.append(proizvod)
    return proizvodi

def pretraga_po_nazivu(proizvodi, search_term):
    return [proizvod for proizvod in proizvodi if proizvod["naziv"].startswith(search_term)]

# Zadatak 93: Filtriranje igrica prema ocjeni i izdavaču
def filtriranje_igrica(igre, ocjena, izdavac):
    return [igra for igra in igre if igra["ocjena"] > ocjena and igra["izdavac"] == izdavac]

# Zadatak 94: Pronalaženje riječi sa parnim brojem slova bez zadatog slova
def get_ewfbyr(tekst, slovo):
    rijeci = tekst.split()
    return [rijec for rijec in rijeci if len(rijec) % 2 == 0 and slovo not in rijec]

# Zadatak 95: Najduža neopadajuća podlista pozitivnih cijelih brojeva
def longest_increasing(input_list):
    najduza_podlista = []
    trenutna_podlista = []
    for broj in input_list:
        if broj > 0:
            trenutna_podlista.append(broj)
        else:
            if len(trenutna_podlista) > len(najduza_podlista):
                najduza_podlista = trenutna_podlista
            trenutna_podlista = []
    if len(trenutna_podlista) > len(najduza_podlista):
        najduza_podlista = trenutna_podlista
    return najduza_podlista

# Zadatak 96: Razbijanje stringa na podstringove zadate dužine
def split_string(s, number):
    result = [s[i:i+number].ljust(number, "*") for i in range(0, len(s), number)]
    return result

# Zadatak 97: Kupovina proizvoda s ograničenim raspoloživim novcem
def koliko_proizvoda_mogu_kupiti(proizvodi, naziv, raspolozivi_novac):
    for proizvod in proizvodi:
        if proizvod["naziv"] == naziv:
            return min(proizvod["broj_artikala"], raspolozivi_novac // proizvod["cijena"])
    return 0

# Zadatak 98: Računanje ukupne kupovine i prodaje akcija
def ukupna_kupovina_prodaja(zahtjevi):
    kupovina = 0
    prodaja = 0
    for zahtjev in zahtjevi.split(","):
        _, kolicina, cijena, status = zahtjev.strip().split()
        kolicina = int(kolicina)
        cijena = float(cijena)
        if status == "B":
            kupovina += kolicina * cijena
        elif status == "S":
            prodaja += kolicina * cijena
    return f"Buy: {kupovina:.2f} Sell: {prodaja:.2f}"

# Zadatak 99: Razbijanje stringa na podstringove zadate dužine (izmjena)
def split_string(s, number):
    return [s[i:i+number] for i in range(0, len(s), number)]

# Zadatak 100: Validacija lozinke
def check_password(input_string, min_string_len, flagUpper=False, flagLower=False, flagDigit=False):
    if len(input_string) < min_string_len:
        return False
    if flagUpper and not any(c.isupper() for c in input_string):
        return False
    if flagLower and not any(c.islower() for c in input_string):
        return False
    if flagDigit and not any(c.isdigit() for c in input_string):
        return False
    return True