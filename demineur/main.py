from Grille import Grille
from Case import Mine,Indication,Vide
from Partie import Partie
from random import randint

if __name__ == '__main__':
    n_l = 9
    n_c = 9
    n_mines = 10
    partie = Partie(n_l,n_c,n_mines)
    grille = partie.creer_grille()
    # grille_np = grille.initialiser_grille()
    grille.initialiser_grille()
    
    while True:
        coord_debut = ((randint(0,n_l-1),randint(0,n_c-1)))
        if isinstance(grille.grille_ll[coord_debut[0]][coord_debut[1]],Vide):
            grille.revelerCases(grille.grille_ll[coord_debut[0]][coord_debut[1]],partie)
            break
        
    partie.afficher(grille) 
    
    while partie.etat == 1:
        action = input("Marquer une case (m) ou révéler une case (r) ? : ")
        coord = eval(input("Quelle case voulez-vous marquer ou révéler ? (sous la forme ligne,colonne) : "))
        l=coord[0]
        c=coord[1]
        case_action = grille.obtenirCase(l,c)
        if action == "m":
            case_action.marquerCase(partie)
        if action == "r":
            if not isinstance(case_action,Vide):
                case_action.decouvrir(partie)
            else :
                # print("case vide")
                # tab_revel_np = grille.revelerCases(case_revelee)
                grille.revelerCases(case_action,partie)
        partie.afficher(grille)