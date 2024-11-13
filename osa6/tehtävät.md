# Osa 6 - Koordinaatit - Tehtävät

1. Tarvitset jokaisessa tehtävässä ohjelmaa, jolla on ikkuna. Ikkunan koon tulee olla leveydeltään 800 ja korkeudeltaan 600, ja siihen piirretään ympyrä. Ohjelmoi kyseinen ohjelma.


2. Ohjelmoi seuraavat asiat edellisen tehtävän ohjelmaan juuri ennen koodia `pyglet.app.run()`.

a) Käynnistä ohjelma ja katso missä ympyrä sijaitsee.

b) Kirjoita nyt ohjelmaan `ympyrä.x = 100` ja käynnistä se uudestaan. Mitä tapahtuu? Entä jos koodinpätkä on toisessa kohtaa koodia, vaikuttaako se ohjelmaan?

c) Korvaa äsken lisäämäsi koodi. Kirjoita sen tilalle `ympyrä.x = 800`. Käynnistä ohjelma uudelleen. Mitä tapahtuu?

d) Lisää koodi `ympyrä.y = 50`. Käynnistä ohjelma uudelleen ja tutki mitä tapahtuu.


3. Käytä ohjelmaa, jonka teit tehtävässä yksi.

Ohjelmassasi luodaan ympyrä luultavasti jollain suunnilleen tämän näköisellä koodilla:

`ympyrä = pyglet.shapes.Circle(x = 400, y = 300, radius = 100)`

Kokeile nyt muokata tässä koodissa olevia kohtia `x = 400` ja `y = 300`.

a) Muokkaa koodia niin, että ympyrä on aivan vasemmassa reunassa.

b) Muokkaa koodia niin, että ympyrä on aivan yläreunassa.

c) Muokkaa koodia niin, että ympyrä on aivan oikeassa alareunassa.


4. Seuraavaksi hyödynnämme aikaisemmin opittuja ikkunatapahtumia. Voit lisätä nämä haluamaasi ohjelmaan.

a) Ohjelmassa ympyrä liikkuu aivan yläreunaan painamalla nuoliylösnäppäintä. Pygletissä näppäimen nimi on `pyglet.window.key.UP`.
b) Lisäksi ohjelmassa ympyrä liikkuu aivan alareunaan painamalla nuolialasnäppäintä. Näppäimen nimi on `pyglet.window.key.DOWN`.
c) Muuta ohjelma sellaiseksi, että napinpainallukset siirtävät ympyrää ylemmäs ja alemmas. Nyt ympyrää pitäisi pystyä ohjaamaan pystysuunnassa näpyttämällä ylös- ja alasnäppäimiä.
