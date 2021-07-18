# Osa 1 - Ikkuna ja ympyrä

## Mikä on ikkuna

Ikkuna on se mitä yleensä pidetään ohjelmana. Oikeasti ikkuna on kuitenkin vain se osa ohjelmaa, jonka kanssa käyttäjä on tekemisissä. Ikkuna huolehtii muun muassa siitä, että käyttäjä näkee näytöllä jotain, sekä seuraa mitä näppäimiä käyttäjä painaa tai missä hiiren osoitin kulkee.

Tässä on esimerkki Miinaharava-pelin ikkunasta:
![kuva miinaharavasta](miinaharavaikkuna.png)

## Pygletin ikkuna

Jotta voimme saada jotain kivaa näkyviin, tarvitsemme ikkunan. Pygletistä löytyy tätä varten Window-niminen olio. Window on englantia ja tarkoittaa ikkunaa. Mitä sitten tarkoittaa, että ikkuna on olio? Ei sen kummempaa kuin, että ikkuna on tavallaan jokin asia, jolla on erilaisia ominaisuuksia (kuten koko tai nimi) ja se osaa tehdä erilaisia asioita (kuten piirtää itseensä).

## Tehdään ohjelma jolla on ikkuna!

Tarvitsemme ikkunaa varten pyglettiä joten lisätään se ohjelmaan kirjoittamalla kooditiedoston alkuun:

```Python3
import pyglet

``` 

Seuraavaksi luodaan meille ikkuna. Sanotaan siis ohjelmalle, että jokin asia nimeltä ikkuna on Pygletin ikkuna (eli Window). Lisäksi kerrotaan minkä kokoinen tämä ikkuna on. `width` tarkoittaa leveyttä ja `height` korkeutta.

```Python3

ikkuna = pyglet.window.Window(width=800, height=600)

```

Nyt ohjelmalla on tiedossa ikkuna, mutta sillä ei tehdä vielä mitään. Haluamme, että Pyglet lähtee käyntiin, jolloin ikkuna tulee näkyviin. Lisätään siis aivan ohjelman koodin loppuu

```Python3


pyglet.app.run()
```
Nyt kun laitamme Python-ohjelmamme käytiin, näytölle ilmestyy tyhjä ruutu.

![tyhjä ikkuna](tyhjäikkuna.png)

Pygletin ikkuna on kuin liitutaulu. Siihen voi piirtää asioita tai taulun voi pyyhkiä tyhjäksi.