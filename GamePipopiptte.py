# Jeu Pipopipette
#____________________________________

from math import *
from tkinter import *
from tkinter import messagebox
#- Crée d'une zone de dessin et zone information -

#- Créé fenêtre prinicpale -
fenetre = Tk()
fenetre.title('Pipopipette')
fenetre.geometry ("710x710")

Largeur = 550
Hauteur = Largeur
zone_dessin = Canvas(fenetre,width=Largeur,height=Hauteur,bg="white",bd=8)
zone_dessin.pack()
zone_info = Canvas(fenetre,width=Largeur,height=20,bg="white",bd=8)
zone_info.pack()

#- information sur les joueurs : tableau [nom, couleur, score] dans zone_info -
i_joueur=0
joueurs =[["Joueur n°1",'red'],["Joueur n°2",'green']]
scores=[0,0]

#- Nombre de cases du carré -
n=5

#- Variables options graphiques -
bordure=20
taille_pt=10
pas = (Largeur- 2*bordure)/n

#- Coordonnées dans grille après clic -
xh=bordure
xb=bordure
yh=bordure
yb=bordure

#- Initialise les tableaux -
horizontales = [False] * (n * (n + 1))
verticales = [False] * (n * (n + 1))
nb_carre = [' '] * (n ** 2)


def affiche_joueur():
    global joueurs, scores
    #- joueur n°0 -
    info_joueur0=Label (zone_info,text=joueurs[0][0]+'--> score : '+str(scores[0]))
    info_joueur0.config(fg=joueurs[0][1])
    info_joueur0.grid(row=0, sticky=E)
    #- joueur n°1 -
    info_joueur1=Label (zone_info,text=joueurs[1][0]+'--> score : '+str(scores[1]))
    info_joueur1.config(fg=joueurs[1][1])
    info_joueur1.grid(row=1, sticky=E)


def change_joueur(i_joueur):
    global joueurs
    score=str(scores[i_joueur])
    if i_joueur==1 :
        i_joueur=0
    else :
        i_joueur=1
    return i_joueur


