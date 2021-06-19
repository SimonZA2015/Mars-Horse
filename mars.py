import os
import sys
import threading

from PyQt5.QtWidgets import QApplication, QMainWindow

from PyQt5 import Qt
from PyQt5.QtWidgets import QLabel, QPushButton, QVBoxLayout, QFrame

class ErrorView(QMainWindow):
    def __init__(self, errorValue, *args, **kwargs):

        super(ErrorView, self).__init__(errorValue, *args, **kwargs)
        self.setWindowTitle("Error MarsHorse")
        label = QLabel(errorValue)
        label.setAlignment(Qt.AlignCenter)
        buttonOk = QPushButton('Хорошо')
        buttonOk.clicked.connect(self.close)
        vframe = QFrame()
        vbox = QVBoxLayout(self)
        vbox.addWidget(label)
        vbox.addWidget(buttonOk)
        vframe.setLayout(vbox)
        self.setCentralWidget(label)

    def close(self):
        self.closeEvent()

class main():
    try:
        def __init__(gui):
            import data.scripts
            import pygame
            from data.scripts.getPath import getPath
            from data.scripts.style import mainStyle
            from data.scripts.terrain import Terrain
            from data.scripts.player import PlayerModel
            from data.scripts.space_ship import Spusk
            from data.scripts.other_scripts import scaleShip
            from data.scripts import ids
            from data.scripts import other_scripts

            fullscreen = 0

            gui.FPS = 60
            gui.stop = 0
            gui.alpha = 100
            gui.playerX = 0
            gui.playerY = 0
            gui.playerXX = 0
            gui.playerYY = 0
            gui.scaleShip = 1000
            gui.scaleGG = 100
            gui.loadingInt = 100
            gui.isSoundShip = True
            gui.isStopSoundShip = True
            gui.widthStart = 0
            gui.rotateLoad = 0
            gui.playerSpriteStay = 0
            gui.playerSpriteUp = 0
            gui.playerSpriteDown = 0
            gui.playerSpriteLeft = 0
            gui.playerSpriteRight = 0
            gui.playerSpriteVivod = 0
            gui.printV = ''
            gui.isLoadTerr = True
            gui.isSittingsShow = False
            gui.isStartShow = False
            gui.resolutionInt = 0
            if os.path.exists(ids.sittingsFile):
                fullscreen = other_scripts.fileOpen.get(gui, ids.sittingsFile, 0)
                gui.resolutionInt = int(other_scripts.fileOpen.get(gui, ids.sittingsFile, 1))

            resolution = ids.sizeMap[int(gui.resolutionInt)]
            gui.resize = resolution

            # centered window
            os.environ['SDL_VIDEO_CENTERED'] = '1'

            pygame.mixer.pre_init(44100, 16, 2, 4096)  # frequency, size, channels, buffersize
            pygame.init()  # turn all of pygame on.
            pygame.display.set_caption("MarsStation")
            programIcon = pygame.image.load(ids.idIconApp)
            pygame.display.set_icon(programIcon)
            gui.screen = pygame.display.set_mode(gui.resize, ids.isFullscreen[int(fullscreen)])

            def potok():
                gui.sand = Terrain.sendCreate(gui, ((gui.resize[0] * 3) * 2, (gui.resize[1] * 3) * 2))
                gui.terrainSurface = Terrain.terrainCreate(gui, 150, 390, 200,
                                                           ((gui.resize[0] * 3) * 2, (gui.resize[1] * 3) * 2))
                gui.screen.blit(gui.terrainSurface, (-gui.resize[0], -gui.resize[1]))
                gui.stop = 1

            # str

            threading.Thread(None, potok).start()
            gui.clock = pygame.time.Clock()
            gui.sizeShip = scaleShip(gui.scaleShip)
            while True:
                gui.loadsDefs()
                gui.clock.tick(gui.FPS)
                pygame.display.update()

        def firtsplayer(gui):
            pos = (gui.resize[0] // 5, gui.resize[1] // 2,)
            from data.scripts.player import PlayerModel
            from data.scripts.getPath import getPath
            from data.scripts.ids import idPlayerImage
            GG = PlayerModel(pos, getPath(idPlayerImage), gui.scaleGG)
            PlayerModel.walk(GG, gui.playerX, gui.playerY)
            gui.playerX, gui.playerY = PlayerModel.getxy(GG)
            gui.screen.blit(GG.image, GG.rect)

        def loading(gui):
            from data.scripts.gui import guimenu
            gui.screen.blit(guimenu.loading(gui), (0, 0))

        def updateSlays(gui):
            from data.scripts.other_scripts import scaleShip
            from data.scripts.space_ship import Spusk
            from data.scripts.ids import idShipImage
            from data.scripts.player import PlayerModel
            from data.scripts import ids

            pos = (gui.resize[0] // 5 + gui.playerX + gui.playerXX, gui.resize[1] // 2 + gui.playerY + gui.playerYY)
            gui.ship = Spusk(pos, idShipImage, gui.scaleShip)
            gui.scaleShip = scaleShip.getScale(gui.sizeShip)
            gui.screen.blit(gui.terrainSurface, (-gui.resize[0] + gui.playerX, -gui.resize[1] + gui.playerY))
            if gui.isStartShow:
                gui.playerPos = PlayerModel((gui.resize[0] // 2, gui.resize[1] // 2),
                                            ids.idHorsePlayer(gui.playerSpriteVivod).idHorse, 10)
                gui.screen.blit(gui.playerPos.image, gui.playerPos.rect)
            gui.screen.blit(gui.ship.image, gui.ship.rect)
            if gui.isSoundShip:
                gui.sound_ship = Spusk.sound(gui.ship, True)
                gui.isSoundShip = False
            if gui.scaleShip == 0 and gui.isStopSoundShip:
                gui.sound_ship.stop()
                gui.isStopSoundShip = False

        def menuShow(self):
            from data.scripts.gui import guimenu
            if not self.isSittingsShow and not self.isStartShow:
                displayMenu = guimenu.start(self)
                self.screen.blit(displayMenu, (self.resize[0] // 2, 0))
            elif self.isSittingsShow:
                self.screen.blit(guimenu.sitShow(self), (self.resize[0] // 2, 0))
            elif self.isStartShow:
                self.screen.blit(guimenu.hudShow(self), (0, 0))

        def loadsDefs(gui):
            from data.scripts.style import mainStyle
            from data.scripts.key import KeyListen
            from data.scripts.terrain import Terrain

            gui.screen.fill(mainStyle)
            if gui.stop == 0:
                gui.loading()
            else:
                gui.updateSlays()
                gui.menuShow()
                KeyListen(gui)
                if gui.isStartShow:
                    Terrain.genListen(gui)
                print('\r' + gui.printV, end="")
                gui.printV = ''

    except ValueError:
        print(ValueError)
        app = QApplication(sys.argv)

        window = ErrorView(ValueError)
        window.show()

        app.exec_()


if __name__ == '__main__':
    st = main()
