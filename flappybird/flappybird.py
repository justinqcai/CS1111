#Justin Cai, jc5pz

import pygame
import gamebox
import random

level = 0
cam = gamebox.Camera(800, 600)
bird = gamebox.from_image(130, 100, "https://bit.ly/2FmzL4Z")
bird.xspeed = 7
power = True

bottom = [
    gamebox.from_image(500, random.randint(-200, -60), "https://bit.ly/2z9SFGs"),
    gamebox.from_image(800, random.randint(-200, -60), "https://bit.ly/2z9SFGs"),
    gamebox.from_image(1100, random.randint(-200, -60), "https://bit.ly/2z9SFGs"),
]
top = [
    gamebox.from_image(500, random.randint(620, 800), "https://bit.ly/2ROQJtS"),
    gamebox.from_image(800, random.randint(620, 800), "https://bit.ly/2ROQJtS"),
    gamebox.from_image(1100, random.randint(620, 800), "https://bit.ly/2ROQJtS"),
]
floor = [
    gamebox.from_image(120, 615, "https://bit.ly/2FjBlo3"),
    gamebox.from_image(400, 615, "https://bit.ly/2FjBlo3"),
    gamebox.from_image(650, 615, "https://bit.ly/2FjBlo3")
]
ceiling = [
    gamebox.from_image(120, -70, "https://bit.ly/2FjBlo3"),
    gamebox.from_image(400, -70, "https://bit.ly/2FjBlo3"),
    gamebox.from_image(650, -70, "https://bit.ly/2FjBlo3"),
]

def tick(keys):
    global level
    global power
    if pygame.K_SPACE in keys:
        bird.speedy = -8
    bird.x += 7
    bird.yspeed += 1
    bird.y = bird.y + bird.yspeed
    cam.clear("cyan")
    cam.draw(bird)
    for f in floor:
        if bird.bottom_touches(f):
            power = False
            gamebox.pause()
        cam.draw(f)
        f.x += 7
    cam.x += 7
    for c in ceiling:
        if bird.touches(c):
            power = False
            gamebox.pause()
        cam.draw(c)
        c.x += 7
    for t in top:
        if bird.touches(t):
            power = False
            gamebox.pause()
        cam.draw(t)
        if t.left < cam.left - 5:
            t.x = cam.right + 200
            t.y = random.randint(620, 800)
    for b in bottom:
        if bird.touches(b):
            power = False
            gamebox.pause()
        cam.draw(b)
        if b.left < cam.left - 5:
            b.x = cam.right + 200
            b.y = random.randint(-250, -40)
            level += 1
    if not power:
        cam.draw(gamebox.from_text(cam.x, cam.y, "Sorry! Score: " + str(level), 70, "red"))
        gamebox.pause()
    cam.display()

ticks_per_second = 30
gamebox.timer_loop(ticks_per_second, tick)