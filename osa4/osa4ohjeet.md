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

## Erilaisia näppäimiä ja erilaisia värejä

Tehdään seuraavaksi niin, että ympyrä muuttuu punaiseksi jos painetaan P:tä, siniseksi jos painetaan S:ää ja vihreäksi jos painetaan V:tä.

Voisimme lisätä koodiin lisää if-komentoja, mutta on tyylikkäämpää tehdä se elif-komennoilla. 

[Seuraava osa]