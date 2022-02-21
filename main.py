from numpy import maximum


j = 1
tableau = [['-'] * 3 for i in range(3)]
continuer = True
jouer = True


def print_tableau():
    print(tableau[0], "ligne 1")
    print(tableau[1], "ligne 2")
    print(tableau[2], "ligne 3")

def win():
    colonne = ligne = diagonal = maximum = 0
    for i in range(3):
        i - 1
        liste = "".join(tableau[i])
        if liste == 'x'*3 or liste == 'o'*3:
            ligne = 1

    for i in [0, 1, 2]:
        liste = []
        for v in [0, 1, 2]:
            liste.append(tableau[v][i])
        liste1 = "".join(liste)
        if liste1 == 'x'*3 or liste1 == 'o'*3:
            colonne = 1

    if tableau[0][0] == tableau[1][1] and tableau[1][1] == tableau[2][2] and tableau[0][0] == 'x':
        diagonal = 1
    if tableau[0][0] == tableau[1][1] and tableau[1][1] == tableau[2][2] and tableau[0][0] == 'o':
        diagonal = 1
    if tableau[2][0] == tableau[1][1] and tableau[1][1] == tableau[0][2] and tableau [2][0] == 'x':
        diagonal = 1
    if tableau[2][0] == tableau[1][1] and tableau[1][1] == tableau[0][2] and tableau [2][0] == 'o':
        diagonal = 1

    for i in [0, 1, 2]:
        liste = []
        for v in [0, 1, 2]:
            liste.append(tableau[v][i])
        if '-' not in liste1:
            maximum = 1


    if colonne == 1 or ligne == 1 or diagonal == 1:
        print("Le jeu est terminé, un des deux joueurs a gagné !")
        return True

    if maximum == 1:
        print("La partie est terminée ! Egalité !")
        return True


def choix():
    global x
    global y 
    x = input("Veuillez donner la colonne : ")
    y = input("Veuillez donner la ligne : ")
    x = int(x) - 1
    y = int(y) - 1

def dessine_tableau():
    global p
    if j == 1:
        if tableau[y][x] != '-':
            print('Cette case est déjâ prise !')
            p = 1        
        else:
            tableau[y][x] = "o"
            p = 0
    else:
        if tableau[y][x] != '-':
            print('Cette case est déjâ prise !')
            p = 1          
        else:
            tableau[y][x] = "x"
            p = 0

if __name__ == '__main__':
    while continuer:
        j = 1
        tableau = [['-'] * 3 for i in range(3)]
        continuer = True
        jouer = True
        print("Voici la grille de jeu:")
        print(print_tableau())
        print("Voila une nouvelle partie qui commence ! ")
        while jouer:
            if j == 1:
                print("C'est au tour du joueur 1 (croix).")
                j = j + 1
            else:
                print("C'est au tour du joueur 2 (rond).")
                j = j - 1
            choix()
            dessine_tableau()
            while p == 1:
                choix()
                dessine_tableau()
            print_tableau()
            if win():
                jouer = False

        oui =  input('Refaire une partie ? oui/non : ')
        if oui == "non":
            continuer = False

