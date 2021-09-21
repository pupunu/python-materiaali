import pyglet

ikkuna = pyglet.window.Window(width = 800, height = 600)
ympyrä = pyglet.shapes.Circle(x = 400, y = 300, radius = 100, color = (255, 0, 0))

@ikkuna.event
def on_draw():
	ikkuna.clear()
	ympyrä.draw()

@ikkuna.event
def on_key_press(merkki, muuntaja):
    if merkki == pyglet.window.key.P:
        ympyrä.color = 255, 0, 0
    else:
        ympyrä.color = 0, 0, 255

@ikkuna.event
def on_key_release(merkki, muuntaja):
	ympyrä.color = 255, 255, 255

def diskopallo(dt):
    if ympyrä.color == (255, 0, 0):
        ympyrä.color = 0, 255, 0
    elif ympyrä.color == (0, 255, 0):
        ympyrä.color = 0, 0, 255
    elif ympyrä.color == (0, 0, 255):
        ympyrä.color = 255, 0, 0 
    else:
        ympyrä.color = 255, 0, 0

pyglet.clock.schedule_interval(diskopallo, 1)

pyglet.app.run()
