# Osa 3 - Ikkunatapahtumien käsittely
Pelin olessa käynnissä pelaaja haluaa vaikuttaa pelin toimintaan. Tämän voi toteuttaa ikkunatapahtumilla.Ikkunatapahtumat ovat erilaisia tilanteita, joita ikkunaille voi tapahtua. Yleisiä ikkunatapahtumia ovat mm. ikkunan avautuminen ja sulkeutuminen tai näppäimen painaminen ikkunan olessa aktiivinen. Jotta ikkuna tietää mitä sen kuuluu tehdä, kun sille tapahtuu jotain, pitää sille kertoa se ohjelman koodissa. Pygletissä ikkunatapahtumia lisätään kutakuinkin näin:

```Python3
@ikkuna.event          
def ikkunatapahtuma():
	# Tästä alkaa sinun koodisi (muista rivin sisennys)
```

* `@ikkuna.event` kertoo, että kyseessä on ikkunatapahtuma.
* `def ikkunatapahtuma():` kertoo, mikä tapahtuma on kyseessä
* Sen jälkeen tuleva sisennetty koodi kertoo mitä tapahtuman tapahtuessa tulee tehdä.
> Huom! `ikkuna` voi olla sinulla toisen niminen. Sen sijaan pygletissä ikkunatapahtumat ovat ennalta nimettyjä.

## Jo tuttu ikkunatapahtuma on_draw()
Olemme jo hyödyntäneet yhtä ikkunatapahtumista, nimittäin `on_draw`:ta, jolla saadaan piirrettyä näytölle asioita. `on_draw`:ta kutsuessa on hyvä tyhjentää ikkuna aina ennen uusien asioiden piirtämistä kahdesta syystä. 
- Ikkunassa saattaa olla ennen ensimmäistä piirtokertaa jotain ikkunan käsittelystä johtuvaa sotkua.
- Lisäksi tulevaisuudessa jos haluamme, että ikkunassa olevat asiat muuttuvat, kannattaa aina tyhjentää kaikki vanha ikkunasta ennen kuin piirtää siihen uudet asiat.

Laita komento `ikkuna.clear()` ensimmäiseksi ikkunatapahtumaan:

```Python3
@ikkuna.event
def on_draw():
	ikkuna.clear()
	# Tästä alkavat muut piirrettävät asiat (muista rivin sisennys)
```

## Jatketaan edellisen osan ohjelmaa
Viime kerralla teimme ikkunnan, johon piirrettiin ympyrä. Voimme jatkaa ohjelmaa lisäämällä ikkunalle ikkunatapahtumia.

## Väriä vaihtava ympyrä
Lisää koodiin ikkunan luomisen jälkeen ja ennen `pyglet.app.run`:ia ikkunatapahtuma `on_key_press`. Tämä on englantia ja tarkoittaa _näppäintä painaessa_, ja se käsittelee ikkunan näppäinten painallukset. Lisää seuraavat rivit koodiisi:

```Python3
@ikkuna.event
def on_key_press(merkki, muuntaja):
	# Tästä alkaa sinun koodisi (muista rivin sisennys)
```

`on_key_press`:stä on hyvä huomata, että se ottaa vastaan parametrejä: suluissa olevat `merkki` ja `muuntaja`. Parametrit kertovat lisätietoja painetusta näppäimestä. Tässä osassa emme kuitenkaan pureudu parametreihin sen kummemmin. Saatat kuitenkin itse jo keksiä miten saamme parametreistä selville painetun napin.

Tämän tapahtuman sisällä voimme vaikuttaa ympyrään, kuten vaihtaa ympyrän väriä. Ympyrän värin saa vaihdettua punaiseksi seuraavasti:

```Python3
ympyrä.color = 255, 0, 0
```

Voimme lisätä koodin ikkunatapahtumaan:

```Python3
@ikkuna.event
def on_key_press(merkki, muuntaja):
	ympyrä.color = 255, 0, 0
```

Nyt käynnistäessä pelin voimme huomata, että mitä tahansa näppäintä painamalla ympyrän väri vaihtuu!

Nyt kuitenkin ympyrän väri jää punaiseksi, mikä on vähän tylsää.

Lisätään vielä toinen ikkunatapahtuma, jolla painamisen loppuessa väri vaihtuu takaisin valkoiseksi. Koodi näyttää kutakuinkin samalta kuin aikaisemmin, mutta tällä kertaa määritämme tapahtuman `on_key_release`:

```Python3
@ikkuna.event
def on_key_release(merkki, muuntaja):
	ympyrä.color = 255, 255, 255
```

`on_key_release` on englantia ja tarkoittaa _näppäimen painamisen loppuessa_.

Tämän lisätessämme ohjelmaan voimme pelin aikana tehdä pallosta punaisen painamalla näppäintä pohjassa. Lopettaessa painamisen pallon väri vaihtuu takaisin alkuperäiseen valkoiseen väriin.

## Ohjelma tähän mennessä

Tähän mennessä ohjelman pitäisi siis näyttää kokonaisuudessaan tältä:
```Python3
import pyglet

ikkuna.pyglet.window.Window(width = 800, height = 600)
ympyrä = pyglet.shapes.Circle(x = 400, y = 300, radius = 100)

@ikkuna.event
def on_draw():
	ikkuna.clear()
	ympyrä.draw()

@ikkuna.event
def on_key_press(merkki, muuntaja):
	ympyrä.color = 255, 0, 0

@ikkuna.event
def on_key_release(merkki, muuntaja):
	ympyrä.color = 255, 255, 255

pyglet.app.run()
```

---

[Tehtävät](tehtävät.md)

[Seuraava osa](../osa4/ohjeet.md)