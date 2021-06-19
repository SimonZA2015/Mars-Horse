import sys

import pygame
from data.scripts.other_scripts import checkMouse
from data.scripts.gui import guimenu
from data.scripts import other_scripts, ids


class KeyListen():
    def __init__(self, view):
        self.keyListen(view)
        self.mouseClick(view)
        self.mouseCheck(view)

    def keyListen(tap, self):
        key = pygame.key.get_pressed()
        startLoad = 0
        if key[pygame.K_ESCAPE]:
            if not self.isStartShow:
                exit()
        if self.isStartShow:
            if key[pygame.K_w]:
                self.playerY += 5
                intArray = 3
                self.playerSpriteUp = other_scripts.SpritePlayer.get(self, intArray, self.playerSpriteUp)

            elif key[pygame.K_s]:
                self.playerY -= 5
                intArray = 4
                self.playerSpriteDown = other_scripts.SpritePlayer.get(self, intArray, self.playerSpriteDown)

            elif key[pygame.K_d]:
                self.playerX -= 5
                intArray = 2
                self.playerSpriteRight =  other_scripts.SpritePlayer.get(self, intArray, self.playerSpriteRight)

            elif key[pygame.K_a]:
                self.playerX += 5
                intArray = 1
                self.playerSpriteLeft = other_scripts.SpritePlayer.get(self, intArray, self.playerSpriteLeft)
            else:
                intArray = 0
                self.playerStay = other_scripts.SpritePlayer.get(self, intArray, self.playerSpriteStay)

            if key[pygame.K_q]:
                self.isRightHand = False
                self.isLeftHand = True
            elif key[pygame.K_e]:
                self.isLeftHand = False
                self.isRightHand = True

        for i in pygame.event.get():
            if i.type == pygame.QUIT:
                pygame.display.quit()
                pygame.quit()
                sys.exit()


    def mouseClick(tap, self):
        for ev in pygame.event.get():
            if ev.type == pygame.MOUSEBUTTONDOWN:
                mouse = pygame.mouse.get_pos()
                if not self.isSittingsShow and not self.isStartShow:
                    if checkMouse.check(ids.startMenu, ids.startMenu1, mouse):
                        self.isLeftHand = False
                        self.isRightHand = False
                        self.isRightHudOn = False
                        self.isLeftHudOn = False
                        self.isStartShow = True
                    elif checkMouse.check(ids.sitMenu, ids.sitMenu1, mouse):
                        self.isSittingsShow = True
                    elif checkMouse.check(ids.exitMenu, ids.exitMenu1, mouse):
                        exit()
                elif self.isSittingsShow:
                    if checkMouse.check(ids.backSit, ids.backSit1, mouse):
                        self.isSittingsShow = False

                    elif checkMouse.check(ids.resize, ids.resize1, mouse):
                        if self.resolutionInt < len(ids.sizeMap) - 1:
                            self.resolutionInt += 1
                        else:
                            self.resolutionInt = 0

                        with open(ids.sittingsFile, 'r') as file:
                            data = file.readlines()
                            file.close()
                            data[1] = self.resolutionInt
                            with open(ids.sittingsFile, 'w') as file:
                                file.writelines(data)
                                file.close()
                elif self.isStartShow:
                    if checkMouse.check(ids.leftHud, ids.leftHud1, mouse) and self.isLeftHudOn:
                        self.isLeftOpen = True



    def mouseCheck(tap, self):
        mouse = pygame.mouse.get_pos()
        size = self.resize
        if not self.isSittingsShow and not self.isStartShow:
            if checkMouse.check(ids.startMenu, ids.startMenu1, mouse):
                self.screen.blit(guimenu.startMouse(self, ids.startMenu, ids.startMenu1, self.widthStart),
                                 (ids.startMenu))
                self.widthStart += 7
                if self.widthStart >= ids.sitMenu1[0] - ids.startMenu[0]:
                    self.isLeftHand = False
                    self.isRightHand = False
                    self.isRightHudOn = False
                    self.isLeftHudOn = False
                    self.isStartShow = True

            elif checkMouse.check(ids.sitMenu, ids.sitMenu1, mouse):
                self.screen.blit(guimenu.startMouse(self, ids.sitMenu, ids.sitMenu1, self.widthStart), (ids.sitMenu))
                self.widthStart += 7
                if self.widthStart >= ids.sitMenu1[0] - ids.sitMenu[0]:
                    self.isSittingsShow = True
            # elif checkMouse.check(ids.exitMenu, ids.exitMenu1, mouse):
            #     self.screen.blit(guimenu.startMouse(self, ids.exitMenu, ids.exitMenu1, self.widthStart), (ids.exitMenu))
            #     self.widthStart += 7
            #     if self.widthStart >= ids.exitMenu1[0] - ids.exitMenu[0]:
            #         exit()
            else:
                self.widthStart = 0

        elif self.isSittingsShow:
            if checkMouse.check(ids.backSit, ids.backSit1, mouse):
                self.screen.blit(guimenu.startMouse(self, ids.backSit, ids.backSit1, self.widthStart), (ids.backSit))
                self.widthStart += 1
                if self.widthStart >= ids.backSit1[0] - ids.backSit[0]:
                    self.isSittingsShow = False
            else:
                self.widthStart = 0

        elif self.isStartShow:
            if checkMouse.check(ids.leftHud, ids.leftHud1, mouse):
                self.isLeftHudOn = True
            elif checkMouse.check(ids.rightHud, ids.rightHud1, mouse):
                self.isRightHudOn = True