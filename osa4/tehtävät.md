# Osa 4 - Ehtolauseet - Tehtävät

Tarvitset tehtäviä varten ohjelman, jolla on ikkuna, jossa näkyy valkoinen ympyrä.

1. 

a) Lisää ikkunatapahtuma, joka tarkistaa painetaanko jotain nappia.

b) Ohjelmoin ympyrä vaihtamaan väriä punaiseksi, kun mitä tahansa nappia painetaan.

c) Lisää ohjelmaan ikkunatapahtuma, joka muuttaa ympyrän takaisin valkoiseksi, kun napin painaminen loppuu.

---

2. 

Jatka edellisen tehtävän ohjelmaa ja muokkaa ikkunatapahtumaan, joka käsittelee napinpainallukset.

a) Poista koodi joka muuttaa ympyrän punaiseksi.

b) Kirjoita ehtolause, joka tarkistaa, että painettu nappi on A.

c) Laita ympyrä muuttamaan väriä punaiseksi jos painettu nappi on A.

---

3. 

Jatka edellisen tehtävän ohjelmaa.

Muokkaa koodia niin, että ympyrä vaihtaa väriä mitä tahansa nappia painamalla, mutta väriksi tulee punainen jos painetaan nappia A, ja sininen jos painetaan jotain muuta nappia.

---

4. 

Jatka edellisen tehtävän ohjelmaa.

a) Muokkaa koodia `pyglet.window.key.A` muotoon `pyglet.window.key.R`. Keksitkö mitä muutos sai aikaiseksi?

b) Muokkaa koodia niin, että ympyrä muuttuu punaiseksi painamalla nappia _P_.

---

5. (Haastavampi tehtävä)

Entä jos haluaisimme, että ympyrä on punainen, kun painamme nappia P, vihreä kun painamme nappia V ja sininen kun painetaan jotain muuta nappia?

Kun haluamme antaa useita tarkkoja vaihtoehtoa ohjelmalle, tarvitsemme ehtolausetta `elif`. Se on lyhenne englannin sanoista _else if_ ja tarkoittaa suomeksi _tai jos_. Toisin sanoen haluamme ohjelmoida, että nappia painaessa:
- jos nappi on P, muutetaan väriksi punainen
- tai jos nappi on V, muutetaan väriksi vihreä
- muussa tapauksessa muutetaan väriksi sininen.

Haluamamme ohjelman saisi siis toteutettua muuttamalla ikkunatapahtumaa `on_key_press` seuraavanlaiseksi:

```Python3
@ikkuna.event
def on_key_press(merkki, muuntaja):
    if merkki == pyglet.window.key.P:
        ympyrä.color = 255, 0, 0
    elif merkki == pyglet.window.key.V:
        ympyrä.color = 0, 255, 0
    else:
        ympyrä.color = 0, 0, 255
```

Tietokone käy järjestyksessä läpi sille annettuja ehtolauseita kunnes törmää sellaiseen ehtoon mikä on totta, jolloin ehtolauseen sisältö toteutuu. Jos mikään ehto ei ole totta, toteutetaan ehtolauseen _muussa tapauksessa_ sisällä oleva koodi.

Jatka edellisen tehtävän ohjelmaa

a) Muokkaa ohjelmaasi niin, että painaessa nappia P, ympyrä muuttuu punaiseksi, mutta mistä tahansa muusta napista ympyrä muuttuukin siniseksi.

b) Muokkaa ohjelmaasi niin, että ympyrä muuttuu nappia V painaessa vihreäksi.

c) Muokkaa ohjelmaani niin, että jos painetaan nappia K, ympyrä muuttuu keltaiseksi. Ympyrä muuttuu keltaiseksi koodilla `ympyrä.color = 255, 255, 0`