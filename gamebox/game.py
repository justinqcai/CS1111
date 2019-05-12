import pygame as pg
import gamebox as gb
import random

##############################################
# Checkpoint 1

# Here we have a side-scroll type game, where it has hints from multiple different games. We already designed a majority
# of the game as seen below, it all should work on any computer except for the music (going to figure out how to
# upload that to be used externally but we'll see if that's possible. The premise of the game is a character has levels,
# experience, and a weapon to go through different rooms. The first room is what we have so far—a woods-type room, with
# the skeleton as the enemy. Every kill is 10 exp, 50 exp to level up, and each room is 3 levels. 1-3 is woods, 3-6 is
# TBD, 6-9 is TBD, and 10 is a boss that will award 50 exp and will cause an end-game win (like Bowser, if you want
# to relate this to mario. So far we have user input (up arrow, right arrow, left arrow, space, and will soon have e
# for equipment [potions, maybe?]). Graphics are seen. Start screen is implemented but hidden until we finish the
# entirety of the game. "Small enough window" is used. As for optional features, we implemented a multitude of
# animations, we will have different (moving) enemies that will hit and can be hit. Collectibles we will have but have
# not determined, possibly potions for health or coins for extra exp. The level scrolls. We might implement a timer
# so as that you must finish each room in time. Health meter is implemented. There will be multiple levels. We might
# do a save point, but we have to discuss that and debate on whether it is useful. Not sure if anything we've done
# so far constitutes as "something more" but we've got a pretty robust code thus far.

# Checkpoint 2

# I finally got to speak to Luther today, he explained to me how to fix the few bugs we have. We couldn't figure out
# how to physically hit the monsters from a distance, fix their flip() movement, and fix the animations
# (pressing one button to go through an entire animation). As of now those are our only bugs. Once we complete that we
# will quickly finish the levels portion, and then add collectibles and possible a save point. The game is nearly
# complete and should be done by this Sunday (December 2). 

#############################################


pg.mixer.pre_init(44100, 16, 2, 4096)
pg.init()

#background_music = "/Users/jacobsadeh/Downloads/python_story/python_music.wav"
#hit_sound = "/Users/jacobsadeh/Downloads/python_story/Hit.wav"
#pg.mixer.music.load(background_music)
#pg.mixer.music.set_volume(.7)
#pg.mixer.music.play(-1)

camera = gb.Camera(800, 600)

game = "on"

start_screen = gb.from_image(camera.x, camera.y, "https://bit.ly/2r9i2UJ")

stand_right = gb.load_sprite_sheet("https://bit.ly/2RbNzAH", 4, 1)

walk_right = gb.load_sprite_sheet("https://bit.ly/2An2tg4", 5, 1)

walk_left = gb.load_sprite_sheet("https://bit.ly/2r5hWNI", 5, 1)

hit_right = gb.load_sprite_sheet("https://bit.ly/2Racwwk", 3, 2)

jump_right = gb.load_sprite_sheet("https://bit.ly/2qZcVpY", 2, 1)

hit_left = gb.load_sprite_sheet("https://bit.ly/2QpqKMR", 3, 2)

stand_left = gb.load_sprite_sheet("https://bit.ly/2PR6UdD", 4, 1)

jump_left = gb.load_sprite_sheet("https://bit.ly/2Bukwme", 2, 1)

stand_frame = 0
walk_frame = 0
hit_frame = 0
jump_frame = 0
frame = 0


character = gb.from_image(camera.x, 540, stand_right[frame])

floor_design = "https://bit.ly/2Kp4VaJ" 

floors = [
    gb.from_image(120, 615, floor_design),
    gb.from_image(570, 615, floor_design),
    gb.from_image(1020, 615, floor_design),
    gb.from_image(1470, 615, floor_design),
    gb.from_image(-330, 615, floor_design),
    gb.from_image(-780, 615, floor_design),
    gb.from_image(-1230, 615, floor_design),
    gb.from_image(-1680, 615, floor_design),
    gb.from_image(-2130, 615, floor_design),
    gb.from_image(-2580, 615, floor_design),
    gb.from_image(1920, 615, floor_design),
    gb.from_image(2370, 615, floor_design),
    gb.from_image(2580, 615, floor_design),
    gb.from_image(300, 350, floor_design),
    gb.from_image(-300, 150, floor_design),
    gb.from_image(-500, 400, floor_design),
    gb.from_image(900, 400, floor_design),
    gb.from_image(1200, 150, floor_design),
    gb.from_image(1700, 250, floor_design),
    gb.from_image(2580, 615, floor_design),
    gb.from_image(2580, 615, floor_design),

]

