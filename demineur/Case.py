
class Case(object):
    def __init__(self,etat,l,c):
        # self.bombe = bombe
        self.etat = etat # 0 cachée, 1 découverte
        self.l = l
        self.c = c
    
    def marquerCase(self,partie):
        self.etat = 2
        partie.n_bombes-=1
    
    def decouvrir(self,partie):
        if self.etat != 1:
            self.etat = 1
            partie.n_cases_non_decouvertes-=1
            # print(f'Nombres de cases non découvertes : {partie.n_cases_non_decouvertes}')


class Mine(Case):
    def __init__(self,etat,l,c):
        Case.__init__(self,etat,l,c)
    
    def decouvrir(self,partie):
        print("Vous avez perdu")
        partie.etat = 0

class Indication(Case):
    def __init__(self,etat,l,c,n_voisins):
        Case.__init__(self,etat,l,c)
        self.n_voisins = n_voisins
    
       
class Vide(Case):
    def __init__(self,etat,l,c):
        Case.__init__(self,etat,l,c)
        