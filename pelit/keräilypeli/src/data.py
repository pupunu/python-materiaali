import pyglet

# vakiomuuttujat

RED = 255, 0, 0
BLUE = 0, 0, 255
GREEN = 0, 255, 0
WHITE = 255, 255, 255, 255

PELAAJAN_ASKELEET = 200
HEDELMÄ_OSUMAETÄISYYS = 39

PAHIKSEN_ASKELEET = 100
PAHIS_OSUMAETÄISYYS = 79

#piirrettävät hahmot

piirrettävät = pyglet.graphics.Batch()

pelaaja = pyglet.shapes.Circle(x = 100, y = 100, color = BLUE, radius = 40, batch = piirrettävät)

hedelmä = pyglet.shapes.Circle(x = 700, y = 500, color = GREEN, radius = 10, batch = piirrettävät)

pahis = pyglet.shapes.Circle(x = 400, y = 500, color = RED, radius = 40, batch = piirrettävät)

pistetaulu = pyglet.text.Label('Pisteet: 0', batch = piirrettävät, x = 50, y = 550, font_size = 20, color = WHITE)

pelin_lopputeksti = pyglet.text.Label('Peli loppui', x = 400, y = 300, font_size = 30, color = WHITE)

#pelin data

pisteet = 0

liikkuuko = {'ylös':False, 'vasemmalle':False, 'alas':False, 'oikealle':False}