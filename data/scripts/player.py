import pygame
from pygame import key


class PlayerModel(pygame.sprite.Sprite):
    def __init__(player, pos, logo, scale):
        pygame.sprite.Sprite.__init__(player)
        player.image = pygame.image.load(logo)
        player.size = player.image.get_size()
        player.image = pygame.transform.scale(player.image, (int(player.size[0] + scale), int(player.size[1] + scale)))
        player.rect = player.image.get_rect(center=pos)

    def walk(player, x, y):
        player.X = x
        player.Y = y
        key = pygame.key.get_pressed()
        if key[pygame.K_w]:
            player.Y -= 5
        if key[pygame.K_s]:
            player.Y += 5
        if key[pygame.K_d]:
            player.X += 5
        if key[pygame.K_a]:
            player.X -= 5

        return player.X, player.Y

    def getxy(player):
        return player.X, player.Y