background_design = "https://bit.ly/2PPmOVO"

backgrounds = [
    gb.from_image(camera.x + 1309, camera.y, background_design),
    gb.from_image(camera.x, camera.y, background_design),
    gb.from_image(camera.x - 1310.4, camera.y, background_design),
    gb.from_image(camera.x - 2620.3, camera.y, background_design),
    gb.from_image(camera.x + 2620.3, camera.y, background_design),
]

skeletrooper_walk = gb.load_sprite_sheet("https://bit.ly/2OT1B8l", 4, 1)
skeletrooper_die = gb.load_sprite_sheet("https://i.imgur.com/40K6PdH.png", 2, 6)
skeletrooper_hit = gb.load_sprite_sheet("https://bit.ly/2r0a0ND", 1, 1)
skeletrooper_attack = gb.load_sprite_sheet("https://i.imgur.com/WlGsUa2.png", 1, 6)

skeletrooper = gb.from_image(500, 255, skeletrooper_walk[0])
skeletrooper_1 = gb.from_image(-100, 55, skeletrooper_walk[0])
skeletrooper_2 = gb.from_image(-300, 305, skeletrooper_walk[0])
skeletrooper_3 = gb.from_image(1100, 305, skeletrooper_walk[0])
skeletrooper_4 = gb.from_image(1400, 55, skeletrooper_walk[0])
skeletrooper_5 = gb.from_image(1900, 155, skeletrooper_walk[0])

health_bar = gb.load_sprite_sheet("https://bit.ly/2DHNJLY", 1, 5)

health_frame = 0

health = gb.from_image(camera.x - 280, 585, health_bar[health_frame])

levels = 1

exp = 0

if exp == 50:
    levels += 1
    exp = 0

level = gb.from_text(camera.x + 340, 585, "Lvl " + str(levels), 30, "gold")

experience_bar = gb.from_text(camera.x, 587, "Exp: " + str(exp) + "/50", 30, "yellow")

direction = 1

skeletrooper_health = 30

ticktick = 0

character.yspeed = 0

mspeed=5
mpos1=100


