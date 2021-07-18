import pyglet

ikkuna = pyglet.window.Window(width = 800, height = 600)
ympyrä = pyglet.shapes.Circle(x = 400, y = 300, radius = 100)

@ikkuna.event
def on_draw():
    ikkuna.clear()	
    ympyrä.draw()

pyglet.app.run()
