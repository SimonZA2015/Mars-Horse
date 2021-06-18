import pygame

from data.scripts.getPath import getPath

sizeMap = [[400, 400], [1024, 800]]
defaultSit = '0\n0'
idIconApp = getPath('data/media/texture/logoApp.png')
idShipImage = getPath("data/media/texture/ship.png")
idPlayerImage = getPath("data/media/texture/horsePlayer/walkLeft0.png")
idLogoathorImage = getPath("data/media/texture/athor.png")
idLoadImage = getPath("data/media/texture/load.png")
idShipSoud = getPath("data/media/soud/ship.wav")
sittingsFile = getPath("data/sittings/sittings")
isFullscreen = [pygame.SRCALPHA, pygame.FULLSCREEN]
with open(sittingsFile, 'r') as file:
    data = file.readlines()
    file.close()
    intRes = data[1]
sizeSys = sizeMap[int(intRes)]

#menusStart
startMenu = ((sizeSys[0] // 2) + 5), sizeSys[1] // 3
startMenu1 = (startMenu[0] + ((sizeSys[0] // 2) - 5)), startMenu[1] + 37
sitMenu = ((sizeSys[0] // 2) + 5), sizeSys[1] // 3 + 50
sitMenu1 = (sitMenu[0] + ((sizeSys[0] // 2) - 5)), sitMenu[1] + 37
exitMenu = ((sizeSys[0] // 2) + 5), sizeSys[1] // 3 + 50 + 50
exitMenu1 = (exitMenu[0] + ((sizeSys[0] // 2) - 5)), exitMenu[1] + 37

#menusSittigs
sitSkelet = (sizeSys[0]//2, sizeSys[1])
backSit = sizeSys[0] // 2, sizeSys[1] // 3 - 50
backSit1 = sizeSys[0] // 2 + 20, sizeSys[1] // 3 - 50 + 37
resize = sizeSys[0] // 2 + 5, sizeSys[1] // 3
resize1 = resize[0] + (sizeSys[0] // 2 - 10), resize[0] + 37

#playing
leftHud = sizeSys[0] // 4 - 10, 0
leftHud1 = sizeSys[0] // 4, sizeSys[1] // 9
rightHud = sizeSys[0] - (sizeSys[0] // 4), 0
rightHud1 = (sizeSys[0] - (sizeSys[0] // 4)) + 10, sizeSys[1] // 9


intsPhotos = [4, 8, 8, 8, 8]
intsPhotosStart = [0, 4, 100, 52, 148]
class idHorsePlayer():
    def __init__(self, intPhoto):
        if intPhoto > 9:
            if intPhoto > 99:
                intPhoto = str(intPhoto)
            else:
                intPhoto = '0' + str(intPhoto)
        elif intPhoto < 10:
            intPhoto = "00" + str(intPhoto)
        self.idHorse = getPath('data/media/texture/horsePlayer/tile' + intPhoto + '.png')
