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
