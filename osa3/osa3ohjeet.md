# Osa 3 - Ikkunatapahtumien käsittely
Pelin olessa käynnissä pelaaja haluaa vaikuttaa pelin toimintaan. Tämä toteutetaan ikkunatapahtumilla, jotka ovat funktiokutsuja, joita ikkuna tietää suorittaa tapahtuman toteutuessa. Yleisiä ikkunatapahtumia ovat mm. ikkunan avautuminen ja sulkeutuminen tai napin painaminen ikkunan olessa aktiivinen. Pygletissä ikkunatapahtumia lisätään kutakuinkin näin:

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
Olemme jo hyödyntäneet yhtä ikkunatapahtumista, nimittäin `on_draw`:ta, jolla saadaan piirrettyä näytölle asioita. `on_draw`:ta kutsuessa olisi hyvä tyhjentää ikkuna siltä varalta, jos tietokone on vahingossa sotkenut ikkunaa sitä käsitellessään. Laita komento `ikkuna.clear()` ennen kuin piirrät muita asioita näytölle, koska muuten myös ne tyhjennetään.

```Python3
@ikkuna.event
def on_draw():
	ikkuna.clear()
	# Tästä lähtee muut piirrettävät asiat (muista rivin sisennys)
```

## Jatketaan ensimmäisen osan ohjelmaa
Viime kerralla teimme ikkunnan, johon piirrettiin ympyrä. Voimme jatkaa ohjelmaa lisäämällä ikkunalle toiminnallisuutta ikkunatapahtumilla. Lisää koodiin ikkunan luomisen jälkeen ja ennen `pyglet.app.run`:ia ikkunatapahtuma `on_key_press`. Tämä tapahtuma käsittelee ikkunan napinpainallukset:

```Python3
@ikkuna.event
def on_key_press(merkki, muuntaja):
	# Tästä alkaa sinun koodisi (muista rivin sisennys)
```

`on_key_press`:stä on hyvä huomata, että se ottaa vastaan parametrejä. Parametreistä voi selvittää mitä nappia on painettu ja missä olosuhteissa.

Tämän tapahtuman sisällä voimme vaikuttaa ympyrään, kuten vaihtaa ympyrän väriä. Seuraava koodi muuttaa ympyrän värin punaiseksi:

```Python3
ympyrä.color = 255, 0, 0
```

Voimme lisätä rivin ikkunatapahtumaan:

```Python3
@ikkuna.event
def on_key_press(merkki, muuntaja):
	ympyrä.color = 255, 0, 0
```

Nyt käynnistäessä pelin ja painaessa mitä tahansa näppäimistön nappia pallon väri vaihtuu punaiseksi. Lisätään vielä toinen ikkunatapahtuma, jolla painamisen loppuessa väri vaihtuu takaisin alkuperäiseen. Koodi näyttää kutakuinkin samalta:

```Python3
@ikkuna.event
def on_key_release(merkki, muuntaja):
	ympyrä.color = 255, 255, 255
```

Tämän lisätessämme ohjelmaan voimme pelin aikana tehdä pallosta punaisen painamalla pohjassa nappia.
