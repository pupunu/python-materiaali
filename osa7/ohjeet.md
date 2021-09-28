# Osa 7 - Ohjattava ympyrä

Nyt olemme oppineet niin paljon asioita, että voimme ohjelmoida ympyrän liikkumaan ylös-alas nappia painamalla! Sitä varten meidän pitää ohjelmoida:

1. Ikkunatapahtumassa `on_key_press` tallennetaan muistiin mihin suuntaan olemme menossa.
2. Ikkunatapahtumassa `on_key_release` tallennamme, onko johonkin suuntaan liikkuminen loppunut.
3. Funktio joka tarkistaa mihin suuntaan ollaan menossa ja sen perusteella muuttaa hahmon sijaintia.
4. Aikataulutetaan funktio tapahtumaan koko ajan.

## Ohjelman siistimistä

Olemme tähän asti kokeilleet ohjelmassamme paljon kaikenlaista, mutta nyt kun ohjelmoimme liikkumista, olisi kiva saada kaikki ylimääräiset asiat ohjelmasta pois. Tehdään siis uusi tiedosto, johon sitten voimme ohjelmoida ympyrän liikkumisen. Voit saada tämän tiedoston seuraamalla osien 1 ja 2 ohjeita tai kopioimalla tyhjään tiedostoon alla olevan koodin.

```Python3
import pyglet

ikkuna = pyglet.window.Window(width = 800, height = 600)
ympyrä = pyglet.shapes.Circle(x = 400, y = 300, radius = 100)

@ikkuna.event
def on_draw():
    ikkuna.clear()
    ympyrä.draw()

pyglet.app.run()
```

Huom! Muista laittaa koodi `ikkuna.clear()` ikkunatapahtuman `on_draw()` sisään. Nyt kun meillä on liikkuvia asioita, pitää ikkuna tyhjentää aina ennen uusien asioiden piirtämistä.

## Liikkumissuunnan tallennus

Haluamme tallentaa johonkin mitä nappia on painettu, eli mihin suuntaan olemme matkalla. Tehdään tätä varten _hashmap_. Emme nyt käy kovin syvällisesti mikä hashmap on, vaan voit kopioida alla olevan koodin:

```Python3
suunta = {'ylös':False, 'alas':False}
```

Kirjoita koodi juuri ennen `on_draw()`-ikkunatapahtumaa.

Hyödyllistä on tietää, että jos haluamme nyt saada tietää olemmeko menossa ylös, se on talennettuna muutujaan `suunta['ylös']`. Jos olemme menossa ylös, muuttujan arvo on `True`, eli totta, jos taas emme ole menossa ylös, se on `False`, eli epätosi.


## on_key_press

Ohjelmoidaan ensin ylöspäin liikkuminen kokonaan. Haluamme siis että jos painetaan näppäintä nuoli ylös, liikkumissuunnasta ylös tulee tosi. Kyseessä on tuttu ehtolause:

```Python3
@ikkuna.event
def on_key_press(merkki, muuntaja):
    if merkki == pyglet.window.key.UP:
        suunta['ylös'] = True
```

Lisää uusi koodi ennen koodia `pyglet.app.run()`.

> `pyglet.window.key.UP` tarkoittaa nuoli ylös -näppäintä. _UP_ on englantia ja tarkoittaa ylös.
> `suunta['ylös'] = True` muuttaa suunnan ylös arvoksi _True_, eli totta.

## on_key_release

Ohjelmoidaan seuraavaksi, että kun lopetamme ylöspäinnapin painamista, suuntamme ei ole enää ylöspäin. Käytetään ikkunatapahtumaa `on_key_release` ja tuttua ehtolausetta:

```Python3
@ikkuna.event
def on_key_release(merkki, muuntaja):
    if merkki == pyglet.window.key.UP:
        suunta['ylös'] = False
```

Lisää ikkunatapahtuma edellisen perään ennen koodia `pyglet.app.run()`.

## liiku-funktio

Kirjoitetaa seuraavaksi funktio, joka muuttaa ympyrän sijaintia jos _suunta ylös_ on totta.

