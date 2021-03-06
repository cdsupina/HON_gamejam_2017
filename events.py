import pygame
from pygame.locals import *
from decor import *
from values import *
from assets import *

#fuction: looks for input events and calls appropriate functions
#parameters: int scene_id, Player player
#scene_id: value representing where in the game the player is example: a menu or a game level
#player: represents an instance of the player class
#title_menu: title menu to use buttons from
def handle_events(scene_id, player, background, menu):

    result = scene_id
    end = False
    for event in pygame.event.get():
        #print(event)

        if event.type == QUIT:
            exit()

        if scene_id == 0:
            if event.type == MOUSEBUTTONUP:
                if event.button == 1:
                    for c,b in zip(menu.clickables, menu.buttons):
                        if c.collidepoint(pygame.mouse.get_pos()):
                            result = b.activate(player, background)

        if scene_id == 1:
            if event.type == KEYDOWN:
                if event.key == K_w:
                    player.assign_frame_set(0)
                    background.accelerate(1)
                if event.key == K_s:
                    player.assign_frame_set(1)
                    background.accelerate(0)
                if event.key == K_a:
                    player.assign_frame_set(2)
                    background.accelerate(3)
                if event.key == K_d:
                    player.assign_frame_set(3)
                    background.accelerate(2)

                if event.key == K_UP:
                    effect = pygame.mixer.Sound(strike_sound_path)
                    effect.play()
                    player.attack(0)
                if event.key == K_DOWN:
                    effect = pygame.mixer.Sound(strike_sound_path)
                    effect.play()
                    player.attack(1)
                if event.key == K_RIGHT:
                    effect = pygame.mixer.Sound(strike_sound_path)
                    effect.play()
                    player.attack(2)
                if event.key == K_LEFT:
                    effect = pygame.mixer.Sound(strike_sound_path)
                    effect.play()
                    player.attack(3)

                if event.key == K_SPACE:
                    #print("space key pressed")
                    if end == False:
                        effect = pygame.mixer.Sound(player_death_sound_path)
                        effect.play()
                        decors.append(Decor(player_death_frames, player_death_final_img, player.rect.x, player.rect.y - 90, 350))
                        decor_sprite_group.add(decors[-1])
                        player.death_spawned = True
                    end = True

            if event.type == KEYUP:
                if event.key == K_w:
                    background.deccelerate(1)
                if event.key == K_s:
                    background.deccelerate(0)
                if event.key == K_a:
                    background.deccelerate(3)
                if event.key == K_d:
                    background.deccelerate(2)

    if result < 0:
        result = 0
    return result, end
