# Osa 2 - Ikkunatapahtumien käsittely
Pelin olessa käynnissä pelaaja haluaa vaikuttaa pelin toimintaan. Tämä toteutetaan ikkunatapahtumilla, jotka ovat funktiokutsuja, joita ikkuna tietää suorittaa tapahtuman toteutuessa. Yleisiä ikkunatapahtumia ovat mm. ikkunan avautuminen ja sulkeutuminen tai napin painaminen ikkunan olessa aktiivinen. Pygletissä ikkunatapahtumia lisätään kutakuinkin näin.

```Python3
@ikkuna.event          
def ikkunatapahtuma():
	# Tästä alkaa sinun koodisi (muista rivin sisennys)
```

* `@ikkuna.event` kertoo, että kyseessä on ikkunatapahtuma.
* `def ikkunatapahtuma():` kertoo, mikä tapahtuma on kyseessä
* Sen jälkeen tuleva sisennetty koodi kertoo mitä tapahtuman tapahtuessa tulee tehdä.
>> Huom! `ikkuna` voi olla sinulla toisen niminen. Pygletissä ikkunatapahtumat ovat ennalta nimettyjä.

## Jatketaan ensimmäisen osan ohjelmaa

Viime kerralla teimme ikkunnan, johon piirrettiin ympyrä. Voimme jatkaa ohjelmaa lisäämällä ikkunalle toiminnallisuutta ikkunatapahtumilla. Lisää koodiin ikkunan luomisen jälkeen ja ennen `pyglet.app.run`ia ikkunatapahtuma `on_key_press`. Tämä tapahtuma käsittelee ikkunan napinpainallukset:

```Python3
@ikkuna.event
def on_key_press(merkki, muuntaja):
	# Tästä alkaa sinun koodisi (muista rivin sisennys)
```

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

Tämän lisätessä ohjelmaan voimme pelin aikana tehdä pallosta punaisen painamalla pohjassa nappia.

---
-- leikkaa seuraavaan osaan. --

Nyt käynnistäessämme pelin voimme huomata nappia painaessamme ympyrän värin vaihtuvan. Tällä hetkellä ohjelmaa ei kiinnosta mitä nappia painetaan. Muokataan koodia niin, että väri vaihtuu vain tietystä napista. Tapahtuma kirjaa ylös muuttujaan merkki mitä nappia on painetta.

Voimme kokeilla on merkissä oleva nappi sama kuin nappia "A" tällä tavalla:

```Python3
merkki == pyglet.window.key.A
```

Laittamalla `A`:n tilalle muita merkkejä voimme kokeilla muiden nappien varalta.

```Python3
@ikkuna.event
def on_key_press(merkki, muuntaja):
	if merkki == pyglet.window.key.A:
		ympyrä.color = 255, 0, 0
```

```Python3
@ikkuna.event
def on_key_press(merkki, muuntaja):
	if merkki == pyglet.window.key._1:
		ympyrä.color = 255, 0, 0
	elif merkki == pyglet.window.key._2:
		ympyrä.color = 0, 255, 0
	elif merkki == pyglet.window.key._3:
		ympyrä.color = 0, 0, 255
```

