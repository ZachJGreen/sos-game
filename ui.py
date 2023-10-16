import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QGridLayout


class Ui_MainWindow(object):
    def __init__(self):
        self.last_gridsize = 3
        self.gameboard = None
        self.layout = None
        self.turn = False
        self.testlabel = None
        self.statusbar = None
        self.label = None
        self.turn_label = None
        self.frame = None
        self.gridsize_selector = None
        self.gridsize_label = None
        self.center_section = None
        self.p2_o = None
        self.p2_s = None
        self.p2_label = None
        self.right_section = None
        self.p1_o = None
        self.p1_s = None
        self.p1_label = None
        self.left_section = None
        self.centralwidget = None
        self.gm_simple = None
        self.gm_general = None
        print(self.turn)
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1200, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        # Player 1 Section
        self.left_section = QtWidgets.QFrame(self.centralwidget)
        self.left_section.setGeometry(QtCore.QRect(0, 0, 81, 571))
        self.left_section.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.left_section.setFrameShadow(QtWidgets.QFrame.Raised)
        self.left_section.setObjectName("left_section")

        self.p1_label = QtWidgets.QLabel(self.left_section)
        self.p1_label.setGeometry(QtCore.QRect(20, 10, 47, 13))
        self.p1_label.setObjectName("p1_label")

        self.p1_s = QtWidgets.QRadioButton(self.left_section)
        self.p1_s.setGeometry(QtCore.QRect(20, 30, 31, 17))
        self.p1_s.setChecked(True)
        self.p1_s.setObjectName("p1_s")

        self.p1_o = QtWidgets.QRadioButton(self.left_section)
        self.p1_o.setGeometry(QtCore.QRect(20, 50, 31, 17))
        self.p1_o.setObjectName("p1_o")

        # Player 2 Section
        self.right_section = QtWidgets.QFrame(self.centralwidget)
        self.right_section.setGeometry(QtCore.QRect(1030, 0, 81, 571))
        self.right_section.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.right_section.setFrameShadow(QtWidgets.QFrame.Raised)
        self.right_section.setObjectName("right_section")

        self.p2_label = QtWidgets.QLabel(self.right_section)
        self.p2_label.setGeometry(QtCore.QRect(20, 10, 47, 13))
        self.p2_label.setObjectName("p2_label")
        self.p2_s = QtWidgets.QRadioButton(self.right_section)
        self.p2_s.setGeometry(QtCore.QRect(20, 30, 31, 17))
        self.p2_s.setChecked(True)
        self.p2_s.setObjectName("p2_s")

        self.p2_o = QtWidgets.QRadioButton(self.right_section)
        self.p2_o.setGeometry(QtCore.QRect(20, 50, 31, 17))
        self.p2_o.setObjectName("p2_o")

        # Gameplay Section
        self.center_section = QtWidgets.QWidget(self.centralwidget)
        self.center_section.setGeometry(QtCore.QRect(79, -1, 951, 571))
        self.center_section.setObjectName("center_section")

        self.gridsize_label = QtWidgets.QLabel(self.center_section)
        self.gridsize_label.setGeometry(QtCore.QRect(110, 10, 71, 21))
        self.gridsize_label.setObjectName("gridsize_label")

        self.gridsize_selector = QtWidgets.QSpinBox(self.center_section)
        self.gridsize_selector.setGeometry(QtCore.QRect(160, 10, 42, 22))
        self.gridsize_selector.setMinimum(3)
        self.gridsize_selector.setObjectName("gridsize_selector")
        self.gridsize_selector.valueChanged.connect(self.getGridSize)
        self.gridsize_selector.valueChanged.connect(self.setGridSize)

        self.groupBox = QtWidgets.QGroupBox(self.center_section)
        self.groupBox.setGeometry(QtCore.QRect(760, 0, 101, 91))
        self.groupBox.setObjectName("groupBox")
        self.gm_label = QtWidgets.QLabel(self.groupBox)
        self.gm_label.setGeometry(QtCore.QRect(20, 10, 71, 20))
        self.gm_label.setObjectName("gm_label")
        self.gm_simple = QtWidgets.QRadioButton(self.groupBox)
        self.gm_simple.setGeometry(QtCore.QRect(20, 30, 82, 17))
        self.gm_simple.setObjectName("gm_simple")
        self.gm_simple.setChecked(True)
        self.gm_general = QtWidgets.QRadioButton(self.groupBox)
        self.gm_general.setGeometry(QtCore.QRect(20, 50, 82, 17))
        self.gm_general.setObjectName("gm_general")

        self.gameboard = QGridLayout(self.center_section)
        self.gameboard.setGeometry(QtCore.QRect(200, 50, 480, 480))
        self.gameboard.setObjectName("gameboard")
        self.setGridSize()

        self.turn_label = QtWidgets.QLabel(self.center_section)
        self.turn_label.setGeometry(QtCore.QRect(370, 20, 47, 13))
        self.turn_label.setObjectName("turn_label")

        self.label = QtWidgets.QLabel(self.center_section)
        self.label.setGeometry(QtCore.QRect(410, 20, 47, 13))
        self.label.setObjectName("label")

        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def getGridSize(self):
        grid = self.gridsize_selector.value()
        return grid

    def setGridSize(self):
        gridSize = self.getGridSize()

        if self.last_gridsize > gridSize:
            for i in reversed(range(self.gameboard.count())):
                self.gameboard.itemAt(i).widget().setParent(None)

        for row in range(gridSize):
            for column in range(gridSize):
                button = QtWidgets.QPushButton(text="X")
                self.gameboard.addWidget(button, row + 1, column)
        self.last_gridsize = gridSize

    def swap_turns(self):
        self.turn = not self.turn
        print(self.turn)

    def get_turn(self):
        return self.turn


    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "SOS Game"))
        self.p1_label.setText(_translate("MainWindow", "Player 1"))
        self.p1_s.setText(_translate("MainWindow", "S"))
        self.p1_o.setText(_translate("MainWindow", "O"))
        self.p2_label.setText(_translate("MainWindow", "Player 2"))
        self.p2_s.setText(_translate("MainWindow", "S"))
        self.p2_o.setText(_translate("MainWindow", "O"))
        self.gridsize_label.setText(_translate("MainWindow", "Grid Size:"))
        self.turn_label.setText(_translate("MainWindow", "Turn:"))
        self.label.setText(_translate("MainWindow", "Player 1"))
        self.gm_label.setText(_translate("MainWindow", "Game Mode:"))
        self.gm_simple.setText(_translate("MainWindow", "Simple"))
        self.gm_general.setText(_translate("MainWindow", "General"))


def setup_window():
    app = QtWidgets.QApplication(sys.argv)
    # create window
    window = QtWidgets.QMainWindow()

    ui = Ui_MainWindow()
    # fill window
    ui.setupUi(window)

    window.show()

    sys.exit(app.exec_())


setup_window()
