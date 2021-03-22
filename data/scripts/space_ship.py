from Earth.data.scripts.ids import *
import pygame


class Spusk(pygame.sprite.Sprite):
    def __init__(ship, pos, image, scale):
        pygame.sprite.Sprite.__init__(ship)
        ship.image = pygame.image.load(image).convert_alpha()
        ship.size = ship.image.get_size()
        ship.image = pygame.transform.scale(ship.image, (int(ship.size[0] + scale), int(ship.size[1] + scale)))
        ship.rect = ship.image.get_rect(center=pos)

    def sound(ship, isOn):
        sound = pygame.mixer.Sound(idShipSoud)
        if isOn:
            sound.play()
        else:
            sound.stop()
        return sound