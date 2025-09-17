from pico2d import *
import math

open_canvas()

grass = load_image('grass.png')
character = load_image('character.png')

while True:
    # 1. 네모 경로 (시작점: 400, 90)
    x, y = 400, 90
    # 오른쪽으로 이동 (400,90) -> (800,90)
    while x < 800:
        clear_canvas_now()
        grass.draw_now(400, 30)
        character.draw_now(x, y)
        x += 2
        delay(0.001)
    # 위로 이동 (800,90) -> (800,600)
    while y < 600:
        clear_canvas_now()
        grass.draw_now(400, 30)
        character.draw_now(x, y)
        y += 2
        delay(0.001)
    # 왼쪽으로 이동 (800,600) -> (0,600)
    while x > 0:
        clear_canvas_now()
        grass.draw_now(400, 30)
        character.draw_now(x, y)
        x -= 2
        delay(0.001)
    # 아래로 이동 (0,600) -> (0,90)
    while y > 90:
        clear_canvas_now()
        grass.draw_now(400, 30)
        character.draw_now(x, y)
        y -= 2
        delay(0.001)
    # 오른쪽으로 이동해서 시작점으로 복귀 (0,90) -> (400,90)
    while x < 400:
        clear_canvas_now()
        grass.draw_now(400, 30)
        character.draw_now(x, y)
        x += 2
        delay(0.001)
    # 2. 원 그리기 (중심: 400, 300, 반지름: 210)
    cx, cy, r = 400, 300, 210
    for degree in range(0, 360, 2):
        clear_canvas_now()
        grass.draw_now(400, 30)
        rad = math.radians(degree)
        ox = int(cx + r * math.cos(rad))
        oy = int(cy + r * math.sin(rad))
        character.draw_now(ox, oy)
        delay(0.001)
#
    # 원이 끝나면 다시 네모 경로 반복

close_canvas()