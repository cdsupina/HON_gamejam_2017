import pygame
from pygame.locals import *
from sys import exit
from values import *
from events import *
from assets import *
from player_sprites import *
from enemy_sprites import *
from scene import *
from game_ui import *
from pickups import *

def new_game_init(player, background):

    background.rect.x = -500
    background.rect.y = -500
    score = 0
    player.stats['health'] = INIT_PLAYER_STATS['health']
    player.stats['level'] = INIT_PLAYER_STATS['level']
    player.stats['exp'] = INIT_PLAYER_STATS['exp']
    player.stats['damage'] = INIT_PLAYER_STATS['damage']

    for i in range(0,10):
        enemies.append(Enemy(skull_frames, skull_damage_frames, skull_death_frames, INIT_SKULL_STATS, 100 + i * 80, 600, 300, 0))
        enemy_sprite_group.add(enemies[-1])

    for i in range(0,20):
        pickups.append(Pickup(exp_frames, 100 + i * 60, 150, 300))
        pickup_sprite_group.add(pickups[-1])

def game_end():
    enemies[:] = []
    pickups[:] = []

    player_attack_group.empty()
    enemy_sprite_group.empty()
    pickup_sprite_group.empty()