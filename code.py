#!/usr/bin/env python3

# Created by: bestin
# Created on: Jan 2025
# RST 09: Lasers

import ugame
import stage
import time
import random

import constants

def splash_scene():
    coin_sound = open("coin.wav", 'rb')
    sound = ugame.audio
    sound.stop()
    sound.mute(False)
    sound.play(coin_sound)

    image_bank_mt_background = stage.Bank.from_bmp16("mt_game_studio.bmp")
    background = stage.Grid(image_bank_mt_background, constants.SCREEN_GRID_X, constants.SCREEN_GRID_Y)

    game = stage.Stage(ugame.display, constants.FPS)
    game.layers = [background]
    game.render_block()

    time.sleep(2.0)
    menu_scene()

def menu_scene():
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
    image_bank_background = stage.Bank.from_bmp16("space_aliens_background.bmp")
    image_bank_sprites = stage.Bank.from_bmp16("space_aliens.bmp")

    # Create random background
    background = stage.Grid(image_bank_background, constants.SCREEN_GRID_X, constants.SCREEN_GRID_Y)
    for x_location in range(constants.SCREEN_GRID_X):
        for y_location in range(constants.SCREEN_GRID_Y):
            tile_picked = random.randint(0, 3)
            background.tile(x_location, y_location, tile_picked)

    # Sprite for the ship
    ship = stage.Sprite(image_bank_sprites, 5, 75, constants.SCREEN_Y - (2 * constants.SPRITE_SIZE))

    # Create lasers for when we shoot
    lasers = []
    for laser_number in range(constants.TOTAL_NUMBER_OF_LASERS):
        a_single_laser = stage.Sprite(image_bank_sprites, 10, constants.OFF_SCREEN_X, constants.OFF_SCREEN_Y)
        lasers.append(a_single_laser)

    a_button = constants.button_state["button_up"]
    pew_sound = open("pew.wav", 'rb')
    sound = ugame.audio
    sound.stop()
    sound.mute(False)

    game = stage.Stage(ugame.display, constants.FPS)
    # Layer order: Lasers on top of ship, ship on top of background
    game.layers = lasers + [ship] + [background]
    game.render_block()

    while True:
        keys = ugame.buttons.get_pressed()

        # Handle A button (Fire)
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

        # Fire a laser
        if a_button == constants.button_state["button_just_pressed"]:
            for laser_number in range(len(lasers)):
                if lasers[laser_number].x < 0:
                    lasers[laser_number].move(ship.x, ship.y)
                    sound.play(pew_sound)
                    break

        # Move lasers up
        for laser_number in range(len(lasers)):
            if lasers[laser_number].x > 0:
                lasers[laser_number].move(lasers[laser_number].x, lasers[laser_number].y - constants.LASER_SPEED)
                if lasers[laser_number].y < constants.OFF_TOP_SCREEN:
                    lasers[laser_number].move(constants.OFF_SCREEN_X, constants.OFF_SCREEN_Y)

        # Ship movement
        if keys & ugame.K_RIGHT and ship.x < (constants.SCREEN_X - constants.SPRITE_SIZE):
            ship.move(ship.x + constants.SPRITE_MOVEMENT_SPEED, ship.y)
        if keys & ugame.K_LEFT and ship.x > 0:
            ship.move(ship.x - constants.SPRITE_MOVEMENT_SPEED, ship.y)
        if keys & ugame.K_UP and ship.y > 0:
            ship.move(ship.x, ship.y - constants.SPRITE_MOVEMENT_SPEED)
        if keys & ugame.K_DOWN and ship.y < (constants.SCREEN_Y - constants.SPRITE_SIZE):
            ship.move(ship.x, ship.y + constants.SPRITE_MOVEMENT_SPEED)

        game.render_sprites(lasers + [ship])
        game.tick()

if __name__ == "__main__":
    splash_scene()