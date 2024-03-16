import random

class Turnir:
    def __init__(self, naziv_turnira, lista_igraca, broj_rundi):
        self.naziv_turnira = naziv_turnira
        self.lista_igraca = lista_igraca
        self.broj_rundi = broj_rundi

    def get_naziv_turnira(self):
        return self.naziv_turnira

    def set_naziv_turnira(self, naziv_turnira):
        self.naziv_turnira = naziv_turnira

    def get_lista_igraca(self):
        return self.lista_igraca

    def set_lista_igraca(self, lista_igraca):
        self.lista_igraca = lista_igraca

    def get_broj_rundi(self):
        return self.broj_rundi

    def set_broj_rundi(self, broj_rundi):
        if 0 < broj_rundi < 10:
            self.broj_rundi = broj_rundi

    def dodaj_igraca(self, ime_igraca):
        self.lista_igraca.append((ime_igraca, 0))

    def obrisi_igraca(self, ime_igraca):
        for igrac in self.lista_igraca:
            if igrac[0] == ime_igraca:
                self.lista_igraca.remove(igrac)
                break

    def prikazi_najboljeg_igraca(self):
        if not self.lista_igraca:
            print("Nema igrača u turniru.")
            return

        najbolji_igrac = max(self.lista_igraca, key=lambda x: x[1])
        print("Najbolji igrač:", najbolji_igrac[0], "sa", najbolji_igrac[1], "bodova.")

    def pokreni_rundu(self):
        if len(self.lista_igraca) < 2:
            print("Nedovoljno igrača za rundu.")
            return

        igrac1, igrac2 = random.sample(self.lista_igraca, 2)
        rezultat = random.random()

        if rezultat <= 0.6:
            igrac1_index = self.lista_igraca.index(igrac1)
            self.lista_igraca[igrac1_index] = (igrac1[0], igrac1[1] + 1)
            print("Pobjednik runde:", igrac1[0])
            print("Par igrača u rundi:", igrac1[0], "-", igrac2[0])
        else:
            igrac2_index = self.lista_igraca.index(igrac2)
            self.lista_igraca[igrac2_index] = (igrac2[0], igrac2[1] + 1)
            print("Pobjednik runde:", igrac2[0])
            print("Par igrača u rundi:", igrac1[0], "-", igrac2[0])

        self.broj_rundi += 1

turnir = Turnir("Teniski turnir", [], 0)

turnir.dodaj_igraca("Novak Djokovic")
turnir.dodaj_igraca("Rafael Nadal")
turnir.dodaj_igraca("Roger Federer")

turnir.prikazi_najboljeg_igraca()

turnir.pokreni_rundu()
turnir.pokreni_rundu()

turnir.prikazi_najboljeg_igraca()
