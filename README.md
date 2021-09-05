# Projektna naloga pri predmetu Uvod v programiranje

## Identifikacija trgatve


Program je namenjen računanju določenih parametrov, ki se spreminjajo glede na vneseno količino grozdja (ki jo damo v prešo) in sorte (Chardonnay, Rebula in Modri pinot). Za lažje beleženje posameznih trgatev določimo tudi datum posamezne trgatve. Ko damo določeno količino grozdja v prešo, iz njega izstisnemo sok (mošt), v katerega dodamo izračunano količino aditivov (npr. kislina, encimi, čistilo...), kateri nam omogočajo hitrejše sesedanje odvečnih umazanij iz mošta, ki ga naslednji dan pretočimo in stem odstranimo odvečno količino umazanije. Za tem sok začne fermentirati, kateri dokonča svojo fermentacijo v cca. 14 dneh, nato nastane vino. 

Idejo za izdelavo moje projektne naloge sem dobila doma, saj se moji starši ukvarjajo s pridelavo penečih vin. Tako, sem svojemu očetu v pomoč napisala program, ki mu bo v času trgatve omogočil računalniško računanje posameznih parametrov. 

Program deluje tako, da vnesemo količino grozdja (ki jo bomo dali v prešo), izberemo sorto potrganega grozdja (Chardonnay, Rebula ali Modri pinot) in datum (kdaj je bilo grozdje potrgano). Ko pritisnemo na gumb "Dodaj", program izračuna naslednje parametre in doda trgatev med trgatve:
-količina soka, ki jo dobimo iz vnesene količine grozdja
-od količine soka izračuna taille (slabši del soka) in cuvee (boljši del soka)
-količina kisline, ki jo dodamo v taille
-količina kisline, ki jo dodamo v cuvee
Na posamezni trgatvi imamo možnost "Izbriši" in "Prikaži več". Z gumbom "Izbriši" lahko vneseno trgatev pobrišemo, gumb "Prikaži več" pa nas vodi na podstran, kjer se prikaže še nekaj izračunanih parametrov (na podlagi vnesene količine, sorte in datuma):
1. količina encimov, ki jih dodamo v taille
2. količina encimov, ki jih dodamo v cuvee
3. količina čistila, ki ga dodamo v taille
4. količina čistila, ki ga dodamo v cuvee
5. količina carbona, ki ga dodamo v taille (samo pri sorti Modri pinot)
6. ime čistila, ki ga dodamo

Sedaj imamo tudi možnost posodobitve trgatve, kar nam omogoča gumb "Posodobi", z njim lahko spremenimo vneseno količino, sorto ali pa datum (npr. v primeru, da smo se zmotili pri tehtanju grozdja). Če trgatev posodobimo, se med trgatve shrani posodobljena trgatev. 
Na koncu začetne spletne strani imamo tudi vodeno skupno količino grozdja in soka, ki ju računa računalnik na podlagi vnesenih trgatev, razdeljeno po sortah grozdja (Chardonnay, Rebula in Modri pinot).

Spletno aplikacijo lahko zaženemo z uporabo ukaza: 
`python spletni_vmesnik.py`. 
Za izdelavo projektne naloge sem uporabila knjižnjico bottle. 








