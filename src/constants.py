import pygame
IDLE = 0
ATTACK = 1
WALK = 2


HITBOX_LOW_KICK = (130, 0, 150, 270)
HITBOX_RELATIVE = (130, 50, 150, 270)
HITBOX_LOW_KICK = (130, 250, 150, 150)
HURTBOX_RELATIVE = (0, 0, 150, 270)
COLLISION_RELATIVE = (0, 270, 150, 150)

ATTACK_COOLDOWN = 500  # Milliseconds
WALK_COOLDOWN = 100
ENNEMY_ATTACK_COOLDOWN = 500

LEFT_PUNCH = 0
HIGH_KICK = 1
LOW_KICK = 2

SPECIAL_ATTACK_COST = 25
ATTACK_KEYS = [pygame.locals.K_SPACE, pygame.locals.K_x, pygame.locals.K_c, pygame.locals.K_v]
GAME_TIME = 18000