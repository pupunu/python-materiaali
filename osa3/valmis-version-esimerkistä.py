import pyglet

ikkuna = pyglet.window.Window(width = 800, height = 600)
ympyrä = pyglet.shapes.Circle(x = 400, y = 300, radius = 100)

@ikkuna.event
def on_draw():
    ikkuna.clear()
    ympyrä.draw()

@ikkuna.event
def on_key_press(merkki, muuntaja):
    ympyrä.color = 255, 0, 0

@ikkuna.event
def on_key_release(merkki, muuntaja):
    ympyrä.color = 255, 255, 255

pyglet.app.run()
