import pyglet
from data import *
import random

def nappia_painaessa(merkki):
    global liikkuuko
    if merkki == pyglet.window.key.W:
        liikkuuko['ylös'] = True
    elif merkki == pyglet.window.key.A:
        liikkuuko['vasemmalle'] = True
    elif merkki == pyglet.window.key.S:
        liikkuuko['alas'] = True
    elif merkki == pyglet.window.key.D:
        liikkuuko['oikealle'] = True

def napin_painamisen_loppuessa(merkki):
    global liikkuuko
    if merkki == pyglet.window.key.W:
        liikkuuko['ylös'] = False
    elif merkki == pyglet.window.key.A:
        liikkuuko['vasemmalle'] = False
    elif merkki == pyglet.window.key.S:
        liikkuuko['alas'] = False
    elif merkki == pyglet.window.key.D:
        liikkuuko['oikealle'] = False

def liiku(dt):
    if liikkuuko['ylös']:
        pelaaja.y += PELAAJAN_ASKELEET*dt
    if liikkuuko['vasemmalle']:
        pelaaja.x -= PELAAJAN_ASKELEET*dt
    if liikkuuko['alas']:
        pelaaja.y -= PELAAJAN_ASKELEET*dt
    if liikkuuko['oikealle']:
        pelaaja.x += PELAAJAN_ASKELEET*dt

def pahiksen_liikkuminen(dt):
    if pelaaja.x > pahis.x:
        pahis.x += PAHIKSEN_ASKELEET*dt
    else:
        pahis.x -= PAHIKSEN_ASKELEET*dt
    if pelaaja.y > pahis.y:
        pahis.y += PAHIKSEN_ASKELEET*dt
    else:
        pahis.y -= PAHIKSEN_ASKELEET*dt

def keräilyn_tarkistus(_):
    global pisteet
    if abs(pelaaja.x - hedelmä.x)**2 + abs(pelaaja.y - hedelmä.y)**2 <= HEDELMÄ_OSUMAETÄISYYS**2:
        while abs(pelaaja.x - hedelmä.x)**2 + abs(pelaaja.y - hedelmä.y)**2 <= HEDELMÄ_OSUMAETÄISYYS**2:
            hedelmä.x = random.randint(0, 800)
            hedelmä.y = random.randint(0, 600)
        pisteet += 1
        pistetaulu.text = 'Pisteet: ' + str(pisteet)

def pahiksen_osuman_tarkistus(_):
    if abs(pelaaja.x - pahis.x)**2 + abs(pelaaja.y - pahis.y)**2 <= PAHIS_OSUMAETÄISYYS**2:
        pelin_lopputeksti.batch = piirrettävät
        pyglet.clock.unschedule(liiku)
        pyglet.clock.unschedule(pahiksen_liikkuminen)
