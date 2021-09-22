# Osa 5 - Aikataulutus ja funktiot - Tehtävät 

1. 

a) Tee ohjelma, jolla on ikkuna, jonka keskelle piirretään ympyrä.

b) Ohjelmoi ympyrä muuttumaan punaiseksi nappia painamalla. Ympyrän ei siis tarvitse muuttua takaisin valkoiseksi painamisen jälkeen.

---

2. 

Jatka edellisen tehtävän ohjelmaa.

a) Kirjoita funktio, joka vaihtaa ympyrän väriä sekunnin välein alla olevan kuvan mukaan.

<img src=kuvat/diskopallo.png height="400">

b) Muuta koodia niin, että väri vaihtuukin kolmen sekunnin välein.

c) Muuta koodia niin, että väri vaihtuukin kahdesti sekunnissa.

---

3. 

Jatka edellisen tehtävän ohjelmaa.

a) Alla on funktio, joka siirtää ympyrän vasempaan alareunaan. Kirjoita tai kopioi se ohjelmaasi.

```Python3
def alakulmaan(dt):
    ympyrä.x = 0
    ympyrä.y = 0
```

b) Aikatauluta funktio tapahtumaan kahden sekunnin kuluttua ohjelman käynnistämisestä.

---

4. 

Aloita uusi ohjelma.

a) Tee ohjelma, jolla on ikkuna, jonka keskelle piirretään ympyrä.

b) Kirjoita tai kopioi alla oleva funktio ohjelmaasi.

```Python3
def siirtyminen(dt):
    if ympyrä.x == 50:
        ympyrä.x = 200
    else:
        ympyrä.x = 50
```

c) Aikatauluta funktio tapahtumaan kahden sekunnin välein.

---

5. 

Aloita uusi ohjelma.

a) Tee ohjelma, jolla on ikkuna, jonka keskelle piirretään ympyrä.

b) Alla on funktio, joka muuttaa ympyrää. Kirjoita tai kopioi se ohjelmaasi.

```Python3
def värimuunnos(dt):
    if ympyrä.color[0] > 25:
        ympyrä.color = ympyrä.color[0] - 25, 255, 255
```

c) Aikatauluta funktio tapahtumaan viisi kertaa sekunnissa (0.2 sekunnin välein).

d) Mitä tapahtuu?

---

6. (Haastavampi tehtävä)

Jatka edellistä tehtävää.

Ympyrän väri koostuu kolmesta numerosta: punaisen, vihreän ja sinisen määrästä. `ympyrä.color[0]` tarkoittaa värin ensimmäistä numeroa, `ympyrä.color[1]` tarkoittaa värin toista numeroa ja `ympyrä.color[2]` tarkoittaa kolmatta numeroa.

Edellisen tehtävän funktio onkin siis kutakuinkin näin:

```
määritele värimuunnos(delta-aika):
    jos ympyrän värin ensimmäinen luku on isompi kuin 25:
        vähennetään ympyrän ensimmäisestä numerosta 25. Muut numerot ovat 255.
```

c) Muokkaa funktiota niin, että värin ensimmäistä numeroa muutetaan vähemmän.

b) Muokkaa funktiota niin, että siinä muutetaankin ainoastaan värin toista numeroa.

c) Muuta funktiota niin, että siinä muutetaan toista ja kolmatta numeroa.

---

7. (Haastavampi tehtävä)

Aloita uusi ohjelma.

Ympyrällä on muitakin ominaisuuksia kuin väri ja sijainti. Yksi näistä on ympyrän säde. Ympyrän säde on tallennettuna muuttujaan `ympyrä.radius`. _Radius_ on englantia ja tarkoittaa sädettä.

<img src=kuvat/säde.png height="400">

a) Tee ohjelma, jolla on ikkuna, johon piirretään ympyrä.

b) Koodi `ympyrä.radius = ympyrä.radius + 1` suurentaa säteen kokoa yhdellä. Kirjoita funktio, joka suurentaa säteen kokoa viidellä.

c) Aikatauluta tämä funktio tapahtumaan puolen sekunnin välein. Mitä ohjelma tekee?

---

8. (Haastavampi tehtävä)

Jatka edellisen tehtävän ohjelmaa.

a) Muokataan koodia niin, että säteellä on jokin maksimikoko. Muokkaa funktiota siis niin, että kokoa suurennetaan vain _jos_ säteen koko on pienempi kuin 300.

> Vinkki! `x < 7` testaa onko x pienempi kuin seitsemän.

b) Muokkaa ohjelmaa niin, että muussa tapauksessa säteen kooksi asetetaan 10.