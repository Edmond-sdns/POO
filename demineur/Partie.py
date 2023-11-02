from Grille import Grille
from Case import Mine,Indication,Vide


class Partie(object):
    def __init__(self,n_lignes,n_colonnes,n_bombes):
        self.n_lignes = n_lignes
        self.n_colonnes = n_colonnes
        self.n_bombes = n_bombes
        self.etat = 1
        self.n_cases_non_decouvertes = n_lignes*n_colonnes
        
        
    def creer_grille(self):
        grille = Grille(self.n_lignes,self.n_colonnes,self.n_bombes)
        return grille
    
    def afficher(self,grille):
        #test partie sans graphisme
        n_l = 0
        n_c = 0
        grille_ll = grille.grille_ll
        print (" \t",end='')
        for _ in grille_ll[0]:
            print (n_c,"\t",end='')
            n_c+=1
        print()
        for ligne in grille_ll:
            print (n_l," \t",end='')
            n_l+=1
            for el in ligne:
                if el.etat == 1 :
                    if isinstance(el, Vide):
                        print ("-\t", end='')
                    elif isinstance(el, Mine):
                        print ('*\t',end='')
                    else:
                        print (el.n_voisins,"\t",end='')
                elif el.etat == 2:
                    print ("!\t",end='')
                else :
                    print ("#\t",end='')
            print("\n")
        print (f'Il reste {self.n_bombes} bombes')
        if self.n_bombes == 0 and grille.n_mines == self.n_cases_non_decouvertes:
            self.etat = 0
            print("Vous avez gagné")