import bottle
import os
from model import Model, Trgatev, Sorta

pot_do_datoteke = os.path.dirname(os.path.abspath(
    __file__))  # vsebuje pot do trenutne mape
# dodamo se mapo podatki.json
m = Model(os.path.join(pot_do_datoteke, "podatki.json"))
m.preberi_iz_datoteke()


@bottle.get('/static/<ime_dat:path>')
def server_static(ime_dat):
    return bottle.static_file(ime_dat, root='static/')


@bottle.get("/")
def index():
    # te sorte smo pobrali iz slovarja objekt Model, vse tri ki so na raspolago smo zapisali v sorte
    sorte = m.sorte.values()
    trgatve = m.trgatve.values()
    # na začetku je kolicina soka 0
    sok = {sorta.st_sorte: 0 for sorta in sorte}
    kolicina = {sorta.st_sorte: 0 for sorta in sorte}
    for trgatev in trgatve:
        # za vsako sorto prišteje količino soka
        sok[trgatev.sorta.st_sorte] += trgatev.sok
        kolicina[trgatev.sorta.st_sorte] += trgatev.kolicina
    return bottle.template(
        "zacetna.tpl", sorte=sorte, trgatve=trgatve, sok=sok, kolicina=kolicina
    )


@bottle.post("/dodaj_trgatev")
def dodaj_trgatev():

    # kolicino pobere s strani zacetna
    kolicina = int(bottle.request.forms.get("kolicina"))
    datum = bottle.request.forms.get("datum")
    st_sorte = int(bottle.request.forms.get('st_sorte'))
    # pobere vse podatke od te sorte, ne samo stevilke
    sorta = m.sorte[st_sorte]

    trgatev = Trgatev(kolicina, sorta, datum)  # ustvarimo nov objekt trgatev
    m.dodaj_trgatev(trgatev)

    return bottle.redirect('/')


@bottle.get("/trgatev/<st_trgatve:int>")
def trgatev(st_trgatve):
    sorte = m.sorte.values()
    trgatev = m.trgatve[st_trgatve]  # izbere tisto trgatev, ki jo ti izberes

    # poveze podatke
    return bottle.template("trgatev.tpl", trgatev=trgatev, sorte=sorte)


@bottle.get("/izbrisi_trgatev/<st_trgatve:int>")
def izbrisi_trgatev(st_trgatve):
    m.izbrisi_trgatev(st_trgatve)
    return bottle.redirect('/')


@bottle.post("/posodobi_trgatev")
def posodobi_trgatev():
    kolicina = bottle.request.forms.get("kolicina")
    datum = bottle.request.forms.get("datum")
    st_trgatve = bottle.request.forms.get("st_trgatve")
    st_sorte = bottle.request.forms.get("st_sorte")
    m.posodobi_trgatev(st_trgatve, kolicina, st_sorte, datum)

    return bottle.redirect(f"/trgatev/{st_trgatve}")


if __name__ == "__main__":

    if len(m.sorte.keys()) == 0:  # koliko vnosov ma tabela

        modri = Sorta(
            ime="Modri pinot",
            kislina_cuvee=0.07,
            encimi_cuvee=1,
            cistilo_cuvee=60,
            kislina_taille=0.08,
            encimi_taille=2,
            cistilo_taille=100,
            carbon_taille=50,
            cistilo_ime_cuvee="Polymust Press (Laffort)",
            cistilo_ime_taille="Polymust Rose (Laffort)",
        )
        chardonnay = Sorta(
            ime="Chardonnay",
            kislina_cuvee=0.06,
            encimi_cuvee=1,
            cistilo_cuvee=50,
            kislina_taille=0.08,
            encimi_taille=2,
            cistilo_taille=100,
            carbon_taille=0,
            cistilo_ime_cuvee="Polymust Press (Laffort)",
            cistilo_ime_taille="Polymust Rose (Laffort)",
        )
        rebula = Sorta(
            ime="Rebula",
            kislina_cuvee=0.06,
            encimi_cuvee=1,
            cistilo_cuvee=50,
            kislina_taille=0.08,
            encimi_taille=2,
            cistilo_taille=100,
            carbon_taille=0,
            cistilo_ime_cuvee="Polymust Press (Laffort)",
            cistilo_ime_taille="Polymust Rose (Laffort)",
        )

        m.dodaj_sorto(modri)
        m.dodaj_sorto(chardonnay)
        m.dodaj_sorto(rebula)

    bottle.run(reloader=True, debug=True)
