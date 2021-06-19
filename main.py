import os
import sys
import threading

from PyQt5 import Qt, QtWidgets
from PyQt5.QtGui import QIcon, QImage
from PyQt5.QtWidgets import QMainWindow, QLabel, QPushButton, QFrame, QVBoxLayout, QApplication, QHBoxLayout, \
    QRadioButton, QButtonGroup, QCheckBox
import mars
from data.scripts import ids, other_scripts
from data.scripts.getPath import getPath


class mainStart(QMainWindow):
    def __init__(self, *args, **kwargs):
        super(mainStart, self).__init__(*args, **kwargs)
        self.setWindowTitle("Starter MarsHorse")
        self.setWindowIcon(QIcon(getPath(ids.idIconApp)))
        self.setFixedWidth(600)
        self.home()

    def home(self):
        label = QLabel('hi')
        buttonOk = QPushButton('Start')
        buttonOk.clicked.connect(self.start)
        buttonCns = QPushButton('Exit')
        buttonCns.clicked.connect(self.closeAction)
        buttonSit = QPushButton('Sittings')
        buttonSit.clicked.connect(self.sittings)
        hframe = QFrame()
        vframe = QFrame()
        hbox = QHBoxLayout(self)
        vbox = QVBoxLayout(self)
        hbox.addWidget(label)

        vbox.addWidget(buttonOk)
        vbox.addWidget(buttonSit)
        vbox.addWidget(buttonCns)

        vframe.setLayout(vbox)
        hbox.addWidget(vframe)

        hframe.setLayout(hbox)
        self.setCentralWidget(hframe)

    def start(self):
        QtWidgets.qApp.quit()

        def potok():
            mars.main()

        threading.Thread(None, potok).start()

    def closeAction(self):
        QtWidgets.qApp.quit()

    def sittings(self):
        resolutionInt = 0
        fullscreen = 0

        def setCheckedButtons(button):
            print(button)
            if button == 0:
                if not (other_scripts.fileOpen.edit(self, ids.sittingsFile, 1, '0\n')):
                    print('r')
            if button == 1:
                if not (other_scripts.fileOpen.edit(self, ids.sittingsFile, 1, '1\n')):
                    print('r')
            if button == 2:
                if not (other_scripts.fileOpen.edit(self, ids.sittingsFile, 1, '2\n')):
                    print('r')

        def setCheckedBox(t):
            if t == 2:
                if not (other_scripts.fileOpen.edit(self, ids.sittingsFile, 0, '1\n')):
                    print('r')
            else:
                other_scripts.fileOpen.edit(self, ids.sittingsFile, 0, '0\n')

        def save():
            print('full-', int(other_scripts.fileOpen.get(self, ids.sittingsFile, 0)), '\nres-',
                  int(other_scripts.fileOpen.get(self, ids.sittingsFile, 1)))
            self.home()

        if os.path.exists(ids.sittingsFile):
            fullscreen = other_scripts.fileOpen.get(self, ids.sittingsFile, 0)
            resolutionInt = int(other_scripts.fileOpen.get(self, ids.sittingsFile, 1))

        resolutions = ids.resize
        red0 = QRadioButton('400x400')
        red0.clicked.connect(lambda: setCheckedButtons(0))
        if resolutionInt == 0:
            red0.setChecked(True)
        red1 = QRadioButton('800x600')
        red1.clicked.connect(lambda: setCheckedButtons(1))
        if resolutionInt == 1:
            red1.setChecked(True)
        red2 = QRadioButton('1024x800')
        red2.clicked.connect(lambda: setCheckedButtons(2))
        if resolutionInt == 2:
            red2.setChecked(True)

        rad_group = QButtonGroup()
        rad_group.addButton(red0)
        rad_group.addButton(red1)
        rad_group.addButton(red2)
        checb = QCheckBox('Fullscreen')
        if fullscreen == 1:
            checb.setChecked(True)
        checb.stateChanged.connect(setCheckedBox)
        buttonOk = QPushButton('ok')
        buttonOk.clicked.connect(save)

        frame = QFrame()
        frame1 = QFrame()
        label = QLabel('Sittings')
        hskelet = QHBoxLayout()
        vcontent = QVBoxLayout()
        vcontent.addWidget(red0)
        vcontent.addWidget(red1)
        vcontent.addWidget(red2)
        vcontent.addWidget(checb)
        vcontent.addWidget(buttonOk)
        frame1.setLayout(vcontent)
        hskelet.addWidget(label)
        hskelet.addWidget(frame1)
        frame.setLayout(hskelet)

        self.setCentralWidget(frame)


app = QApplication(sys.argv)

window = mainStart()
window.show()

app.exec_()
