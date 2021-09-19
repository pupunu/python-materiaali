# Osa 4 - Ehtolauseet

Edellisessä osassa teimme ohjelman, jossa pallon väri vaihtui näppäintä painamalla. Ohjelmaa ei kuitenkaan kiinnostanut ollenkaan mitä näppäintä painettiin. Jatketaan ohjelmointia nyt niin, että ympyrä vaihtaa väriä ainoastaan, kun painetaan näppäintä _A_.

Näppäinten painamista tarkistava ikkunatapahtuma `on_key_press` näyttää tällä hetkellä koodissa suunnilleen tältä:

```Python3
@ikkuna.event
def on_key_press(merkki, muuntaja):
    ympyrä.color = 255, 0, 0
```

Suluissa olevat `merkki` ja `muuntaja` ovat ikkunatapahtuman parametrejä. Ne ovat ikkunatapahtuman omia muuttujia, jotka kertovat lisätietoa näppäimen painalluksesta. Muuttujaan `merkki` on tallennettu, mitä näppäintä on painettu. Muuttujaan `muuntaja` on tallennettu onko samaan aikaan painettu jotain muuntavaa näppäintä kuten Shift tai Ctrl.

Haluamme nyt muokata koodiamme niin, että ympyrän väriä muutetaan **vain** jos painettu näppäin, eli `merkki`, on A.

Kun halutaan tarkistaa ovatko jotkin kaksi asiaa sama asia, pythonissa käytetään kahta yhtäsuuruusmerkkiä. Pygletissä taas näppäimistön merkki P on `pyglet.window.key.A`. Siis voimme tarkistaa onko painettu näppäin P seuraavasti:

```Python3
merkki == pyglet.window.key.A
```

## if-komento

Pelkällä testaamisella emme kuitenkaan tee mitään. Tarvitsemme _ehtolauseen_. Haluamme sanoa ohjelmalle, että **jos** `merkki == pyglet.window.key.A`, niin ympyrän väriksi vaihtuu punainen. Poista koodistasi `ympyrä.color = 255, 0, 0` ja korvaa se seuraavalla ehtolauseella:

```Python3
if merkki == pyglet.window.key.A:
    ympyrä.color = 255, 0, 0
```
> Huom! Muista sisennys rivillä `ympyrä.color = 255, 0, 0`, niin että se on ehtolauseen sisällä.

`if` on englantia ja tarkoittaa _jos_. Sitä kutsutaan ehtolauseeksi, koska sille annetaan ehto, kuten `merkki == pyglet.window.key.P`. Jos ehto on totta, niin `if`:n sisällä olevat asiat toteutuvat. Jos ehto taas ei ole totta, esimerkiksi painettu näppäin on B eikä A, niin ehtolauseen sisällä olevat komennot eivät toteudu.

Nyt ympyrän pitäisi muuttua punaiseksi ainoastaan, jos painetaan näppäintä A.


## else-komento

Entäpä jos haluaisimme, että ympyrä muuttuu punaiseksi kun painetaan nappia A, mutta muita nappeja painamalla se muuttuisikin siniseksi?

Tällaisen ohjelmoimiseksi tarvitsemme jotain `if`-ehtolauseemme lisäksi. Tarvitsemme `else`-lauseen. Else on englantia ja tarkoittaa kutakuinkin _muussa tapauksessa_.

Haluamme siis, että nappia painaessa _jos painettu nappi on A, ympyrästä tulee punainen. Muussa tapauksessa ympyrästä tulee sininen_.

Haluamamme ohjelman saisi siis ohjelmoitua lisäämällä ikkunatapahtumaan `on_key_press` ehtolause _muussa tapauksessa_.

```Python3
@ikkuna.event
def on_key_press(merkki, muuntaja):
    if merkki == pyglet.window.key.P:
        ympyrä.color = 255, 0, 0
    else:
        ympyrä.color = 0, 0, 255
```

## Ohjelma tähän mennessä

Tähän mennessä koko ohjelma näyttää siis seuraavalta:

```Python3
import pyglet

ikkuna = pyglet.window.Window(width = 800, height = 600)
ympyrä = pyglet.shapes.Circle(x = 400, y = 300, radius = 100)

@ikkuna.event
def on_draw():
	ikkuna.clear()
	ympyrä.draw()

@ikkuna.event
def on_key_press(merkki, muuntaja):
	if merkki == pyglet.window.key.A:
		ympyrä.color = 255, 0, 0
	else:
		ympyrä.color = 0, 0, 255


@ikkuna.event
def on_key_release(merkki, muuntaja):
	ympyrä.color = 255, 255, 255

pyglet.app.run()
```

## Koodi suomeksi

Ohjelmoidessa törmää koko ajan uusiin sanoihin ja termeihin ja ne on helpompi muistaa, jos tietää mitä ne oikeasti tarkoittavat. Tässä on tähän asti tekemämme ohjelma suomennettuna.

---

[Tehtävät](tehtävät.md)

[Seuraava osa](../osa5/ohjeet.md)