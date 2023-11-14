from Grille import Grille
from Case import Mine,Indication,Vide


class Partie(object):
    '''
    Classe représentant une partie du jeu Démineur.

    Attributs:
        - n_lignes (int): Nombre de lignes de la grille.
        - n_colonnes (int): Nombre de colonnes de la grille.
        - n_bombes (int): Nombre de bombes non marquée sur la grille.
        - etat (int): État de la partie (1 en cours, 0 terminée).
        - n_cases_non_decouvertes (int): Nombre de cases non découvertes.

    Méthodes:
        - creer_grille(): Crée une nouvelle instance de la classe Grille.
        - afficher(grille): Affiche l'état de la grille, utilisé pour la partie en mode console.
    '''
    def __init__(self,n_lignes,n_colonnes,n_bombes):
        '''
        Initialise une nouvelle instance de la classe Partie.

        Args:
            n_lignes (int): Le nombre de lignes de la grille.
            n_colonnes (int): Le nombre de colonnes de la grille.
            n_bombes (int): Le nombre de bombes présentes sur la grille.
        '''
        self.n_lignes = n_lignes
        self.n_colonnes = n_colonnes
        self.n_bombes = n_bombes
        self.etat = 1
        self.n_cases_non_decouvertes = n_lignes*n_colonnes
        
        
    def creer_grille(self):
        '''
        Crée une nouvelle instance de la classe Grille.

        Returns:
            Grille: Une nouvelle grille de jeu.
        '''
        grille = Grille(self.n_lignes,self.n_colonnes,self.n_bombes)
        return grille
    
    def afficher(self,grille):
        '''
        Affiche l'état de la grille en console.

        Args:
            grille (Grille): L'instance de la grille à afficher.

        Notes:
            Utilisé principalement pour le débogage.
        '''
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