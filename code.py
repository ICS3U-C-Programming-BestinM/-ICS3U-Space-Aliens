#!/usr/bin/env python3

# Created by: bestin
# Created on: Jan 2025
# This program is the "Space Aliens" program with sound

import ugame
import stage
import constants

def game_scene():
    # this function is the main game scene

    # image banks for CircuitPython
    image_bank_background = stage.Bank.from_bmp16("space_aliens_background.bmp")
    image_bank_sprites = stage.Bank.from_bmp16("space_aliens.bmp")

    # Set up button state for the A button
    a_button = constants.button_state["button_up"]

    # get sound ready
    pew_sound = open("pew.wav", 'rb')
    sound = ugame.audio
    sound.stop()
    sound.mute(False)

    # sets the background to image 0 in the image bank
    background = stage.Grid(image_bank_background, 10, 8)

    # create the ship sprite
    ship = stage.Sprite(image_bank_sprites, 5, 75, constants.SCREEN_Y - (2 * constants.SPRITE_SIZE))

    # create a stage for the background and set frame rate
    game = stage.Stage(ugame.display, constants.FPS)
    game.layers = [ship] + [background]
    game.render_block()

    # game loop
    while True:
        # get user input
        keys = ugame.buttons.get_pressed()

        # Handle A button (Fire) logic
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

        # If A button was just pressed, play sound
        if a_button == constants.button_state["button_just_pressed"]:
            sound.play(pew_sound)

        # Ship movement logic
        if keys & ugame.K_RIGHT:
            if ship.x < (constants.SCREEN_X - constants.SPRITE_SIZE):
                ship.move(ship.x + constants.SPRITE_MOVEMENT_SPEED, ship.y)
        if keys & ugame.K_LEFT:
            if ship.x > 0:
                ship.move(ship.x - constants.SPRITE_MOVEMENT_SPEED, ship.y)
        if keys & ugame.K_UP:
            if ship.y > 0:
                ship.move(ship.x, ship.y - constants.SPRITE_MOVEMENT_SPEED)
        if keys & ugame.K_DOWN:
            if ship.y < (constants.SCREEN_Y - constants.SPRITE_SIZE):
                ship.move(ship.x, ship.y + constants.SPRITE_MOVEMENT_SPEED)

        # update game logic and render
        game.render_sprites([ship])
        game.tick()

if __name__ == "__main__":
    game_scene()