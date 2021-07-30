# Osa 2 - Ikkunatapahtumien käsittely
Pelin olessa käynnissä pelaaja haluaa vaikuttaa pelin toimintaan. Tämän voi toteuttaa ikkunatapahtumilla. Ikkunatapahtumat ovat erilaisia asioita mitä ikkunalle voi tapahtua. Niitä ovat mm. ikkunan sulkeminen ja näppäinten painaminen. Jotta ikkuna tietää mitä sen kuuluu tehdä, kun sille tapahtuu jotain, pitää sille kertoa se ohjelman koodissa. Myös ikkunaan piirtäminen on ikkunatapahtuma, jota käytimmekin jo osassa 1.

Pygletissä ikkunatapahtumia lisätään kutakuinkin näin:

```Python3
@ikkuna.event
def ikkunatapahtuma():
	# Tänne tulee mitä ohjelman pitää tehdä
```

`ikkuna` voi olla sinulla toisella nimellä. Pygletin ikkunatapahtumat ovat myös ennalta nimettyjä.

Viime kerralla teimme ikkunnan, johon piirrettiin ympyrä. Voimme jatkaa ohjelmaa lisäämällä ikkunalle ikkunatapahtumia. Lisää koodiin ikkunan luomisen jälkeen ja ennen `pyglet.app.run`ia ikkunatapahtuma `on_key_press`. Tämä tapahtuma käsittelee ikkunan napinpainallukset:

```Python3
@ikkuna.event
def on_key_press(merkki, muuntaja):
	# Oma koodi
```

Tämän tapahtuman sisällä voimme vaikuttaa ympyrään, kuten vaihtaa ympyrän väriä. Ympyrän värin vaihtaminen punaiseksi toteutuu seuraavasti:

```Python3
ympyrä.color = 255, 0, 0
```

Voimme lisätä rivin ikkunatapahtumaan:

```Python3
@ikkuna.event
def on_key_press():
	ympyrä.color = 255, 0, 0
```

Nyt käynnistäessämme pelin voimme huomata nappia painamalla ympyrän värin vaihtuvan. Lisätään se, että ympyrän väri riippuu siitä mikä nappi painetaan. Sen, mikä nappi on painettu `on_key_press` tapahtuman aikana, saa selville tapahtuman parametrista. Voimme lisätä siten tapahtumaan parametrin `merkki`.

```Python3
@ikkuna.event
def on_key_press(merkki, muuntaja):
	ympyrä.color = 255, 0, 0
```

Voimme selvittää onko merkki, jokin tietty napin painallus seuraavasti:
```Python3
merkki == pyglet.window.key.A
```
TODO - SELITYS MERKEILLE

```Python3
@ikkuna.event
def on_key_press(merkki):
	if merkki == pyglet.window.key._1:
		ympyrä.color = 255, 0, 0
	elif merkki == pyglet.window.key._2:
		ympyrä.color = 0, 255, 0
	elif merkki == pyglet.window.key._3:
		ympyrä.color = 0, 0, 255
```

```Python3
@ikkuna.event
def on_key_release(merkki):
	ympyrä.color = 255, 255, 255
```
