import pyglet

ikkuna = pyglet.window.Window(width = 800, height = 600)
ympyrä = pyglet.shapes.Circle(x = 40, y = 40, radius = 10)

ta = False

@ikkuna.event
def on_draw():
    ikkuna.clear()
    ympyrä.draw()

@ikkuna.event
def on_key_press(merkki, muuntaja):
    global ta
    ta = not ta
    
@ikkuna.event
def on_key_release(merkki, muuntaja):
    global ta
    ta = not ta

def liiku(dt):
    if ta:
        ympyrä.x += 1



pyglet.clock.schedule(liiku)

pyglet.app.run()