lisää pyglet

ikkuna = pyglet.ikkuna.Ikkuna(leveys = 800, korkeus = 600)
ympyrä = pyglet.muodot.Ympyrä(x = 400, y = 300, säde = 100)

@ikkuna.tapahtuma
määritä piirtäessä():
    ikkuna.puhdista()
    ympyrä.piirrä()

pyglet.sovellus.suorita()

