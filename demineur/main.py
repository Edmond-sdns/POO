from Grille import Grille
from Case import Mine,Indication,Vide
from Partie import Partie
from random import randint
from AffichageGrille import AffichageGrille
from PyQt5.QtWidgets import QApplication
import sys

if __name__ == '__main__':
    '''
    Principale routine du programme qui appelle les classes et les méthodes pour le jeu.
    Commenter et décommenter la partie du code voulue selon que l'on souhaite une partie en
        mode console ou en mode graphique'
    '''
    dif = {1:(9,9,10),2:(16,16,40),3:(16,30,99)} #paraméètres des grilles en fonction du niveau de difficulté
    difficulte = 1 #Niveau de difficulté par défaut
    
    n_l,n_c,n_mines = dif.get(difficulte)
    partie = Partie(n_l,n_c,n_mines)
    grille = partie.creer_grille()
    # grille_np = grille.initialiser_grille()
    grille.initialiser_grille()
    
    
    ####################### Partie en mode console ################################
    # while True:
    #     coord_debut = ((randint(0,n_l-1),randint(0,n_c-1)))
    #     if isinstance(grille.grille_ll[coord_debut[0]][coord_debut[1]],Vide):
    #         grille.revelerCases(grille.grille_ll[coord_debut[0]][coord_debut[1]],partie)
    #         break
        
    # partie.afficher(grille) 
    
    # while partie.etat == 1:
    #     action = input("Marquer une case (m) ou révéler une case (r) ? : ")
    #     coord = eval(input("Quelle case voulez-vous marquer ou révéler ? (sous la forme ligne,colonne) : "))
    #     l=coord[0]
    #     c=coord[1]
    #     case_action = grille.obtenirCase(l,c)
    #     if action == "m":
    #         case_action.marquerCase(partie)
    #     if action == "r":
    #         if not isinstance(case_action,Vide):
    #             case_action.decouvrir(partie)
    #         else :
    #             # print("case vide")
    #             # tab_revel_np = grille.revelerCases(case_revelee)
    #             grille.revelerCases(case_action,partie)
    #     partie.afficher(grille)
      
    ######################## Partie avec interface graphique ###################
    while True:
        coord_debut = ((randint(0,n_l-1),randint(0,n_c-1)))
        if isinstance(grille.grille_ll[coord_debut[0]][coord_debut[1]],Vide):
            grille.revelerCases(grille.grille_ll[coord_debut[0]][coord_debut[1]],partie)
            break

    app = QApplication.instance() 
    if not app:
        app = QApplication(sys.argv)
    affichageGrille = AffichageGrille(grille,partie)
    affichageGrille.show()
    # affichageInfos = AffichageInfos(partie)
    app.exec_()