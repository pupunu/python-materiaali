import pyglet

ikkuna = pyglet.window.Window(width = 800, height = 600)
ikkuna.clear()	

@ikkuna.event
def on_draw():
    pyglet.shapes.Circle(x = 400, y = 300, radius = 100).draw()

pyglet.app.run()
