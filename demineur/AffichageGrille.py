

from PyQt5.QtWidgets import (QWidget,QPushButton, QGridLayout,QLabel,QComboBox,QApplication)
from Case import Mine,Indication,Vide
from Partie import Partie
from Grille import Grille
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QMouseEvent,QIcon
import numpy as np
from random import randint
import sys
 
class AffichageGrille(QWidget):
    '''
   Classe représentant l'affichage de la grille de jeu Démineur.

   Attributs:
       - n_lignes (int): Nombre de lignes de la grille.
       - n_colonnes (int): Nombre de colonnes de la grille.
       - cases (dict): Dictionnaire pour garder la trace de l'état de chaque case.

   Méthodes:
       - initUI(grille, partie): Initialise l'interface utilisateur.
       - leftClickCase(coord, grille, partie): Gère le clic gauche sur une case.
       - rightClickCase(pos, grille, partie): Gère le clic droit sur une case.
       - changeDifficulty(index): Change le niveau de difficulté en fonction de la sélection dans la liste déroulante.
       - miseAJourGrille(ancienne_grille, nouvelle_grille, grille): Met à jour l'affichage de la grille.
       - perdu(): Affiche le message de défaite.
       - gagne(): Affiche le message de victoire.
   '''
 
    def __init__(self,grille,partie):
        '''
       Initialise une nouvelle instance de la classe AffichageGrille.

       Args:
           grille (Grille): L'instance de la grille de jeu.
           partie (Partie): L'instance de la partie en cours.
       '''
        super().__init__()
        self.initUI(grille,partie)
     
    def initUI(self,grille,partie):  
        '''
        Initialise l'interface utilisateur.

        Args:
            grille (Grille): L'instance de la grille de jeu.
            partie (Partie): L'instance de la partie en cours.
        '''
        grid = QGridLayout()  
        self.setLayout(grid)
      
        self.n_lignes = grille.n_lignes
        self.n_colonnes = grille.n_colonnes
        self.cases = {}  # Dictionnaire pour garder la trace de l'état de chaque case

        positions = [(i, j) for i in range(self.n_lignes) for j in range(self.n_colonnes)]
      
        for position in positions:
            cont_case = grille.grille_ll[position[0]][position[1]]

            case = QPushButton()
            case.setContextMenuPolicy(Qt.CustomContextMenu)  # Active le menu contextuel
            case.customContextMenuRequested.connect(lambda _, pos=position: self.rightClickCase(pos,grille,partie))  # Gère le clic droit
    
            
            if cont_case.etat == 1:
                case.setStyleSheet("font-size:30px;background-color:blue")
                if isinstance(cont_case, Indication):
                    case.setText(str(cont_case.n_voisins))
           
            case.clicked.connect(lambda _, pos=position: self.leftClickCase(pos,grille,partie))  # Gère le clic gauche
           
            case.setFixedSize(50,50)
            coord = (position[0],position[1])
            case.coord = coord
            self.cases[coord] = case 
            grid.addWidget(case, *position)
            
            
            
        grid.setSpacing(1)
        
        self.n_mines = QLabel(f'Nombre de mines restantes: {partie.n_bombes}')
        self.n_mines.setStyleSheet('font-size: 30px')
        grid.addWidget(self.n_mines,self.n_lignes,0,1,9)
        
        
        # Ajoutez la zone de sélection pour le niveau de difficulté
        difficulty_label = QLabel('Niveau de difficulté:')
        difficulty_label.setStyleSheet('font-size: 20px')
        grid.addWidget(difficulty_label, self.n_lignes + 1, 0, 1, 4)

        difficulty_combobox = QComboBox()
        difficulty_combobox.addItems(['Niveau','Facile', 'Moyen', 'Difficile'])
        difficulty_combobox.currentIndexChanged.connect(self.changeDifficulty)
        grid.addWidget(difficulty_combobox, self.n_lignes + 1, 4, 1, 3)
        
        
        self.move(300, 150)
        self.setWindowTitle('Démineur')  
        self.show()
        
        
    def leftClickCase(self, coord,grille,partie):
        '''
       Gère le clic gauche sur une case.

       Args:
           coord (tuple): Coordonnées de la case cliquée.
           grille (Grille): L'instance de la grille de jeu.
           partie (Partie): L'instance de la partie en cours.
        '''

        ancienne_grilleNP = grilleLL2grilleNP(grille)
        case_action = grille.obtenirCase(coord[0],coord[1])
        if (case_action.etat == 0 or case_action.etat == 2) and partie.etat == 1:
            if case_action.etat == 2:
                case_action.etat = 0
                case = self.cases.get(coord)
                case.setIcon(QIcon(''))
            if not isinstance(case_action,Vide):
                case_action.decouvrir(partie)
                if isinstance(case_action, Mine):
                    case = self.cases.get(coord)
                    case.setIcon(QIcon('img/bombe.png'))
                    self.updateCase((coord),"font-size:30px;background-color:blue","")
            else :
                # print("case vide")
                # tab_revel_np = grille.revelerCases(case_revelee)
                grille.revelerCases(case_action,partie)
            nouvelle_grilleNP = grilleLL2grilleNP(grille)
            self.miseAJourGrille(ancienne_grilleNP,nouvelle_grilleNP,grille)
            if partie.etat == 0:
                self.perdu()
            if partie.n_bombes == 0 and grille.n_mines == partie.n_cases_non_decouvertes:
                partie.etat = 0
                self.gagne()

    def rightClickCase(self, coord,grille,partie):
        '''
        Gère le clic droit sur une case.

        Args:
            coord (tuple): Coordonnées de la case cliquée.
            grille (Grille): L'instance de la grille de jeu.
            partie (Partie): L'instance de la partie en cours.
        '''
        case_action = grille.obtenirCase(coord[0],coord[1])
        if case_action.etat == 0 and partie.etat == 1:
            case_action.marquerCase(partie)
            case = self.cases.get(coord)
            case.setIcon(QIcon('img/drapeau.png')) 
            self.n_mines.setText(f'Nombre de mines restantes: {partie.n_bombes}')
            if partie.n_bombes == 0 and grille.n_mines == partie.n_cases_non_decouvertes:
                partie.etat = 0
                self.gagne()
            
    def changeDifficulty(self, index):
        '''
        Change le niveau de difficulté en fonction de la sélection dans la liste déroulante.

        Args:
            index (int): L'index de la sélection dans la liste déroulante.
        '''
        difficulty = index  # Niveaux de difficulté: 1, 2, 3
        print("Niveau de difficulté choisi:", difficulty)
        dif = {1:(9,9,10),2:(16,16,40),3:(16,30,99)}

        
        n_l,n_c,n_mines = dif.get(difficulty)
        partie = Partie(n_l,n_c,n_mines)
        grille = partie.creer_grille()
        # grille_np = grille.initialiser_grille()
        grille.initialiser_grille()
        
        while True:
            coord_debut = ((randint(0,n_l-1),randint(0,n_c-1)))
            if isinstance(grille.grille_ll[coord_debut[0]][coord_debut[1]],Vide):
                grille.revelerCases(grille.grille_ll[coord_debut[0]][coord_debut[1]],partie)
                break
    
        self.close()
    
        app = QApplication.instance() 
        if not app:
            app = QApplication(sys.argv)
        affichageGrille = AffichageGrille(grille,partie)
        affichageGrille.show()
        # affichageInfos = AffichageInfos(partie)
        app.exec_()
    
    

    
    def miseAJourGrille(self,ancienne_grille,nouvelle_grille,grille):
        '''
       Met à jour l'affichage de la grille.

       Args:
           ancienne_grille (numpy.ndarray): Ancienne grille.
           nouvelle_grille (numpy.ndarray): Nouvelle grille.
           grille (Grille): L'instance de la grille de jeu.
       '''
        dif = np.where(nouvelle_grille!=ancienne_grille)
        for (i,j) in zip(dif[0],dif[1]):
            case_action = grille.obtenirCase(i,j)
            if isinstance(case_action,Indication):
                txt = str(case_action.n_voisins)
            else:
                txt = ""
            self.updateCase((i,j),"font-size:30px;background-color:blue",txt)
    

    
    def updateCase(self, coord, style, text):
        '''
        Met à jour l'apparence d'une case.

        Args:
            coord (tuple): Coordonnées de la case.
            style (str): Style CSS de la case.
            text (str): Texte à afficher dans la case.
        '''
        case = self.cases.get(coord)
        if case:
            case.setStyleSheet(style)
            case.setText(text)
    
    def perdu(self):
        '''Affiche le message de défaite.'''
        self.n_mines.setText("Vous avez perdu !!!")
        
    def gagne(self):
        '''Affiche le message de victoire.'''
        self.n_mines.setText("Vous avez gagné !!!")


def grilleLL2grilleNP(grille):
    '''
    Convertit la grille de liste de listes en tableau numpy.

    Args:
        grille (Grille): L'instance de la grille de jeu.

    Returns:
        numpy.ndarray: La grille convertie en tableau numpy.
    '''
    nl = len(grille.grille_ll)
    nc = len(grille.grille_ll[0])
    grilleNP = np.zeros((nl,nc))
    for i in range (nl):
        for j in range (nc):
            grilleNP[i,j]=grille.grille_ll[i][j].etat
    return grilleNP
