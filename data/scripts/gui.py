import pygame

from Earth.data.scripts.ids import idPlayerImage
from Earth.data.scripts.player import PlayerModel
from Earth.data.scripts.style import *
from Earth.data.scripts import ids, other_scripts


class guimenu:
    def start(gui):
        skelet = pygame.Surface((gui.resize[0] // 2, gui.resize[1]))
        skelet.set_alpha(255)
        skelet.set_colorkey((0, 0, 0))
        skeletonSize = skelet.get_size()
        butSloy = pygame.Surface(skeletonSize)
        # contur = pygame.draw.rect(butSloy, startTextStyle,
        #                           (0, 0, skeletonSize[0] - 2, skeletonSize[1] - 2), 1)
        butSloy.set_alpha(255)
        butStartSloy = pygame.Surface((skeletonSize[0] - 5, 37))
        butSitSloy = pygame.Surface((skeletonSize[0] - 5, 37))
        butExitSloy = pygame.Surface((skeletonSize[0] - 5, 37))
        butStart = pygame.draw.rect(butStartSloy, conturSkeletStyle,
                                    (0, 0, skeletonSize[0] - 5, 37), 0)
        butSit = pygame.draw.rect(butSitSloy, conturSkeletStyle,
                                  (0, 0, skeletonSize[0] - 5, 37), 0)
        butExit = pygame.draw.rect(butExitSloy, conturSkeletStyle,
                                   (0, 0, skeletonSize[0] - 5, 37), 0)
        sitfont = pygame.font.SysFont('Corbel', 37)
        textSit = sitfont.render('Настройки', True, startTextStyle)
        startfont = pygame.font.SysFont('Corbel', 37)
        textStart = startfont.render('Начать', True, startTextStyle)
        exitfont = pygame.font.SysFont('Corbel', 37)
        textExit = exitfont.render('Выход', True, startTextStyle)
        sitTextRect = textExit.get_rect()
        sitLayRect = butSitSloy.get_rect()
        pos = butSitSloy.get_size()
        butSitSloy.blit(textSit, (sitLayRect[3] - sitTextRect[3] // 2, 3))
        pos = butStartSloy.get_size()
        butStartSloy.blit(textStart, (pos[0] // 4, 2))
        pos = butExitSloy.get_size()
        butExitSloy.blit(textExit, (pos[0] // 4, 5))
        butSloy.blit(butStartSloy, (5, skeletonSize[1] // 3))
        butSloy.blit(butSitSloy, (5, skeletonSize[1] // 3 + 50))
        butSloy.blit(butExitSloy, (5, skeletonSize[1] // 3 + 50 + 50))
        skelet.blit(butSloy, (0, 0))

        return skelet

    def startMouse(gui, start, start1, width):
        surface = pygame.Surface((abs(start1[0] - start[0]), abs(start[1] - start1[1])))
        surface.set_colorkey((0, 0, 0))
        surface.set_alpha(255)
        pygame.draw.rect(surface, startTextStyle,
                         (0, 0, width, 37))
        return surface

    def sitShow(gui):
        skelet = pygame.Surface((gui.resize[0] // 2, gui.resize[1]))
        skelet.set_colorkey((0, 0, 0))
        skelet.set_alpha(255)
        skeletPos = skelet.get_size()
        topSlay = pygame.Surface((gui.resize[0] // 2 - 10, 37))
        resizeSlay = pygame.Surface((gui.resize[0] // 2 - 10, 37))
        soundSlay = pygame.Surface((gui.resize[0] // 2 - 10, 37))
        back = pygame.draw.rect(topSlay, conturSkeletStyle, (0, 0, 20, 37))
        name = pygame.draw.rect(topSlay, conturSkeletStyle, (30, 0, topSlay.get_size()[0] - 30, 37))
        resize = pygame.draw.rect(resizeSlay, conturSkeletStyle, resizeSlay.get_rect(), 37)
        sound = pygame.draw.rect(soundSlay, conturSkeletStyle, soundSlay.get_rect(), 37)
        backFont = pygame.font.SysFont('Corbel', 37)
        textBack = backFont.render("<", True, startTextStyle)
        titleFont = pygame.font.SysFont('Corbel', 25)
        textTitle = backFont.render("Настройки", True, startTextStyle)
        resFont = pygame.font.SysFont('Corbel', 25)
        resText = backFont.render(str(gui.resize[0]) + 'x' + str(gui.resize[1]), True, startTextStyle)
        topSlay.blit(textBack, (0, 0))
        topSlay.blit(textTitle, (topSlay.get_size()[0] // 7, 0))
        resizeSlay.blit(resText, (0, 0))
        skelet.blit(topSlay, (5, skeletPos[1] // 3 - 50))
        skelet.blit(resizeSlay, (5, skeletPos[1] // 3))
        skelet.blit(soundSlay, (5, skeletPos[1] // 3 + 50))

        return skelet

    def loading(gui):
        skelet = pygame.Surface(gui.resize)
        skelet.fill((0, 0, 0))
        logoAthorImage = pygame.image.load(ids.idLogoathorImage)
        loadingImage = pygame.image.load(ids.idLoadImage)
        logoAthorImage = pygame.transform.scale(logoAthorImage, (int(gui.resize[0] // 4), int(gui.resize[0] // 4 - 25)))
        loadingImage = pygame.transform.scale(loadingImage, (int(gui.resize[0] // 9), int(gui.resize[0] // 9)))
        loadingImage = pygame.transform.rotate(loadingImage, gui.rotateLoad)
        logoAthorRect = logoAthorImage.get_size()
        athorFont = pygame.font.SysFont('Corbel', 20)
        textAthor = athorFont.render("Denis Hik's game", True, athorTextStyle)
        textAthorSize = textAthor.get_size()
        skelet.blit(logoAthorImage, (gui.resize[0] // 2.5, gui.resize[1] // 2.5))
        skelet.blit(textAthor, ((gui.resize[0] - textAthorSize[0]) // 2, gui.resize[1] // 2.5 + logoAthorRect[1] + 2))
        skelet.blit(loadingImage, (int(gui.resize[0] // 9 * 8), int(gui.resize[0] // 9 * 8)))

        gui.rotateLoad += 10

        return skelet

    def hudShow(gui):
        skelet = pygame.Surface(gui.resize)
        skelet.set_colorkey((0, 0, 0))
        skelet.set_alpha(255)
        hud_slay = pygame.Surface((gui.resize[0] // 2, gui.resize[1] // 9))
        hudLeft_slay = pygame.Surface((10, gui.resize[1] // 9))
        hudRight_slay = pygame.Surface((10, gui.resize[1] // 9))
        hand_slay = pygame.Surface((gui.resize[0] // 6, gui.resize[1] // 9))
        hud_slay.fill(hudBackStyle)
        #hand work>
        hand_slay.fill(hudBackStyle)
        handLeft = pygame.draw.rect(hand_slay, handsStyle,
                                    (0, 0, hand_slay.get_size()[0] // 2, hand_slay.get_size()[1]), 5)
        handRight = pygame.draw.rect(hand_slay, handsStyle, (
        hand_slay.get_size()[0] // 2, 0, hand_slay.get_size()[0] // 2, hand_slay.get_size()[1]), 5)
        if gui.isLeftHand:
            handLeftOn = other_scripts.gradientRect(hand_slay, handOnStyle, hudBackStyle, pygame.Rect(3, 3, hand_slay.get_size()[0] // 2 - 5, hand_slay.get_size()[1] - 5))
        elif gui.isRightHand:
            handRightOn = other_scripts.gradientRect(hand_slay,hudBackStyle, handOnStyle,
                                                    pygame.Rect(hand_slay.get_size()[0] // 2 + 3, 3, hand_slay.get_size()[0] // 2 - 5,
                                                                hand_slay.get_size()[1] - 5))
        #hud work>
        hud_contur = pygame.draw.rect(hud_slay, hudConturStyle,
                                      (0, -5, hud_slay.get_size()[0], hud_slay.get_size()[1] + 5), 4)
        leftHud = pygame.draw.polygon(hudLeft_slay, hudBackStyle, [[0, hudLeft_slay.get_rect()[3] // 5], [0, hudLeft_slay.get_rect()[3] // 5 * 4], [hudLeft_slay.get_rect()[2], hudLeft_slay.get_rect()[3]], [hudLeft_slay.get_rect()[2], 0]])
        rightHud = pygame.draw.polygon(hudRight_slay, hudBackStyle, [[hudRight_slay.get_rect()[2], hudRight_slay.get_rect()[3] // 5], [hudRight_slay.get_rect()[2], hudLeft_slay.get_rect()[3] // 5 * 4], [0, hudLeft_slay.get_rect()[3]], [0, 0]])
        if gui.isLeftHudOn:
            leftHudOn = pygame.draw.polygon(hudLeft_slay, hudOnStyle, [[2, hudLeft_slay.get_rect()[3] // 5],
                                                                       [2, hudLeft_slay.get_rect()[3] // 5 * 4],
                                                                       [hudLeft_slay.get_rect()[2],
                                                                        hudLeft_slay.get_rect()[3] - 2],
                                                                       [hudLeft_slay.get_rect()[2], 2]])
            gui.isLeftHudOn = False
        elif gui.isRightHudOn:
            rightHudOn = pygame.draw.polygon(hudRight_slay, hudOnStyle,
                                           [[hudRight_slay.get_rect()[2] - 2, hudRight_slay.get_rect()[3] // 5],
                                            [hudRight_slay.get_rect()[2] - 2, hudLeft_slay.get_rect()[3] // 5 * 4],
                                            [0, hudRight_slay.get_rect()[3] - 2], [0, 2]])
            gui.isRightHudOn = False

        skelet.blit(hud_slay, (gui.resize[0] // 4, 0))
        skelet.blit(hudLeft_slay, (gui.resize[0] // 4 - hudLeft_slay.get_rect()[2], 0))
        skelet.blit(hudRight_slay, (gui.resize[0] // 4 + hud_slay.get_rect()[2], 0))
        skelet.blit(hand_slay, (gui.resize[0] // 7 * 3, gui.resize[1] // 9 * 8))

        return skelet
