
from PyQt5.QtWidgets import (QWidget,QPushButton, QGridLayout,QLabel,QLineEdit,QVBoxLayout,QHBoxLayout)
from Case import Mine,Indication,Vide
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QMouseEvent,QIcon
import numpy as np
 
class AffichageInfos(QWidget):
 
    def __init__(self,partie):
        super().__init__()
        self.initUI(partie)
     
    def initUI(self,partie):
        widget = QWidget()
        # self.move(800, 150)
        # # on fixe la taille de la fenêtre
        # self.resize(500,250)
        self.setGeometry(800, 150, 500, 250)
        self.setWindowTitle('Partie démineur')  
        
        
        # lbl1 = QLabel('ZetCode', self)
        # lbl1.move(15, 10)

        # lbl2 = QLabel('tutorials', self)
        # lbl2.move(35, 40)

        # lbl3 = QLabel('for programmers', self)
        # lbl3.move(55, 70)

        choix_dif = QLabel('Choix de la difficulté (1,2,3) : ')
        dif_edit = QLineEdit()
        n_mines = QLabel(f'Nombre de mines restantes: {partie.n_bombes}')
        
        
        
        
        self.show()
        
        

