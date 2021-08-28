# Osa 4 - Ehtolauseet

Edellisessä osassa teimme ohjelman, jossa pallon väri vaihtui näppäintä painamalla. Ohjelmaa ei kuitenkaan kiinnostanut ollenkaan mitä näppäintä painettiin. Jatketaan ohjelmointia nyt niin, että ympyrä vaihtaa väriä ainoastaan, kun painetaan näppäintä _A_.

Näppäinten painamista tarkistava ikkunatapahtuma `on_key_press` näyttää tällä hetkellä koodissa suunnilleen tältä:

```Python3
@ikkuna.event
def on_key_press(merkki, muuntaja):
    ympyrä.color = 255, 0, 0
```

Suluissa olevat `merkki` ja `muuntaja` ovat ikkunatapahtuman parametrejä. Ne ovat ikkunatapahtuman omia muuttujia, jotka kertovat lisätietoa näppäimen painalluksesta. Muuttujaan `merkki` on tallennettu, mitä näppäintä on painettu. Muuttujaan `muuntaja` on tallennettu onko samaan aikaan painettu jotain muuntavaa näppäintä kuten Shift tai Ctrl.

Haluamme nyt muokata koodiamme niin, että ympyrän väriä muutetaan **vain** jos painettu näppäin, eli `merkki`, on _A_.

Kun halutaan tarkistaa ovatko jotkin kaksi asiaa sama asia, pythonissa käytetään kahta yhtäsuuruusmerkkiä. Pygletissä taas näppäimistön merkki _A_ on `pyglet.window.key.A`. Siis voimme tarkistaa onko painettu näppäin _A_ seuraavasti:

```Python3
merkki == pyglet.window.key.A
```

Pelkällä testaamisella emme kuitenkaan tee mitään. Tarvitsemme _ehtolauseen_.

Poistetaan ikkunatapahtumasta.