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



ehtolauseista:

Tutustutaan niihin hiukan paremmin tutkimalla seuraavaa leikkikoodia:

![joslauseita](kuvat/pelkkäjos.png)

Tämä koodi ensin tarkistaa onko tiikeri hedelmä. Tämä ei ole totta joten se siirtyy seuraavaan koodiin, jossa se testaa onko tiikeri huonekalu. Tämäkään ei ole totta joten koodi ei tee mitään.

Sen sijaan seuraava leikkikoodi tekee jotain:

![else-lause](kuvat/muussatapauksessa.png)

Tämä koodi ensin tarkistaa onko tiikeri hedelmä. Tämä ei ole totta joten koodissa siirrytään eteenpäin. _Muussa tapauksessa_ toteutuu jos yksikään aiempi ehto ei ole toteutunut. Koska tiikeri ei ollut hedelmä, kyseessä on muu tapaus, joten ohjelma sanoo räyr.

Tutkitaan vielä hiukan monimutkaisempaa ehtojen ketjua:

![if, elif ja else](kuvat/kaikkiehdot)

Tämä koodi ensin tarkistaa onko tiikeri hedelmä, 




## Erilaisia näppäimiä ja erilaisia värejä

Tehdään seuraavaksi niin, että ympyrä muuttuu punaiseksi jos painetaan P:tä, siniseksi jos painetaan S:ää ja vihreäksi jos painetaan V:tä.

Voisimme lisätä koodiin lisää if-komentoja, mutta on tyylikkäämpää tehdä se elif-komennoilla. 



## Erilaisia ehtolauseita

Ehtolauseita on kolmenlaisia: `if`, `elif` ja `else`. Suomeksi ne tarkoittavat kutakuinkin `jos`, `tai jos` ja `muussa tapauksessa`.

Tutkin hiukan lähemmin miten nämä ehtolauseet toimivat:

<img src=kuvat/joslauseet.png height="500">

Tässä on leikkikoodi, jossa ensin tarkistetaan onko tiikeri eläin ja sitten tarkistetaan onko tiikeri oranssi. Ohjelma tarkistaa ensin ensimmäisen jos-lauseen ja sen ollessa totta, se sanoo "eläimellistä touhua". Sitten tietokone etenee seuraavaan jos-lauseeseen, jonka ollessa totta, ohjelma sanoo "appelsiinkin kaltainen".

<img src=kuvat/jostai.png height="500">

Tässä koodissa on tärkeää huomata, että toinen ehtolause ei ole jos-lause vaan tai jos -lause. Tai jos -lause käsitellään vain jos sitä edeltävä jos-lause ja "tai jos"-lauseet eivät ole totta. Koska ensimmäinen jos-lause on totta, tietokone hyppää tai jos -lauseen yli kokonaan ja sanoo ainoastaan "eläimellistä touhua".

<img src=kuvat/ööh.png height="500">

Tässä koodissa on muussa tapauksessa -lause. Muussa tapauksessa -lause käsitellään vain jos sitä edeltävä jos-lause ja "tai jos"-lauseet eivät ole totta.
Tietokone tarkistaa ensin onko tiikeri kasvi. Koska tämä ei ole totta se testaa seuraavaksi, että olisiko tiikeri sittenkin huonekalu. Koska tämäkään ei ole totta, tietokone lopulta päätyy muussa tapauksessa -lauseeseen ja sanoo siis loppujen lopuksi ainoastaan "ööh".

<img src=kuvat/eläimellistämenoa.png height="500">

Tämä koodi on hyvin samanlainen kuin edellinen, mutta nyt toisena tuleva tai jos -lause onkin totta, joten tietokone sanoo sen kohdalla "eläimellistä menoa" ja sen jälkeen hyppää muussa tapauksessa -lauseen yli.