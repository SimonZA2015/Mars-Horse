import threading
import time
import pygame

from data.scripts import ids


class scaleShip():
    def __init__(self, scale):
        self.scale = scale
        self.speed = 10
        self.time = 0.03

        def colculate():
            for i in range(self.scale // self.speed):
                self.scale -= self.speed
                if i < (self.scale // self.speed) // 2:
                    self.time = 0.03
                time.sleep(self.time)

        threading.Thread(target=colculate).start()

    def getScale(self):
        return self.scale


class editSprite():
    def rotate(image, rect, angle):
        """rotate an image while keeping its center"""
        rot_image = pygame.transform.rotate(image, angle)
        rot_rect = rot_image.get_rect(center=rect.center)
        return rot_image, rot_rect


class checkMouse():
    def check(widget, widget1, mouse):
        widgetX = widget[0]
        widgetY = widget[1]
        if widget[0] < mouse[0] and widget1[0] > mouse[0]:
            if widget[1] < mouse[1] and widget1[1] > mouse[1]:
                return True


class SpritePlayer():
    def get(self, intArray, playerSpriteParties):
        if playerSpriteParties >= ids.intsPhotos[intArray]:
            playerSpriteParties = 0
        self.playerSpriteVivod = ids.intsPhotosStart[intArray] + playerSpriteParties
        playerSpriteParties += 1
        return playerSpriteParties

class fileOpen():
    def get(self, path, dataInt):
        with open(path, 'r') as file:
            data = file.readlines()
            file.close()
            return data[dataInt]

class console():
    def Print(self, textAdd):
        self.printV = self.printV + '\n' + textAdd

def gradientRect( window, left_colour, right_colour, target_rect ):
    colour_rect = pygame.Surface( ( 2, 2 ) )                                   # tiny! 2x2 bitmap
    pygame.draw.line( colour_rect, left_colour,  ( 0,0 ), ( 0,1 ) )            # left colour line
    pygame.draw.line( colour_rect, right_colour, ( 1,0 ), ( 1,1 ) )            # right colour line
    colour_rect = pygame.transform.smoothscale( colour_rect, ( target_rect.width, target_rect.height ) )  # stretch!
    window.blit( colour_rect, target_rect )                                    # paint it
