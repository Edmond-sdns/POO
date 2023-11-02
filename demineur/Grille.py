from Case import Vide,Indication,Mine

import random
import numpy as np

class Grille(object):
    def __init__(self,n_lignes,n_colonnes,n_mines):
        self.n_lignes = n_lignes
        self.n_colonnes = n_colonnes
        self.n_mines = n_mines
        
    def initialiser_grille(self):
        # Génération des position des mines
        l_pos_all = [(y,x) for x in range(self.n_colonnes) for y in range(self.n_lignes)]
        random.shuffle(l_pos_all)
        l_pos_mines = l_pos_all[:self.n_mines]
        
        #Création d'une version numpy de la grille pour le calcul des indices
        grille_np = np.zeros((self.n_lignes,self.n_colonnes))
        for pos in l_pos_mines:
            grille_np[pos[0],pos[1]] = 100
        for l in range (self.n_lignes):
            for c in range (self.n_colonnes):
                if grille_np[l,c] != 100:
                    zone = grille_np[max(0,l-1):min(self.n_lignes,l+2),max(0,c-1):min(self.n_colonnes,c+2)]
                    sum_zone = np.sum(zone)
                    n_mines = int(sum_zone/100)
                    grille_np[l,c] = n_mines
        
        #Création des objets Case et enregistrement dans une liste de liste
        grille_ll = grille_np.tolist()
        for l in range (self.n_lignes):
            for c in range (self.n_colonnes):
                if grille_np[l,c] == 0:
                    grille_ll[l][c] = Vide(0,l,c)
                elif grille_np[l,c] == 100:
                    grille_ll[l][c] = Mine(0,l,c)
                else :
                    grille_ll[l][c] = Indication(0, l, c, int(grille_np[l,c]))
        self.grille_ll = grille_ll
        # return (grille_np)

    def obtenirCase(self,l,c):
        case_revelee = self.grille_ll[l][c]
        return case_revelee
    
    def revelerCases(self,case,partie):
        # print(case)
        # print('itération suivante')
        l = case.l
        c = case.c
        l_max = len(self.grille_ll)-1
        c_max = len(self.grille_ll[0])-1
        l_coord_env = [(max(0,l-1),c),(l,max(0,c-1)),(min(l_max,l+1),c),(l,min(c_max,c+1))]
        if self.grille_ll[l][c].etat != 1:
            # self.grille_ll[l][c].etat = 1
            case.decouvrir(partie)
            for coord in l_coord_env :
                case = self.grille_ll[coord[0]][coord[1]]
                if not isinstance(case,Indication):
                    self.revelerCases(case,partie)
                case.decouvrir(partie)
        # tab_revel_np = np.zeros((l_max+1,c_max+1))
        # for l in range(l_max+1):
        #     for c in range(c_max+1):
        #         tab_revel_np[l,c] = self.grille_ll[l][c].etat
        # return tab_revel_np
    
