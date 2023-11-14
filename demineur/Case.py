
class Case(object):
    def __init__(self,etat,l,c):
        '''
           Classe représentant une case du jeu Démineur.
           
           Attributs:
               - etat (int): L'état de la case (0 cachée, 1 découverte, 2 marquée).
               - l (int): Indice de ligne de la case dans la grille.
               - c (int): Indice de colonne de la case dans la grille.
           '''
        self.etat = etat 
        self.l = l
        self.c = c
    
    def marquerCase(self,partie):
        '''
        Marque la case comme contenant une mine et met à jour le nombre de bombes restantes dans la partie.
        
        Args:
            partie (Partie): L'instance de la partie en cours.
        '''
        self.etat = 2
        partie.n_bombes-=1
    
    def decouvrir(self,partie):
        '''
        Découvre la case, met à jour l'état de la case et ajuste le nombre de cases non découvertes dans la partie.
        
        Args:
            partie (Partie): L'instance de la partie en cours.
        '''
        if self.etat != 1:
            self.etat = 1
            partie.n_cases_non_decouvertes-=1


class Mine(Case):
    '''
    Classe représentant une case contenant une mine dans le jeu Démineur.
    '''
    def __init__(self,etat,l,c):
        '''
        Initialise une nouvelle instance de la classe Mine, une sous-classe de Case.
        Appelle le constructeur de la classe mère (Case).
        '''
        Case.__init__(self,etat,l,c)
    
    def decouvrir(self,partie):
        '''
        Découvre la case contenant une mine, déclare que le joueur a perdu la partie et met à jour l'état de la partie.
        
        Args:
            partie (Partie): L'instance de la partie en cours.
        '''
        print("Vous avez perdu")
        partie.etat = 0

class Indication(Case):
    '''
    Classe représentant une case avec une indication du nombre de mines voisines dans le jeu Démineur.
    '''
    def __init__(self,etat,l,c,n_voisins):
        '''
       Initialise une nouvelle instance de la classe Indication, une sous-classe de Case.
       Appelle le constructeur de la classe mère (Case) et ajoute un attribut spécifique.
       
       Args:
           n_voisins (int): Le nombre de mines voisines.
       '''
        Case.__init__(self,etat,l,c)
        self.n_voisins = n_voisins
    
       
class Vide(Case):
    '''
   Classe représentant une case vide dans le jeu Démineur.
   '''
    def __init__(self,etat,l,c):
        '''
        Initialise une nouvelle instance de la classe Vide, une sous-classe de Case.
        Appelle le constructeur de la classe mère (Case).
        '''
        Case.__init__(self,etat,l,c)
        