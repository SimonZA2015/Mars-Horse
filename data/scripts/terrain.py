import random
import pygame


from data.scripts.style import *


class Terrain:
    def __init__(self, resize, kolvo, kolvo1, alpha):
        self.resize = resize
        self.sand = self.sendCreate(self.resize)
        self.terrain = self.terrainCreate(kolvo, kolvo1, alpha, ((self.resize[0] * 3) * 2, (self.resize[1] * 3) * 2))

    def terrainCreate(self, kolvo, kolvo1, alpha, size):
        global rf
        self.terrainMas = []
        surface = pygame.Surface(size)
        surface.set_colorkey((0, 0, 0))
        surface.fill(mainStyle)
        surface.set_alpha(alpha)
        surface.blit(self.sand, (0, 0))
        if self.sand.get_size()[0] < surface.get_size()[0]:
            ySand = 1
            xSand = 1
            for IntSandX in range(surface.get_size()[0] // self.sand.get_size()[0]):
                if self.sand.get_size()[1] < surface.get_size()[1]:
                    for IntSandY in range(surface.get_size()[1] // self.sand.get_size()[1]):
                        surface.blit(self.sand, (IntSandX * self.sand.get_rect()[2], IntSandY * self.sand.get_rect()[3]))
                        ySand += 1
                surface.blit(self.sand, (IntSandX * self.sand.get_rect()[2], ySand * self.sand.get_rect()[3]))
                ySand = 1
                xSand += 1

        for i in range(kolvo):
            pos = (random.randint(0, size[0] - 20), random.randint(0, size[1] - 20))
            pos1 = pos
            self.terrainMas.append(pos)
            if i == kolvo - 1:
                self.load = 0
            for k in range(random.randint(0, kolvo1)):
                r = random.randint(0, 20)
                s = pygame.draw.circle(surface, sendStyle, pos, r, r)
                p = random.randint(1, 4)
                replace0 = random.randint(0, 10)
                replace1 = random.randint(0, 10)
                if p == 1 and pos[0] + replace0 < size[0] - (r + 10) and pos[1] + replace1 < size[1] - (r + 10):
                    pos = (pos[0] + replace0, pos[1] + replace1)
                if p == 2 and pos[0] + replace0 < size[0] - (r + 10) and pos[1] - replace1 > r + 10:
                    pos = (pos[0] + replace0, pos[1] - replace1)
                if p == 3 and pos[0] - replace0 > r + 10 and pos[1] + replace1 < size[1] - (r + 10):
                    pos = (pos[0] - replace0, pos[1] + replace1)
                if p == 4 and pos[0] - replace0 > r + 10 and pos[1] - replace1 > r + 10:
                    pos = (pos[0] - replace0, pos[1] - replace1)

                self.terrainMas.append(pos)
                rf = kolvo1 // 4
                rf = kolvo1 - rf
            for g in range(rf):
                surface.set_alpha(alpha * 2)
                r = random.randint(0, 10)
                s = pygame.draw.circle(surface, groundStyle, pos1, r, r)
                p = random.randint(1, 4)
                repllace0 = random.randint(0, 10)
                repllace1 = random.randint(0, 10)
                if p == 1 and pos[0] + repllace0 < size[0] - (r + 10) and pos1[1] + repllace1 < size[1] - (r + 10) :
                    pos1 = (pos[0] + repllace0, pos1[1] + repllace1)
                if p == 2 and pos[0] + repllace0 < size[0] - (r + 10) and pos1[1] - repllace1 > r + 10:
                    pos1 = (pos[0] + repllace0, pos1[1] - repllace1)
                if p == 3 and pos[0] - repllace0 > r + 10 and pos1[1] + repllace1 < size[1] - (r + 10):
                    pos1 = (pos[0] - repllace0, pos[1] + repllace1)
                if p == 4 and pos[0] - repllace0 > r + 10 and pos1[1] - repllace1 > r + 10:
                    pos1 = (pos[0] - random.randint(0, 10), pos[1] - random.randint(0, 10))

                self.terrainMas.append(pos)

        return surface

    def sendCreate(self, size):
        surface = pygame.Surface(size)
        surface.set_colorkey((255, 255, 255))
        surface.set_alpha(50)
        px = 1
        x = 0
        y = 0
        for sY in range(size[1] // px):
            for sX in range(size[0] // px):
                pygame.draw.rect(surface, colorMarsStyle[random.randint(0, 2)], (x, y, px, px))
                x = x + px

            x = 0
            y = y + px
        return surface

    def genListen(self):
        pos = -self.resize[0] + self.playerX, -self.resize[1] + self.playerY
        # Left
        if pos[0] > self.terrainSurface.get_rect()[0] - 20 and self.isLoadTerr:
            self.isLoadTerr = False
            surfaceTemp = pygame.Surface(
                (self.terrainSurface.get_rect()[2] + self.resize[0], self.terrainSurface.get_rect()[3]))
            surfaceTemp.set_colorkey((0, 0, 0))
            surfaceTemp.set_alpha(255)
            terrainSurfaceTemp = Terrain.terrainCreate(self, 90, 100, 200,
                                                       (self.resize[0], self.terrainSurface.get_rect()[3]))
            surfaceTemp.blit(self.terrainSurface, (terrainSurfaceTemp.get_rect()[2], 0))
            surfaceTemp.blit(terrainSurfaceTemp, (0, 0))
            self.terrainSurface = surfaceTemp
            self.playerX -= self.resize[0]
            self.playerXX += self.resize[0]
            self.isLoadTerr = True

        elif pos[0] < -(self.terrainSurface.get_rect()[2]) + self.resize[0] + 20 and self.isLoadTerr:
            #Right
            self.isLoadTerr = False
            surfaceTemp = pygame.Surface(
                (self.terrainSurface.get_rect()[2] + self.resize[0], self.terrainSurface.get_rect()[3]))
            surfaceTemp.set_colorkey((0, 0, 0))
            surfaceTemp.set_alpha(255)
            terrainSurfaceTemp = Terrain.terrainCreate(self, 90, 100, 200, (self.resize[0], self.terrainSurface.get_rect()[3]))
            surfaceTemp.blit(self.terrainSurface, (0, 0))
            surfaceTemp.blit(terrainSurfaceTemp, (surfaceTemp.get_rect()[2] - self.resize[0], 0))
            self.terrainSurface = surfaceTemp
            self.isLoadTerr = True

        if pos[1] > self.terrainSurface.get_rect()[1] - 20 and self.isLoadTerr:
            self.isLoadTerr = False
            surfaceTemp = pygame.Surface(
                (self.terrainSurface.get_rect()[2], self.terrainSurface.get_rect()[3] + self.resize[0]))
            surfaceTemp.set_colorkey((0, 0, 0))
            surfaceTemp.set_alpha(255)
            terrainSurfaceTemp = Terrain.terrainCreate(self, 90, 100, 200,
                                                       (self.terrainSurface.get_rect()[3], self.resize[1]))
            surfaceTemp.blit(terrainSurfaceTemp, (0, 0))
            surfaceTemp.blit(self.terrainSurface, (0, self.resize[1]))
            self.terrainSurface = surfaceTemp
            self.playerY -= self.resize[1]
            self.playerYY += self.resize[1]
            self.isLoadTerr = True

        elif pos[1] < -(self.terrainSurface.get_rect()[3]) + self.resize[0] + 20 and self.isLoadTerr:
            self.isLoadTerr = False
            surfaceTemp = pygame.Surface(
                (self.terrainSurface.get_rect()[2], self.terrainSurface.get_rect()[3] + self.resize[0]))
            surfaceTemp.set_colorkey((0, 0, 0))
            surfaceTemp.set_alpha(255)
            terrainSurfaceTemp = Terrain.terrainCreate(self, 90, 100, 200, (self.terrainSurface.get_rect()[3], self.resize[1]))
            surfaceTemp.blit(self.terrainSurface, (0, 0))
            surfaceTemp.blit(terrainSurfaceTemp, (0, self.terrainSurface.get_rect()[3]))
            self.terrainSurface = surfaceTemp
            self.isLoadTerr = True