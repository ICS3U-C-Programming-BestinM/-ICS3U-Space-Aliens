#!/usr/bin/env python3

# Created by: bestin
# Created on: Jan 2025
# RST 08: Splash Scene and Random Backgrounds

import ugame
import stage
import time
import random

import constants

def splash_scene():
    # this function is the splash scene (intro)
    
    # get image for the splash scene
    image_bank_mt_background = stage.Bank.from_bmp16("mt_game_studio.bmp")
    background = stage.Grid(image_bank_mt_background, constants.SCREEN_GRID_X, constants.SCREEN_GRID_Y)

    # create a stage for the background
    game = stage.Stage(ugame.display, constants.FPS)
    game.layers = [background]
    game.render_block()

    # Wait for 2 seconds
    time.sleep(2.0)
    menu_scene()

def menu_scene():
    # this function is the menu scene
    image_bank_mt_background = stage.Bank.from_bmp16("mt_game_studio.bmp")

    texts = []
    text1 = stage.Text(width=29, height=12, font=None, palette=constants.RED_PALETTE, buffer=None)
    text1.move(20, 10)
    text1.text("MT Game Studios")
    texts.append(text1)

    text2 = stage.Text(width=29, height=12, font=None, palette=constants.RED_PALETTE, buffer=None)
    text2.move(40, 110)
    text2.text("PRESS START")
    texts.append(text2)

    background = stage.Grid(image_bank_mt_background, constants.SCREEN_GRID_X, constants.SCREEN_GRID_Y)

    game = stage.Stage(ugame.display, constants.FPS)
    game.layers = texts + [background]
    game.render_block()

    while True:
        keys = ugame.buttons.get_pressed()
        if keys & ugame.K_START:
            game_scene()
        game.tick()

def game_scene():
    # this function is the main game scene
    
    # setup random background
    image_bank_background = stage.Bank.from_bmp16("space_aliens_background.bmp")
    image_bank_sprites = stage.Bank.from_bmp16("space_aliens.bmp")

    # Create the grid and fill it with random tiles (0-2) from the bank
    background = stage.Grid(image_bank_background, constants.SCREEN_GRID_X, constants.SCREEN_GRID_Y)
    for x_location in range(constants.SCREEN_GRID_X):
        for y_location in range(constants.SCREEN_GRID_Y):
            tile_picked = random.randint(0, 3)
            background.tile(x_location, y_location, tile_picked)

    a_button = constants.button_state["button_up"]
    pew_sound = open("pew.wav", 'rb')
    sound = ugame.audio
    sound.stop()
    sound.mute(False)

    ship = stage.Sprite(image_bank_sprites, 5, 75, constants.SCREEN_Y - (2 * constants.SPRITE_SIZE))

    game = stage.Stage(ugame.display, constants.FPS)
    game.layers = [ship] + [background]
    game.render_block()

    while True:
        keys = ugame.buttons.get_pressed()

        # Input handling for A button and Movement
        if keys & ugame.K_X:
            if a_button == constants.button_state["button_up"]:
                a_button = constants.button_state["button_just_pressed"]
            elif a_button == constants.button_state["button_just_pressed"]:
                a_button = constants.button_state["button_still_pressed"]
        else:
            if a_button == constants.button_state["button_still_pressed"]:
                a_button = constants.button_state["button_released"]
            else:
                a_button = constants.button_state["button_up"]

        if a_button == constants.button_state["button_just_pressed"]:
            sound.play(pew_sound)

        if keys & ugame.K_RIGHT and ship.x < (constants.SCREEN_X - constants.SPRITE_SIZE):
            ship.move(ship.x + constants.SPRITE_MOVEMENT_SPEED, ship.y)
        if keys & ugame.K_LEFT and ship.x > 0:
            ship.move(ship.x - constants.SPRITE_MOVEMENT_SPEED, ship.y)
        if keys & ugame.K_UP and ship.y > 0:
            ship.move(ship.x, ship.y - constants.SPRITE_MOVEMENT_SPEED)
        if keys & ugame.K_DOWN and ship.y < (constants.SCREEN_Y - constants.SPRITE_SIZE):
            ship.move(ship.x, ship.y + constants.SPRITE_MOVEMENT_SPEED)

        game.render_sprites([ship])
        game.tick()

if __name__ == "__main__":
    # Start the program at the splash scene
    splash_scene()