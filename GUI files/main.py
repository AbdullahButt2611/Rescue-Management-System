import sys
import platform
from pySide2 import QtCore, QtGui, QtWidgets
from pySide2.QtWidgets import *


class SplashScreen(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        # self.ui =