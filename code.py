#!/usr/bin/env python3

# Created by: [Your Name]
# Created on: Dec 2025
# This program handles button input for movement and printing to the console

import ugame
import stage

def game_scene():
    # Load image banks (Must be 16-color indexed BMPs)
    image_bank_background = stage.Bank.from_bmp16("space_aliens_background.bmp")
    image_bank_sprites = stage.Bank.from_bmp16("space_aliens.bmp")

    # Setup background and ship sprite
    background = stage.Grid(image_bank_background, 10, 8)
    ship = stage.Sprite(image_bank_sprites, 5, 75, 66)

    # Create the stage and layers
    game = stage.Stage(ugame.display, 60)
    game.layers = [ship] + [background]
    game.render_block()

    # repeat forever, game loop
    while True:
        # get user input
        keys = ugame.buttons.get_pressed()

        # Check for A button (often K_X in some versions)
        if keys & ugame.K_X:
            print("A")
        
        # Check for B button (often K_O in some versions)
        if keys & ugame.K_O:
            print("B")

        if keys & ugame.K_START:
            print("Start")

        if keys & ugame.K_SELECT:
            print("Select")

        # Movement logic using bitwise AND
        if keys & ugame.K_RIGHT:
            ship.move(ship.x + 1, ship.y)
        
        if keys & ugame.K_LEFT:
            ship.move(ship.x - 1, ship.y)

        if keys & ugame.K_UP:
            ship.move(ship.x, ship.y - 1)

        if keys & ugame.K_DOWN:
            ship.move(ship.x, ship.y + 1)

        # Update sprite position and wait for next frame
        game.render_sprites([ship])
        game.tick()

if __name__ == "__main__":
    game_scene()