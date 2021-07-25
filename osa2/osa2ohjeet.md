# Osa 2 - Ikkunataphtumien käsittely
Pelin olessa käynnissä pelaaja haluaa vaikuttaa pelin toimintaan. Tämä voidaan toteuttaa ikkunatapahtumilla, jotka ovat funktio kutsuja, joita ikkuna tietää suorittaa tapahtuman toteutuessa. Yleisiä ikkunatapahtumia ovat mm. ikkunan avautuminen ja sulkeutuminen tai napin painaminen ikkunan olessa aktiivinen. Pygletissä ikkunatapahtumia lisätään kutakuinkin näin.

```Python3
@ikkuna.event
def ikkunatapahtuma:
	# Omaa toiminnallisuutta
```

`ikkuna` voi olla sinulla toisella nimellä. Pygletin ikkunatapahtumat ovat myös Pygletissä ennalta nimettyjä.

Viime kerralla teimme ikkunnan, johon piirrettiin ympyrä. Voimme jatkaa peliä lisäämällä samalle ikkunalle toiminnallisuutta ikkunatapahtumilla. Lisää koodiin ikkunan luomisen ja ennen `pyglet.app.run`ia ikkunatapahtuma `on_key_pressed`. Tämä käsittelee ikkunan napinpainallukset.

```Python3
@ikkuna.event
def on_key_pressed():
	# Omaa toiminnallisuutta
```

Tämän funktion sisällä voimme vaikuttaa ympyrään, kuten vaihtaa ympyrän väriä. Ympyrän värin vaihtaminen punaiseksi toteutuu seuraavasti:

```Python3
ympyrä.color = 255, 0, 0
```

Voimme lisätä rivin ikkunatapahtumaan:

```Python3
@ikkuna.event
def on_key_pressed():
	ympyrä.color = 255, 0, 0
```

Nyt käynnistäessämme pelin voimme huomata nappia painamalla ympyrän värin vaihtuvan.
