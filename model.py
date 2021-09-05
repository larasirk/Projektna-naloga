import json
import datetime
import os


class Model:
    def __init__(self, pot_do_datoteke):
        self.pot_do_datoteke = pot_do_datoteke
        self.trgatve = dict()
        self.sorte = dict()

    def preberi_iz_datoteke(self):
        if os.path.isfile(self.pot_do_datoteke):  # preveri, ali je veljavna datoteka
            with open(self.pot_do_datoteke) as f:
                slovar = json.load(f)  # pobere podatke iz jsona
                # pod trgatve tiste, ki so pod ključem trgatve
                trgatve = slovar["trgatve"]
                sorte = slovar["sorte"]

                self.sorte = {int(sorta["st_sorte"]): Sorta(  # beremo podatke, da naredimo objekt
                    st_sorte=sorta['st_sorte'],
                    ime=sorta['ime'],
                    kislina_cuvee=sorta['kislina_cuvee'],
                    encimi_cuvee=sorta['encimi_cuvee'],
                    cistilo_cuvee=sorta['cistilo_cuvee'],
                    cistilo_ime_cuvee=sorta['cistilo_ime_cuvee'],
                    kislina_taille=sorta['kislina_taille'],
                    encimi_taille=sorta['encimi_taille'],
                    cistilo_taille=sorta['cistilo_taille'],
                    cistilo_ime_taille=sorta['cistilo_ime_taille'],
                    carbon_taille=sorta['carbon_taille']
                ) for sorta in sorte}
                self.trgatve = {
                    int(trgatev["st_trgatve"]): Trgatev(
                        kolicina=trgatev["kolicina"],
                        sorta=self.sorte[int(trgatev["st_sorte"])],
                        datum=trgatev["datum"],
                        st_trgatve=trgatev["st_trgatve"],
                    )
                    for trgatev in trgatve
                }
        else:
            self.shrani_v_datoteko()

    # funkcija, ki zdruzi sorte in trgatve in zapise v podatki.json
    def shrani_v_datoteko(self):
        with open(self.pot_do_datoteke, "w", encoding="UTF-8") as f:
            slovar = {
                # trgatev.v_slovar...da formatira v obliko, ki jo sprejme json
                "trgatve": [trgatev.v_slovar() for trgatev in self.trgatve.values()],
                "sorte": [sorta.v_slovar() for sorta in self.sorte.values()],
            }
            json.dump(slovar, f)  # slovar zapiše v f

    def dodaj_trgatev(self, trgatev):
        st_trgatev = self.trgatve.keys()  # pod st_strgatve shranis tabelo kljucev
        if len(st_trgatev) == 0:  # to določi id cel if
            trgatev.st_trgatve = 0
        else:
            trgatev.st_trgatve = max(st_trgatev) + 1
        # trgatve je tabela vseh tistih kart, vsaka karta je trgatev
        # objekt tanove trgatve da na id v tabeli objekt
        self.trgatve[trgatev.st_trgatve] = trgatev
        self.shrani_v_datoteko()

    def posodobi_trgatev(self, st_trgatve, kolicina, st_sorte, datum):
        self.trgatve[int(st_trgatve)].kolicina = int(kolicina)
        self.trgatve[int(st_trgatve)].sorta = self.sorte[int(st_sorte)]
        self.trgatve[int(st_trgatve)].nastavi_datum(datum)
        self.trgatve[int(st_trgatve)].izracunaj()

        self.shrani_v_datoteko()

    def izbrisi_trgatev(self, st_trgatve):
        del self.trgatve[st_trgatve]
        self.shrani_v_datoteko()

    def dodaj_sorto(self, sorta):
        st_sort = self.sorte.keys()
        if len(st_sort) == 0:
            sorta.st_sorte = 0
        else:
            sorta.st_sorte = max(st_sort) + 1

        self.sorte[sorta.st_sorte] = sorta
        self.shrani_v_datoteko()


class Trgatev:
    def __init__(self, kolicina, sorta, datum, st_trgatve=-1):
        self.st_trgatve = int(st_trgatve)
        self.kolicina = int(kolicina)
        self.sorta = sorta
        self.nastavi_datum(datum)
        self.izracunaj()

    def izracunaj(self):
        self.izracun_sok()
        self.izracun_taille_quvee()
        self.izracun_kislina()
        self.izracun_encimi()
        self.izracun_cistilo()
        self.izracun_carbon()

    def izracun_sok(self):
        self.sok = self.kolicina * 0.65

    def izracun_taille_quvee(self):
        self.taille = self.sok * 0.2
        self.cuvee = self.sok * 0.8

    def izracun_kislina(self):
        self.kislina_cuvee = (self.cuvee / 100) * self.sorta.kislina_cuvee
        self.kislina_taille = (self.taille / 100) * self.sorta.kislina_taille

    def izracun_encimi(self):
        self.encimi_cuvee = (self.cuvee / 100) * self.sorta.encimi_cuvee
        self.encimi_taille = (self.taille / 100) * self.sorta.encimi_taille

    def izracun_cistilo(self):
        self.cistilo_cuvee = (self.cuvee / 100) * self.sorta.cistilo_cuvee
        self.cistilo_taille = (self.taille / 100) * self.sorta.cistilo_taille

    def izracun_carbon(self):
        self.carbon_taille = (self.taille / 100) * self.sorta.carbon_taille

    def nastavi_datum(self, datum):
        datum = datum.split("-")
        self.datum = datetime.date(
            year=int(datum[0]), month=int(datum[1]), day=int(datum[2]))

    def v_slovar(self):
        return {
            "st_trgatve": self.st_trgatve,
            "kolicina": self.kolicina,
            "st_sorte": self.sorta.st_sorte,
            "datum": self.datum.strftime("%Y-%m-%d"),
        }


class Sorta:
    def __init__(
        self,
        ime,
        kislina_cuvee,
        encimi_cuvee,
        cistilo_cuvee,
        cistilo_ime_cuvee,
        kislina_taille,
        encimi_taille,
        cistilo_taille,
        cistilo_ime_taille,
        carbon_taille,
        st_sorte=-1,
    ):
        self.st_sorte = int(st_sorte)
        self.ime = ime
        self.kislina_cuvee = float(kislina_cuvee)
        self.encimi_cuvee = float(encimi_cuvee)
        self.cistilo_cuvee = float(cistilo_cuvee)
        self.cistilo_ime_cuvee = cistilo_ime_cuvee
        self.kislina_taille = float(kislina_taille)
        self.encimi_taille = float(encimi_taille)
        self.cistilo_taille = float(cistilo_taille)
        self.cistilo_ime_taille = cistilo_ime_taille
        self.carbon_taille = float(carbon_taille)

    def v_slovar(self):  # shranjuje podatke v obliko, ki jo zahteva json
        return {
            "st_sorte": self.st_sorte,
            "ime": self.ime,
            "kislina_cuvee": self.kislina_cuvee,
            "encimi_cuvee": self.encimi_cuvee,
            "cistilo_cuvee": self.cistilo_cuvee,
            "cistilo_ime_cuvee": self.cistilo_ime_cuvee,
            "kislina_taille": self.kislina_taille,
            "encimi_taille": self.encimi_taille,
            "cistilo_taille": self.cistilo_taille,
            "cistilo_ime_taille": self.cistilo_ime_taille,
            "carbon_taille": self.carbon_taille,
        }
