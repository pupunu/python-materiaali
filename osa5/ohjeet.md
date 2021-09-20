# Osa 5 - Funktiot

Tähän mennessämme ohjelmamme tekee asioita vain silloin, kun pelaaja painaa nappia. Peleissä kuitenkin tapahtuu usein asioita myös pelaajan tekemättä mitään, esimerkiksi pelaajaa saattaa jahdata vihollinen tai pelikentälle ilmestyy vähän väliä keräiltäviä aarteita. On kuitenkin yksi asia, joka on tärkeä oppia ennen, kun alamme ohjelmoida pelimme itsenäistä toimintaa.

## Mikä on funktio

Funktio saattaa olla koulusta tuttu matematiikantunneilta. Ohjelmoinnissa funktiot ovat kuitenkin hiukan erilaisia.

Onhjelmoinnin funktiot ovat aliohjelmia. Se tarkoittaa, että funktio on kuin ohjelman sisällä oleva pienempi ohjelma, jota voi käyttää muualla ohjelmassa halutessaan. Yleensä funktioita käytetään, kun on jokin asia, joka täytyy tehdä usein.

FUNKTIOKUVA [KOODIA]--> FUNKTIO jne

Ohjelmoidessa funktioita on kahdenlaisia erilaisia. On funktioita, jotka vain tekevät jonkin asian, kuten tulostavat "moi" terminaaliin. Sitten on funktioita, jotka palauttavat jonkin vastauksen.

PALAUTTAVAT FUNKTIOT -KUVA

## Tuttuja funktioita

Olemme tähän mennessä itse asiassa käyttäneet funktioita jo. Esimerkiksi ikkunatapahtumat määritellään funktioiden avulla.

## Milloin käyttää funktiota

Seuraavassa esimerkissä lasketaan viiden ja neljän tulo, johon summataan viiden ja seitsemän osamäärä. Laskun tulos tallennetaan muuttujaan tulos.

```Python3
tulos = 5*4 + 5/7
```

Entä jos haluamme laskea saman laskun monta kertaa, mutta niin että viiden tilalla ovat numerot 1, 4 ja 6? Voimme tietysti tehdä näin:

```Python3
tulos1 = 5*4 + 5/7

tulos2 = 1*4 + 1/7

tulos3 = 43*4 + 43/7

tulos4 = 6*4 + 6/7
```

Tässä koodissa on kuitenkin paljon toistoa ja ainoa mikä siinä muuttuu on viiden paikalla oleva numero. Voisimme siis vaivan säästämiseksi tehdä funktion, jonka avulla voimme laskea laskun.

## Miten luodaan funktio

Funktion luominen on kohtalaisen simppeliä. Aloitamme sanomalla `def`. Se on lyhenne englannin sanasta define eli määrittele. Seuraavaksi kerromme funktion nimen.

Nimen jälkeen merkitsemme sulkuihin millaisia tietoja funktio haluaa. Esimerkkimme laskutoimituksen tarvitsee tietää mikä numero tulee viiden tilalle. Nimetään tätä numeroa vaikkapa x:ksi. Jos funktio ei tarvitse mitään tietoja, laitetaan pelkät tyhjät sulut.

Sulkujen jälkeen tulee kaksoipiste ja sen jälkeen seuraavalle riville voidaan alkaa kirjoittaa mitä funktio tekee.

```Python3
def laskutoimitus(x):
    #tänne tulee koodi siitä mitä laskutoimitus tekee
```

## Funktion palautusarvot

Haluamamme funktio ottaa numeron, jonka haluamme laittaa viiden tilalle alkuperäisessä laskussamme, ja antaa vastaukseksi jonkin toisen numeron. Vastausta kutsutaan palautusarvoksi, koska funktio "palauttaa" sen ohjelmalle, joka funktiota on kutsunut. Pythonissa palautusarvon eteen laitetaan `return` ja sen jälkeen mitä halutaan palauttaa. Return on englantia ja tarkoittaa palauttaa. Se tarkoitta itse asiassa myös palata, ja `return`in jälkeen ei ole pakko antaa palautusarvoa. Tällöin funktion suoritus vain loppuu ja palataan pääohjelmaan.

Koska haluamme, että funktiomme _laskutoimitus_ kertoo ohjelmalle laskutoimituksen tuloksen, määrittelemme funktion seuraavasti:

```Python3
def laskutoimitus(x):
    return x*4 + x/7
```

## Funktion käyttö

Nyt kun olemme määritelleet funktiomme, voimme käyttää sitä. Funktiota käytetään kirjoittamalla sen nimi ja perään sulkuihin mahdolliset funktion haluamat arvot. Jos funktio ei halua arvoja, niin kirjoitetaan pelkät tyhjät sulut.

Nyt voimme kirjoittaa aikaisemman ohjelmamme siistimmin ilman liikaa toistoa:

```Python3
def laskutoimitus(x):
    return x*4 + x/7

tulos1 = laskutoimitus(5)

tulos2 = laskutoimitus(1)

tulos3 = laskutoimitus(43)

tulos4 = laskutoimitus(6)
```
