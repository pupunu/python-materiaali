import pyglet
import logiikka
import data

ikkuna = pyglet.window.Window(width = 800, height = 600, caption = 'Keräilypeli')

@ikkuna.event
def on_draw():
    ikkuna.clear()
    data.piirrettävät.draw()

@ikkuna.event
def on_key_press(merkki, muuntaja):
    logiikka.nappia_painaessa(merkki)

@ikkuna.event
def on_key_release(merkki, muuntaja):
    logiikka.napin_painamisen_loppuessa(merkki)

pyglet.clock.schedule(logiikka.liiku)
pyglet.clock.schedule(logiikka.keräilyn_tarkistus)
pyglet.clock.schedule(logiikka.pahiksen_osuman_tarkistus)
pyglet.clock.schedule(logiikka.pahiksen_liikkuminen)

pyglet.app.run()