#- Cherche la corde entre pos1 et pos2 dans hor_lins et verticales -
def cree_corde(pos1, pos2, horizontales, verticales):
    if pos1 > pos2:
        pos1, pos2 = pos2, pos1
    if (pos1 + 1) % (n + 1) == 0 and pos2 % (n + 1) == 0:
        return False
    if pos2 - pos1 == n + 1:
        return verticales[pos1]
    elif pos2 - pos1 == 1:
        return horizontales[pos1 - ((pos1 + 1) // (n + 1))]
    else:
        return False


def ferme_un_carre(pos1, pos2, pos3, pos4, horizontales, verticales):
    all = [pos1, pos2, pos3, pos4]
    all.sort()
    for i in all:
        if i < 0 or i > (((n + 1) ** 2) - 1):
            return False
    if (cree_corde(all[0], all[1], horizontales, verticales) and cree_corde(all[2], all[3], horizontales, verticales)) and (
                cree_corde(all[0], all[2], horizontales, verticales) and cree_corde(all[1], all[3], horizontales, verticales)):
        return True
    else:
        return False


def cree_carre(pos1, pos2, horizontales, verticales,i_joueur):
    global joueurs, pas
    carres_crees=[]
    if pos1 > pos2:
        pos1, pos2 = pos2, pos1
    if pos2 - pos1 == n + 1:
        verticales[pos1] = True
        check = ferme_un_carre(pos1, pos2, pos1 - 1, pos2 - 1, horizontales, verticales)
        if check:
            dessine_carre (pos1,pos2,pos1 -1, pos2 - 1,i_joueur)
            carres_crees.append(pos1 - 1)
        check = ferme_un_carre(pos1, pos2, pos1 + 1, pos2 + 1, horizontales, verticales)
        if check:
            dessine_carre (pos1,pos2,pos1 + 1, pos2 + 1,i_joueur)
            carres_crees.append(pos1)
        return carres_crees
    elif pos2 - pos1 == 1:
        horizontales[pos1 - ((pos1 + 1) // (n + 1))] = True
        carres_crees = []
        check = ferme_un_carre(pos1, pos2, pos1 - (n + 1), pos2 - (n + 1), horizontales, verticales)
        if check:
            dessine_carre (pos1,pos2,pos1 -(n+1), pos2 - (n+1),i_joueur)
            carres_crees.append(pos1 - (n + 1))
        check = ferme_un_carre(pos1, pos2, pos1 + (n + 1), pos2 + (n + 1), horizontales, verticales)
        if check:
            dessine_carre (pos1,pos2,pos1 + (n+1), pos2 + (n+1),i_joueur)
            carres_crees.append(pos1)
        return carres_crees
    else:
        pass


#-------------------------------

#- Retourne une coordonnée graphique x_cord en coordonnées dans la grille (n+1)x(n+1) -
def get_x_case(x_coord):
    global bordure, pas
    return round(max([0,(x_coord-bordure)])/pas,0)


#- Retourne une coordonnée x_grille de la grille (n+1)x(n+1) en coordonnées graphiques -
def get_x_coord (x_grille):
    global bordure, pas
    return pas*x_grille+bordure


#- dessine carre à partir des positions des points pos1 à pos4, avec la couleur du joueur le_joueur -
def dessine_carre (pos1,pos2,pos3,pos4,le_joueur):
    global joueurs
    all = [pos1, pos2, pos3, pos4]
    all.sort()
    a=int(get_x_coord (all[0]//(n+1)))
    b=int(get_x_coord (all[0] % (n+1)))
    c=int(get_x_coord (all[3] // (n+1)))
    d=int(get_x_coord (all[3] %(n+1)))
    zone_dessin.create_rectangle(b,a,d,c,fill=joueurs[le_joueur][1],width=4)


#- Créer grille initiale -
def creer_grille():
    global n, taille_pt, bordure, pas
    #- Trace quadriallage : lignes verticales -
    for i in range(n+1):
        x1=bordure+i*pas
        y1=bordure
        x2=x1
        y2=(n*pas)+bordure
        zone_dessin.create_line(x1,y1,x2,y2,fill="grey",width=1)
    #- Trace quadriallage : lignes horizontales -
    for i in range(n+1):
        x1=bordure
        y1=bordure+i*pas
        x2=(n*pas)+bordure
        y2=y1
        zone_dessin.create_line(x1,y1,x2,y2,fill="grey",width=1)

    info_joueur=Label (zone_info,text=joueurs[i_joueur][0])
    info_joueur.config(fg=joueurs[i_joueur][1])
    info_joueur.grid(row=0, sticky=E)

    #- Associe souris sur clic gauche appel à la fonction Clic() -
    zone_dessin.bind("<Button-1>", Clic)
    zone_dessin.pack(padx =5, pady =5)


#- A partir d'une position graphique (x,y), renvoie la corde (horizontale ou verticale) et les positions des 2 points de la corde dans la grille
def choix_corde(x,y,bordure,pas):
    global joueurs, verticales, horizontales, xh, yh, xb, yb, dots, pos1, pos2
    xgrille_brut=max([0,(x-bordure)])/pas
    ygrille_brut=max([0,(y-bordure)])/pas
    xgrille = round(xgrille_brut,0)
    ygrille = round(ygrille_brut,0)
    #- détermine la corde choisie
    xy_plus_pres='x'
    if abs(xgrille_brut-xgrille)>abs(ygrille_brut-ygrille) :
        xy_plus_pres='y'
    if xy_plus_pres == 'x' :
        xh=xb=xgrille
        if ygrille_brut-ygrille < 0 :
            yh=int(max([0,ygrille-1]))
            yb=int(ygrille)
        else:
            yh=int(ygrille)
            yb=int(min([n,ygrille+1]))
    else :
        yh=yb=ygrille
        if xgrille_brut-xgrille < 0 :
            xh=int(max([0,xgrille-1]))
            xb=int(xgrille)
        else:
            xh=int(xgrille)
            xb=int(min([n,xgrille+1]))
    #- trace la corde
    x1= get_x_coord (xh)
    y1= get_x_coord (yh)
    x2= get_x_coord (xb)
    y2= get_x_coord (yb)

    xh=int(get_x_case (x1))
    yh=int(get_x_case (y1))
    xb=int(get_x_case (x2))
    yb=int(get_x_case (y2))


    #- conversion coordonnées grilles (x,y) en position ou ordre de 0 à n.n-1
    pos1=yh*(n+1) + xh
    pos2=yb*(n+1) + xb


def Clic (event):
    global xh, yh, xb, yb, i_joueur, joueurs, dots, horizontales, verticales, scores
    choix_corde(event.x, event.y, bordure, pas)
    carres_crees=[]
    if pos2 - pos1 == n + 1:
        #- une verticale -
        if verticales[pos1] == True :
            messagebox.showerror("Côté déjà choisi", "Recommencez")
        else :
            zone_dessin.create_line(get_x_coord (xh),get_x_coord (yh),get_x_coord (xb),get_x_coord (yb),fill=joueurs[i_joueur][1],width=4)
            carres_crees=cree_carre(pos1, pos2, horizontales, verticales,i_joueur)
            if len(carres_crees)==0 :
                i_joueur=change_joueur (i_joueur)
            else :
                scores[i_joueur] = scores[i_joueur]+len(carres_crees)
    elif pos2 - pos1 == 1:
        #- une horizontale -
        if horizontales[pos1 - ((pos1 + 1) // (n + 1))] == True :
            messagebox.showerror("Côté déjà choisi", "Recommencez")
        else :
            zone_dessin.create_line(get_x_coord (xh),get_x_coord  (yh),get_x_coord (xb),get_x_coord (yb),fill=joueurs[i_joueur][1],width=4)
            carres_crees=cree_carre(pos1, pos2, horizontales, verticales,i_joueur)
            if len(carres_crees)==0 :
                i_joueur=change_joueur (i_joueur)
            else :
                scores[i_joueur] = scores[i_joueur]+len(carres_crees)
    else :
        pass
    if scores[0]+scores[1]>=(n*n) :
        gagnant = "joueur n°1 gagne avec "+str(scores[0])
        if scores[1]>scores[0] :
            gagnant = "joueur n°2 gagne avec "+str(scores[0])
        elif scores[1] == scores[0] :
            gagnant = "égalité "+str(scores[0])+" partout"
        messagebox.showinfo("Bravo", str(gagnant))
    affiche_joueur()




#-----------------------------------

#- Fonctions utiles pour le menu et création de celui-ci

def jouer():
    creer_grille ()


def regles_du_jeu():
    my_label=Label(fenetre, text="La Pipopipette ou « jeu des petits carrés » est un jeu de société se pratiquant à deux").pack()
    my_label=Label(fenetre, text="joueurs en tour par tour. À chaque tour, chaque joueur trace un petit trait de sa couleur suivant un quadrillage").pack()
    my_label=Label(fenetre, text="donné. Le but du jeu est de former des carrés. Le fait de fermer un carré impose de rejouer, ce qui peut ").pack()
    my_label=Label(fenetre, text="aboutir à fermer de nombreux carrés à la suite lorsque se créent des couloirs. Le gagnant est celui qui a fermé le plus de carrés.").pack()


#def nb_cases():

#- Efface la corde définie par ses coordonnées grille xh,yh,xb,yb -
def efface_corde():
    global xh,yh,xb,yb
    x1=get_x_coord (xh)
    y1=get_x_coord (yh)
    x2=get_x_coord (xb)
    y2=get_x_coord (yb)
    zone_dessin.create_line(x1,y1,x2,y2,fill="white",width=4)
    zone_dessin.create_line(x1,y1,x2,y2,fill="grey",width=1)

#- Interface via menu -
le_menu = Menu(fenetre)
fenetre.config (menu=le_menu)


#- Menu principal "Jeu"
jeu_menu = Menu(le_menu)
le_menu.add_cascade(label="Jeu", menu=jeu_menu)
jeu_menu.add_command(label="Nouveau", command=jouer)
jeu_menu.add_command(label="Quitter", command=fenetre.destroy)


#- Menu "Option"
option_menu = Menu(le_menu)
le_menu.add_cascade(label="Options", menu=option_menu)
option_menu.add_command(label="Règles du jeu", command=regles_du_jeu)
#option_menu.add_command(label="Cases", command=menu_test)
option_menu.add_command(label="Undo", command=efface_corde)


fenetre.mainloop()

