

from PyQt5.QtWidgets import (QWidget,QPushButton, QGridLayout)
from Case import Mine,Indication,Vide
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QMouseEvent
import numpy as np
 
class AffichageGrille(QWidget):
 
    def __init__(self,grille,partie):
        super().__init__()
        self.initUI(grille,partie)
     
    def initUI(self,grille,partie):   
        grid = QGridLayout()  
        self.setLayout(grid)
      
        self.n_lignes = grille.n_lignes
        self.n_colonnes = grille.n_colonnes
        self.cases = {}  # Dictionnaire pour garder la trace de l'état de chaque case

        positions = [(i, j) for i in range(self.n_lignes) for j in range(self.n_colonnes)]
      
        for position in positions:
            cont_case = grille.grille_ll[position[0]][position[1]]
            # print (type(cont_case),cont_case.etat)

            case = QPushButton()
            case.setContextMenuPolicy(Qt.CustomContextMenu)  # Active le menu contextuel
            case.customContextMenuRequested.connect(lambda _, pos=position: self.rightClickCase(pos,grille,partie))  # Gère le clic droit
    
            
            if cont_case.etat == 1:
                case.setStyleSheet("font-size:30px;background-color:blue")
                if isinstance(cont_case, Indication):
                    case.setText(str(cont_case.n_voisins))
            # case.coord = (position[0],position[1])
            # case.clicked.connect(lambda _, coord=case.coord: self.clickCase(coord))
            case.clicked.connect(lambda _, pos=position: self.leftClickCase(pos,grille,partie))  # Gère le clic gauche
           
            case.setFixedSize(50,50)
            coord = (position[0],position[1])
            case.coord = coord
            self.cases[coord] = case 
            grid.addWidget(case, *position)
            
            
            
        grid.setSpacing(1)
      
        self.move(300, 150)
        self.setWindowTitle('Démineur')  
        self.show()
        
    # def clickCase(self, coord):
    #     # return (coord)
    #     sender_button = self.sender()
    #     print(sender_button)
    #     # print(self, coord)
        
    def leftClickCase(self, coord,grille,partie):
        # sender_button = self.sender()
        ancienne_grilleNP = grilleLL2grilleNP(grille)
        case_action = grille.obtenirCase(coord[0],coord[1])
        if case_action.etat == 0:
            if not isinstance(case_action,Vide):
                case_action.decouvrir(partie)
            else :
                # print("case vide")
                # tab_revel_np = grille.revelerCases(case_revelee)
                grille.revelerCases(case_action,partie)
            nouvelle_grilleNP = grilleLL2grilleNP(grille)
            self.miseAJourGrille(ancienne_grilleNP,nouvelle_grilleNP)
                
            print("Clic gauche à la coordonnée:", coord,case_action)

    def rightClickCase(self, coord,grille,partie):
        # sender_button = self.sender()
        case_action = grille.obtenirCase(coord[0],coord[1])
        if case_action.etat == 0:
            case_action.marquerCase(partie)
            print("Clic droit à la coordonnée:", coord,case_action)
    
    def miseAJourGrille(self,ancienne_grille,nouvelle_grille):
        dif = np.where(nouvelle_grille!=ancienne_grille)
        for (i,j) in zip(dif[0],dif[1]):
           self.updateCase((i,j),"font-size:30px;background-color:blue","n")
    

    
    def updateCase(self, coord, style, text):
        case = self.cases.get(coord)
        if case:
            case.setStyleSheet(style)
            case.setText(text)


def grilleLL2grilleNP(grille):
    nl = len(grille.grille_ll)
    nc = len(grille.grille_ll[0])
    grilleNP = np.zeros((nl,nc))
    for i in range (nl):
        for j in range (nc):
            grilleNP[i,j]=grille.grille_ll[i][j].etat
    return grilleNP
