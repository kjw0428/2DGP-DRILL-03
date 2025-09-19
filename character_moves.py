from pico2d import *
import math

open_canvas()

grass = load_image('grass.png')
character = load_image('character.png')

while True:
    x, y = 400, 90
    while x < 800:
        clear_canvas_now()
        grass.draw_now(400, 30)
        character.draw_now(x, y)
        x += 2
        delay(0.01)
    while y < 600:
        clear_canvas_now()
        grass.draw_now(400, 30)
        character.draw_now(x, y)
        y += 2
        delay(0.01)
    while x > 0:
        clear_canvas_now()
        grass.draw_now(400, 30)
        character.draw_now(x, y)
        x -= 2
        delay(0.01)
    while y > 90:
        clear_canvas_now()
        grass.draw_now(400, 30)
        character.draw_now(x, y)
        y -= 2
        delay(0.01)
    while x < 400:
        clear_canvas_now()
        grass.draw_now(400, 30)
        character.draw_now(x, y)
        x += 2
        delay(0.01)
    ax, ay = 400, 90
    bx, by = 150, 400
    cx, cy = 650, 400
    steps = 150
    for i in range(steps):
        t = i / steps
        x = int(ax + (bx - ax) * t)
        y = int(ay + (by - ay) * t)
        clear_canvas_now()
        grass.draw_now(400, 30)
        character.draw_now(x, y)
        delay(0.01)
    for i in range(steps):
        t = i / steps
        x = int(bx + (cx - bx) * t)
        y = int(by + (cy - by) * t)
        clear_canvas_now()
        grass.draw_now(400, 30)
        character.draw_now(x, y)
        delay(0.01)
    for i in range(steps):
        t = i / steps
        x = int(cx + (ax - cx) * t)
        y = int(cy + (ay - cy) * t)
        clear_canvas_now()
        grass.draw_now(400, 30)
        character.draw_now(x, y)
        delay(0.01)
    cx, cy, r = 400, 300, 210
    for degree in range(0, 360, 2):
        clear_canvas_now()
        grass.draw_now(400, 30)
        rad = math.radians(degree)
        ox = int(cx + r * math.cos(-1 * rad))
        oy = int(cy + r * math.sin(-1 * rad))
        character.draw_now(ox, oy)
        delay(0.01)

close_canvas()