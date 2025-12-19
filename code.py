#!/usr/bin/env python3
# Created by: Mr. Mathew
# Created on: dec 2025
# This program displays a background and a sprite for the "Space Aliens" game

import ugame
import stage

def game_scene():
    # 1. Load image banks (CITE: Must be 16-color indexed BMPs)
    image_bank_background = stage.Bank.from_bmp16("space_aliens_background.bmp")
    image_bank_sprites = stage.Bank.from_bmp16("space_aliens.bmp")

    # 2. Setup background grid (10x8 tiles)
    background = stage.Grid(image_bank_background, 10, 8)

    # 3. Create the ship sprite 
    # Change '5' to '0' if your ship is the first image in your BMP
    ship = stage.Sprite(image_bank_sprites, 5, 75, 66)

    # 4. Create the stage and set layers
    # Layers are a list; the ship comes first so it is on top
    game = stage.Stage(ugame.display, 60)
    game.layers = [ship] + [background]

    # 5. Render the background once
    game.render_block()

    # 6. Main game loop
    while True:
        
        # Redraw the sprite layer
        game.render_sprites([ship])
        
        # Refresh the screen at 60 FPS
        game.tick()

if __name__ == "__main__":
    game_scene()