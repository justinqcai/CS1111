#Justin Cai, jc5pz
#ayush mayur, am3nz
import pygame
import gamebox
import random
import time

pygame.init()

gameDisplay = pygame.display.set_mode((800,600))

pygame.display.set_caption('George in the Jungle')

level = 0
cam = gamebox.Camera(800, 600)
monkey = gamebox.from_image(130, 100, "https://bit.ly/2FmzL4Z")
monkey.xspeed = 7
power = False

lvl = gamebox.from_text(cam.x - 280, 20, "Level: " + str(level//10+1), 50, "red")
backgrounds = [
    gamebox.from_image(cam.x + 1296, cam.y, "https://bit.ly/2EcQDcI"), #+1296
    gamebox.from_image(cam.x, cam.y, "https://bit.ly/2EcQDcI"),
    gamebox.from_image(cam.x - 1296, cam.y, "https://bit.ly/2EcQDcI"),
    gamebox.from_image(cam.x - 2592, cam.y, "https://bit.ly/2EcQDcI"),
    gamebox.from_image(cam.x + 2592, cam.y, "https://bit.ly/2EcQDcI"),
]
# for i in range(0,99):
#     backgrounds.append(gamebox.from_image(2592*i, cam.y, "https://bit.ly/2EcQDcI"))
bottom = [
    gamebox.from_image(500, random.randint(-200, -90), "https://bit.ly/2z9SFGs"),
    gamebox.from_image(800, random.randint(-200, -90), "https://bit.ly/2z9SFGs"),
    gamebox.from_image(1100, random.randint(-200, -90), "https://bit.ly/2z9SFGs"),
]
top = [
    #gamebox.from_image(500, random.randint(620, 800), "https://bit.ly/2ROQJtS"),
    gamebox.from_color(500, random.randint(0, 600), "black", 30, random.randint(200,400)),
    gamebox.from_color(800, random.randint(0, 600), "black", 30, random.randint(200,400)),
    gamebox.from_color(1100, random.randint(0, 600), "black", 30, random.randint(200,400)),
    #gamebox.from_image(800, random.randint(620, 800), "https://bit.ly/2ROQJtS"),
    #gamebox.from_image(1100, random.randint(620, 800), "https://bit.ly/2ROQJtS"),
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
count = 1
#current_health = 100
health_bar = gamebox.load_sprite_sheet("https://bit.ly/2DHNJLY", 1, 5)

health_frame = 0
screen = [
    gamebox.from_text(400, 230, "Flappy in the Jungle", 40, "red"),
    gamebox.from_text(400, 270, "Justin Cai and Ayush Mayur, jc5pz, am3nz", 30, "red"),
    gamebox.from_text(400, 300, "Avoid the obstacles by moving the bird with the arrow keys.", 30, "red"),
    gamebox.from_text(400, 330, "Do not touch the edges of the screen.", 30, "red"),
    gamebox.from_text(400, 360, "The number of obstacles progressively increases.", 30, "red"),
    gamebox.from_text(400, 390, "Press space to play.", 30, "red"),
    gamebox.from_text(400, 420, "You pass a level every 10 enemies passed.", 30, "red"),
    gamebox.from_text(400, 450, "Every collision results in loss of 25 health of 100 total.", 30, "red")
]
def tick(keys):
    global level
    global power
    global count
    global health_frame
    global health_bar
    global lvl
    global level
    global screen


    if pygame.K_SPACE in keys:
        power = True
    #monkey.x += 10
    #monkey.yspeed += 1
    # if pygame.K_SPACE in keys:
    #     power = True
    # if not power:
    #     gamebox.pause()
    # else:
    #     gamebox.unpause()
    if level % 10 == 0 and len(top) - 3 == level//10:
        top.append(gamebox.from_color(cam.right + 50, random.randint(0, 600), "black", 30, random.randint(200,400)))
        lvl = gamebox.from_text(cam.x - 280, 20, "Level: " + str(level // 10 + 1), 50, "red")
    health = gamebox.from_image(cam.x - 280, 585, health_bar[health_frame])
    #monkey.y = monkey.y + monkey.yspeed


    if power is False:
        for sc in screen:
            cam.draw(sc)

    if power:
        cam.clear("cyan")
        for bg in backgrounds:
            cam.draw(bg)
        cam.draw(monkey)
        cam.draw(lvl)
           # print(bg.width, bg.height) #2592 1168
            #print(bg.x, cam.x)

        for f in floor:
            if monkey.bottom_touches(f):
                health_frame += 1
                health.image = health_bar[health_frame]
                respawn()
            cam.draw(f)
            f.x += 6
        cam.x += 6
        lvl.x += 6
        for c in ceiling:
            if monkey.top_touches(c):
                health_frame += 1
                health.image = health_bar[health_frame]
                respawn()
            cam.draw(c)
            c.x += 10
        for t in top:
            if monkey.touches(t):
                health_frame += 1
                health.image = health_bar[health_frame]
                respawn()
            cam.draw(t)
            if top.index(t) % 4 == 0:
                t.y -= random.randint(3, 6 + level//15)
                t.x += (3 + level//10)
            elif top.index(t) % 4 == 1:
                t.y += random.randint(3, 6 + level//15)
                t.x -= (3 + level // 10)
            elif top.index(t) % 4 == 2:
                t.y -= random.randint(3, 6 + level//15)
                t.x -= (3 + level//10)
            else:
                t.y += random.randint(3, 6 + level//15)
                t.x += (3+ level //10)
            if t.left < cam.left - 5:
                t.x = cam.right + 50
                t.width = 30
                if top.index(t) %2 ==0:
                    t.y = random.randint(300, 600)
                else:
                    t.y = random.randint(0,300)
                t.height = random.randint(200,400)
                level += 1
        cam.draw(health)
                #print(cam.)
        # for b in bottom:
        #     if monkey.touches(b):
        #         power = False
        #         gamebox.pause()
        #     cam.draw(b)
        #     b.y -= 10
        #     if b.left < cam.left - 5:
        #         b.x = cam.right + 200
        #         b.y = random.randint(-250, -40)
        #         level += 1
        if cam.x > (2592*count):
            count += 1
            backgrounds.append(gamebox.from_image(2592*count+400, cam.y, "https://bit.ly/2EcQDcI"))
        if monkey.x + 400 < cam.x or monkey.x + 400 > cam.x + 800:
            health_frame += 1
            health.image = health_bar[health_frame]
            respawn()

        if pygame.K_UP in keys:
            #monkey.image = walk_right[walk_frame]
            # if walk_frame == 4:
            #     walk_frame = 0
            # walk_frame += 1
            monkey.y -= 7
            #cam.y = monkey.y
            #health.x = monkey.x - 280
            #level.x = monkey.x + 340
            #experience_bar.x = monkey.x

            # if direction == -1:
            #     direction *= -1
            # else:
            #     direction *= 1
        if pygame.K_DOWN in keys:
            monkey.y += 7
        if pygame.K_LEFT in keys:
            monkey.x -= 15
            #cam.x = monkey.x
        if pygame.K_RIGHT in keys:
            monkey.x += 15
            #cam.x = monkey.x
    if health_frame == 4:
        cam.draw(gamebox.from_text(cam.x, cam.y, "Sorry! Score: " + str(level), 70, "red"))
        power = False
        gamebox.pause()
    cam.display()

def respawn():
    global power
    global top
    monkey.x = cam.x - 270
    monkey.y = 300
    power = False
    for t in top:
        #top.append(gamebox.from_color(cam.right + 200, random.randint(0, 600), "black", 30, random.randint(200,400)))
        t.x = random.randint(cam.right+50, cam.right + 250)
        if top.index(t) % 2 == 0:
            t.y = random.randint(300, 600)
        else:
            t.y = random.randint(0, 300)
    # for t in top:
    #     t.speedx = 0
    #     t.speedy = 0
    now = time.time()
    cam.clear("cyan")
    while time.time() < now + 1:
        cam.draw(gamebox.from_text(cam.x, 300, "3", 50, "red"))
    cam.clear("cyan")
    while time.time() < now + 2:
        cam.draw(gamebox.from_text(cam.x, 300, "2", 50, "red"))
    cam.clear("cyan")
    while time.time() < now + 3:
        cam.draw(gamebox.from_text(cam.x, 300, "1", 50, "red"))
    cam.clear("cyan")
    power = True
    # for t in top:
    #     if top.index(t) % 2 == 0:
    #         t.speedy = -5
    #     else:
    #         t.speedy = 5



ticks_per_second = 30
gamebox.timer_loop(ticks_per_second, tick)

