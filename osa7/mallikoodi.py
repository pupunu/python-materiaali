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