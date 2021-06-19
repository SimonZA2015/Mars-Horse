
class sittings:
    def __init__(self, action):
        fullscreen = 1
        self.resolution = 800, 600
        if action == 'GET-RESOLUTION':
            self.getResolution()
        else:
            print('ERROR sittingsNew.py: get argument in action - "type"')

    def getResolution(self):
        return self.resolution

    def setResolution(self, resolution):
        self.resolution = resolution