Aloitetaan funktio määrittelemällä ja antamalla sille nimi. Se tarvitsee yhden arvon sulkuihin, nimittäin dt, koska se on aikataulutettava funktio. Funktio katsoo jos `suunta['ylös'] == True`, ja silloin lisää ympyrän y-koordinaattiin 10.

```Python3
def liiku(dt):
    if suunta['ylös'] == True:
        ympyrä.y = ympyrä.y + 10
```

Kirjoita uusi koodi juuri ennen koodia `pyglet.app.run()`.

## Funktion aikataulutus

Jäljelle on jäänyt vain liikkumisfunktion aikataulutus. Koska haluamme että hahmomme liikkuu jatkuvasti, haluamme että ohjelma muuttaa sijaintia koko ajan.

```Python3
pyglet.clock.schedule(liiku)
```

Kirjoita uusi koodi juuri ennen koodia `pyglet.app.run()`.

Kokeile nyt ohjelmaasi ja paina näppäimistöltä nappia nuoli ylös!

## Alaspäin

Ohjelmoidaan vielä liikkuminen alaspäin. Englanniksi alas on `DOWN`, joten nappi alaspäin on `pyglet.window.key.DOWN`.

Voimme käyttää edelleen tuttuja ehtolauseita ikkunatapahtumissa:

```Python3
@ikkuna.event
def on_key_press(merkki, muuntaja):
    if merkki == pyglet.window.key.UP:
        suunta['ylös'] = True
    elif merkki == pyglet.window.key.DOWN:  #Tällä rivillä alkaa lisätty koodi
        suunta['alas'] = True               #Tämän rivin jälkeen alkaa taas vanha koodi

@ikkuna.event
def on_key_release(merkki, muuntaja):
    if merkki == pyglet.window.key.UP:
        suunta['ylös'] = False
    elif merkki == pyglet.window.key.DOWN:  #Tästä rivistä alkaa taas uusi koodi
        suunta['alas'] = False              #Tähän loppuu uusi koodi
```

Sen sijaan liikkuessa emme halua käyttää elif-komentoja. Miksi? Koska elif-komennoilla jos yksi ehto on totta, muita ehtoja ei huomioida. On kuitenkin mahdollista, että painetaan samaan aikaan sekä ylös että alas, jolloin pitäisi kulkea molempiin suuntiin (molempiin suuntiin kulkeminen on paikallaan pysymistä). Siis testataan vain jokainen suunta omalla ehtolauseellaan.

```Python3
def liiku(dt):
    if suunta['ylös'] == True:
        ympyrä.y = ympyrä.y + 10

    if suunta['alas'] == True:              #Tällä rivillä alkaa uusi koodi
        ympyrä.y = ympyrä.y - 10
```

Nyt ympyrä liikkuu ikkunassa ylös alas!

## Koodi kokonaisuudessaan

Ohjelmamme koodin pitäisi siis näyttää nyt tältä

```Python3
import pyglet

ikkuna = pyglet.window.Window(width = 800, height = 600)
ympyrä = pyglet.shapes.Circle(x = 400, y = 300, radius = 100)


suunta = {'ylös':False, 'alas':False}

@ikkuna.event
def on_draw():
    ikkuna.clear()
    ympyrä.draw()

@ikkuna.event
def on_key_press(merkki, muuntaja):
    if merkki == pyglet.window.key.UP:
        suunta['ylös'] = True
    elif merkki == pyglet.window.key.DOWN:
        suunta['alas'] = True

@ikkuna.event
def on_key_release(merkki, muuntaja):
    if merkki == pyglet.window.key.UP:
        suunta['ylös'] = False
    elif merkki == pyglet.window.key.DOWN:
        suunta['alas'] = False


def liiku(dt):
    if suunta['ylös'] == True:
        ympyrä.y = ympyrä.y + 10

    if suunta['alas'] == True:
        ympyrä.y = ympyrä.y - 10

pyglet.clock.schedule(liiku)

pyglet.app.run()
```

---

[Tehtävät](tehtävät.md)