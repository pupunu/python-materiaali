# Osa 3 - Ikkunatapahtumien käsittely
Pelin olessa käynnissä pelaaja haluaa vaikuttaa pelin toimintaan. Tämän voi toteuttaa ikkunatapahtumilla.Ikkunatapahtumat ovat erilaisia tilanteita, joita ikkunaille voi tapahtua. Yleisiä ikkunatapahtumia ovat mm. ikkunan avautuminen ja sulkeutuminen tai napin painaminen ikkunan olessa aktiivinen. Jotta ikkuna tietää mitä sen kuuluu tejdä, kun sille tapahtuu jotain, pitää sille kertoa se ohjelman koodissa. Pygletissä ikkunatapahtumia lisätään kutakuinkin näin:

```Python3
@ikkuna.event          
def ikkunatapahtuma():
	# Tästä alkaa sinun koodisi (muista rivin sisennys)
```

* `@ikkuna.event` kertoo, että kyseessä on ikkunatapahtuma.
* `def ikkunatapahtuma():` kertoo, mikä tapahtuma on kyseessä
* Sen jälkeen tuleva sisennetty koodi kertoo mitä tapahtuman tapahtuessa tulee tehdä.
> Huom! `ikkuna` voi olla sinulla toisen niminen. Pygletissä ikkunatapahtumat ovat ennalta nimettyjä.

## Jo tuttu ikkunatapahtuma
Olemme jo hyödyntäneet yhtä ikkunatapahtumista, nimittäin `on_draw`:ta, jolla saadaan piirrettyä näytölle asioita. `on_draw`:ta kutsuessa olisi hyvä tyhjentää ikkuna siltä varalta, jos tietokone on vahingossa sotkenut ikkunaa sitä käsitellessään. Laita komento `ikkuna.clear()` ennen kuin piirrät muita asioita näytölle, koska muuten myös uudet asiat tyhjennetään.

```Python3
@ikkuna.event
def on_draw():
	ikkuna.clear()
	# Tästä lähtee muut piirrettävät asiat (muista rivin sisennys)
```

## Jatketaan ensimmäisen osan ohjelmaa
Viime kerralla teimme ikkunnan, johon piirrettiin ympyrä. Voimme jatkaa ohjelmaa lisäämällä ikkunalle ikkunatapahtumia. Lisää koodiin ikkunan luomisen jälkeen ja ennen `pyglet.app.run`:ia ikkunatapahtuma `on_key_press`. Tämä tapahtuma käsittelee ikkunan napinpainallukset. Lisää seuraavat rivit koodiisi:

```Python3
@ikkuna.event
def on_key_press(merkki, muuntaja):
	# Tästä alkaa sinun koodisi (muista rivin sisennys)
```

`on_key_press`:stä on hyvä huomata, että se ottaa vastaan parametrejä. Parametreistä voi selvittää mitä nappia on painettu ja missä olosuhteissa. Tässä osassa emme kuitenkaan pureudu parametreihin sen kymmemmin, mutta saatat pystyä itse selvittämään miten saamme selville parametreistä kyseisen painetun napin.

Tämän tapahtuman sisällä voimme vaikuttaa ympyrään, kuten vaihtaa ympyrän väriä. Ympyrän värin vaihtaminen punaiseksi toteutuu seuraavasti:

```Python3
ympyrä.color = 255, 0, 0
```

Voimme lisätä rivin ikkunatapahtumaan:

```Python3
@ikkuna.event
def on_key_press(merkki, muuntaja):
	ympyrä.color = 255, 0, 0
```

Nyt käynnistäessä pelin voimme huomata nappia painamalla ympyrän värin vaihtuvan. Lisätään vielä toinen ikkunatapahtuma, jolla painamisen loppuessa väri vaihtuu takaisin valkoiseksi. Koodi näyttää kutakuinkin samalta kuin aikaisemmin, mutta tällä kertaa määritämme tapahtuman `on_key_release`:

```Python3
@ikkuna.event
def on_key_release(merkki, muuntaja):
	ympyrä.color = 255, 255, 255
```

Tämän lisätessämme ohjelmaan voimme pelin aikana tehdä pallosta punaisen painamalla pohjassa nappia. Lopettaessa painamisen pallon väri vaihtuu takaisin alkuperäiseen valkoiseen väriin.