def tick(keys):
    global game, character, frame, hit_sound, background_music, health_frame, direction, skeletrooper_health
    global stand_frame, walk_frame, hit_frame, jump_frame, level, levels, exp, ticktick
    global frame
    global mspeed, skeletrooper_1, skeletrooper, skeletrooper_2, skeletrooper_3, skeletrooper_4, skeletrooper_5

    character.yspeed += 5
    character.y = character.y + character.yspeed

    if character.x >= 2365:
        character.x -= 10

    if character.x <= -1570:
        character.x += 10
    frame += 1
    if frame == 2:
        frame = 0

    camera.draw(start_screen)

    if pg.K_s in keys:
        game = "on"

    if health_frame == 4:
        game = "die"

    if game == "die":
        camera.clear("white")
        camera.draw(gb.from_text(camera.x, camera.y, "Oof, dead", 70, "red"))
        #pg.mixer.music.load(hit_sound)
        #pg.mixer.music.set_volume(.7)
        #pg.mixer.music.play()

        gb.pause()

    if game == "on":
        camera.clear("White")
        camera.draw(character)
        for background in backgrounds:
            camera.draw(background)
            print(background.x, camera.x)

        for floor in floors:
            if character.bottom_touches(floor):
                character.yspeed = 0
                if pg.K_UP in keys:  # if up is pressed, jump
                    if direction == -1:
                        character.image = jump_left[frame]
                    else:
                        character.image = jump_right[frame]
                    character.yspeed = -55

            if character.touches(floor):
                character.move_to_stop_overlapping(floor)
            if skeletrooper.touches(floor):
                skeletrooper.move_to_stop_overlapping(floor)

            camera.draw(floor)

        # skeletrooper.image = skeletrooper_walk[frame]
        # skeletrooper_1.image = skeletrooper_walk[frame]
        # skeletrooper_2.image = skeletrooper_walk[frame]
        # skeletrooper_3.image = skeletrooper_walk[frame]
        # skeletrooper_4.image = skeletrooper_walk[frame]
        # skeletrooper_5.image = skeletrooper_walk[frame]
        # camera.draw(skeletrooper)
        # camera.draw(skeletrooper_1)
        # camera.draw(skeletrooper_2)
        # camera.draw(skeletrooper_3)
        # camera.draw(skeletrooper_4)
        # camera.draw(skeletrooper_5)
        # Chunk of code between the hash lines does the same as above

        ################################################################################################
        sklist=[skeletrooper, skeletrooper_1, skeletrooper_2, skeletrooper_3, skeletrooper_4, skeletrooper_5]
        for trooper in sklist:
            trooper.image = skeletrooper_walk[frame]
            camera.draw(trooper)
        ################################################################################################
        skeletrooper.x -= mspeed
        if skeletrooper.x <= 100 or skeletrooper.x >= 500:
            mspeed = -mspeed
            skeletrooper.flip()

        skeletrooper_1.x -= mspeed
        if skeletrooper_1.x <= -500 or skeletrooper_1.x >= -100:
            skeletrooper_1.flip()
            mspeed = -mspeed

        skeletrooper_2.x -= mspeed
        if skeletrooper_2.x <= -700 or skeletrooper_2.x >= -300:
            mspeed = -mspeed

        skeletrooper_3.x -= mspeed
        if skeletrooper_3.x <= 700 or skeletrooper_3.x >= 1100:
            mspeed = -mspeed
            skeletrooper_3.flip()

        skeletrooper_4.x -= mspeed
        if skeletrooper_4.x <= 1000 or skeletrooper_4.x >= 1400:
            mspeed = -mspeed
            skeletrooper_4.flip()

        skeletrooper_5.x -= mspeed
        if skeletrooper_5.x <= 1500 or skeletrooper_5.x >= 1900:
            mspeed = -mspeed
            skeletrooper_5.flip()






        if character.touches(skeletrooper) or character.touches(skeletrooper_1) or character.touches(skeletrooper_2):
            health_frame += 1
            health.image = health_bar[health_frame]
            character.move_to_stop_overlapping(skeletrooper)
            character.move_to_stop_overlapping(skeletrooper_1)
            character.move_to_stop_overlapping(skeletrooper_2)

        if character.touches(skeletrooper_3) or character.touches(skeletrooper_4) or character.touches(skeletrooper_5):
            health_frame += 1
            health.image = health_bar[health_frame]
            character.move_to_stop_overlapping(skeletrooper_3)
            character.move_to_stop_overlapping(skeletrooper_4)
            character.move_to_stop_overlapping(skeletrooper_5)


        if pg.K_RIGHT in keys:
            character.image = walk_right[walk_frame]
            if walk_frame == 4:
                walk_frame = 0
            walk_frame += 1
            character.x += 10
            camera.x = character.x
            health.x = character.x - 280
            level.x = character.x + 340
            experience_bar.x = character.x

            if direction == -1:
                direction *= -1
            else:
                direction *= 1

        elif pg.K_LEFT in keys:
            character.image = walk_left[walk_frame]
            if walk_frame == 4:
                walk_frame = 0
            walk_frame += 1
            character.x -= 10
            camera.x = character.x
            health.x = character.x - 280
            level.x = character.x + 340
            experience_bar.x = character.x
            if direction == -1:
                direction *= 1
            else:
                direction *= -1

        elif pg.K_SPACE in keys:
            if direction == -1:
                #for loop
                #continously delete then reupdate character gamebox using character.x
                if character.touches(skeletrooper, 100, 100):
                    character.image = hit_left[hit_frame]
                    skeletrooper_health -= 10
                    if hit_frame == 3:
                        hit_frame = 0
                    hit_frame += 1
                else:
                    character.image = hit_left[hit_frame]

                    if hit_frame == 3:
                        hit_frame = 0
                    hit_frame += 1
            elif direction == 1:
                if character.touches(skeletrooper, 100, 100):
                    character.image = hit_right[hit_frame]
                    if hit_frame == 3:
                        hit_frame = 0
                    hit_frame += 1
                    skeletrooper_health -= 10
                else:
                    character.image = hit_right[hit_frame]
                    if hit_frame == 3:
                        hit_frame = 0
                    hit_frame += 1

        elif direction == -1:
            character.image = stand_left[0-4]

        else:
            character.image = stand_right[0-4]

        if skeletrooper_health <= 0:
            skeletrooper.image = skeletrooper_die[6]
            if exp == 50:
                levels += 1
                camera.draw(gb.from_text(camera.x + 340, 585, "Lvl " + str(levels), 30, "gold"))
                exp = 0
            exp += 10
            camera.draw(gb.from_text(camera.x, 587, "Exp: " + str(exp) + "/50", 30, "yellow"))
            pass
        else:
            camera.draw(gb.from_text(camera.x, 587, "Exp: " + str(exp) + "/50", 30, "yellow"))
            camera.draw(gb.from_text(camera.x + 340, 585, "Lvl " + str(levels), 30, "gold"))

        camera.draw(character)
        camera.draw(health)
        camera.draw(level)
    camera.display()


ticks_per_second = 30

gb.timer_loop(ticks_per_second, tick)