import sys
from PyQt5.QtWidgets import QWidget, QApplication, QMainWindow, QVBoxLayout, QHBoxLayout, QPushButton, QGridLayout
from PyQt5.QtGui import QIcon
import menu_bar
import tool_bar
import side_menu
import tabs_area
import status_bar


class HospitalMgmt():

    def __init__(self):
        app = QApplication(sys.argv)
        with open('./styles/styles.qss','r') as f:
            app.setStyleSheet(f.read())

        # Window formating
        window = QMainWindow()
        window.setWindowTitle('Walz Hospital Mangement System')
        window.resize(897, 726)
        window.setWindowIcon(QIcon('./icons/clinic.png'))

        # window.setGeometry(200,200,300,200)
        centralwidget = QWidget(window)
        gridLayout = QGridLayout()
        verticalLayout = QVBoxLayout(centralwidget)

        # hot_stuff = tabs_area.TabsArea()
        tool_bar.ToolBar(window)

        tabs = tabs_area.TabsArea(centralwidget, gridLayout)
        # tabs.right_tabwidget.hide()
        menu_bar.MenuBar(window,tabs)

        side_menu.SideMenu(centralwidget, gridLayout, tabs)
        verticalLayout.addLayout(gridLayout)
        window.setCentralWidget(centralwidget)

        status_bar.StatusBar(window)

        window.show()
        app.exec_()


HospitalMgmt()
