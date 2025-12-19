#!/usr/bin/env python3

# Created by: Mr. Coxall
# Created on: July 2020
# This program is the "Space Aliens" program on the PyBadge

import ugame
import stage

import constants

def game_scene():
    # this function is the main game scene

    # image banks for CircuitPython
    image_bank_background = stage.Bank.from_bmp16("space_aliens_background.bmp")
    image_bank_sprites = stage.Bank.from_bmp16("space_aliens.bmp")

    # sets the background to image 0 in the image bank
    # and the sie (10x8 tiles of size 16x16)
    background = stage.Grid(image_bank_background, 10, 8)

    ship = stage.Sprite(image_bank_sprites, 5, 75, constants.SCREEN_Y - (2 * constants.SPRITE_SIZE))

    # create a stage for the background to show up on
    # and set the frame rate to 60fps
    game = stage.Stage(ugame.display, 60)
    # set the layers, items show up in order
    game.layers = [ship] + [background]
    # render the background and initial location of sprite list
    # most likely you will only render background once per scene
    game.render_block()

    # repeat forever, game loop
    while True:
        # get user input
        keys = ugame.buttons.get_pressed()

        if keys & ugame.K_X:
            print("A")
        if keys & ugame.K_O:
            print("B")
        if keys & ugame.K_START:
            print("Start")
        if keys & ugame.K_SELECT:
            print("Select")

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

        # update game logic
        game.render_sprites([ship])
        game.tick()

if __name__ == "__main__":
    game_scene()