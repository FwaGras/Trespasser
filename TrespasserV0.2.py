import random

def print_lines(*lines):
    """
    A helpful function for printing many
    separate strings on separate lines. (source : https://codereview.stackexchange.com/questions/94116/turn-based-battle-simulator)
    """
    print("\n".join([line for line in lines]))

def combat():
    """
    S'occupe du déroulement du combat : prend en compte l'action choisi par le joueur et s'occupe du comportement
    de l'ennemi. Renvoie les stats modifiés des personnages.
    """
    global Attaque2, Attaque, nb_objet1
    rejouer = True
    
    #mise en place de la boucle rejouer
    while rejouer:
        gagnant = None
    
        tourJoueur = True #Trespasser commence toujours en premier à chaque partie
        tourOrdi = False
    
        #mise en place de la boucle du jeu
        while (Fiche1['PV'] != 0 or Fiche2['PV'] != 0):
        
            soin = False #Détermine si un premier soin a été utilisé
            récup = False #Détermine si une ration a été utilisé
            
            if tourJoueur: #C'est au tour du joueur
                #L'attaque choisie inflige des dégâts à l'ennemi et consomme de l'énergie
                if Attaque == Fiche1['Attaques'][0]:
                    Attaque = 35 # Dgts de Trespass
                    print("Trespasser utilise", Fiche1['Attaques'][0][0], "cela fait", Fiche1['Attaques'][0][1],"dégats!" )
                    Fiche1['EN'] -= Fiche1['Attaques'][0][2]
                elif Attaque == Fiche1['Attaques'][1]:
                    Attaque = 15 # Dgts de Slash
                    print("Trespasser utilise", Fiche1['Attaques'][1][0], "cela fait", Fiche1['Attaques'][1][1],"dégats!" )
                    Fiche1['EN'] -= Fiche1['Attaques'][1][2]
                elif Attaque == Fiche1['Attaques'][2]:
                    Attaque = 25 # Dgts de Devil's Dance
                    print("Trespasser utilise", Fiche1['Attaques'][2][0], "cela fait", Fiche1['Attaques'][2][1],"dégats!" )
                    Fiche1['EN'] -= Fiche1['Attaques'][2][2]
                else:
                    if Objet == "premier soin":
                        soin = True #activation du heal
                        nb_objet1 -= 1
                        print("Trespasser utilise Premier soin!", 35,"PV soignés!")
                    elif Objet == "ration":
                        récup = True #activation de la récupération d'énergie
            
            else: #tour de l'ordi
                Attaque2 = random.randint(1,3) #Choisi au hasard une action (oui c'est une IA stupide)
                if Attaque2 == 1:
                    Attaque2 = 30 # Dgts de Longinus
                    print("Legarde utilise", Fiche2['Attaques'][0][0], "cela fait", 30, "dégâts!")
                    
                    
                elif Attaque2 == 2:
                    Attaque2 = 20 # Dgts de Pierce
                    print("Legarde utilise", Fiche2['Attaques'][1][0], "cela fait", 20, "dégats!")
                
                    
                else: #Legarde utilise Soin 
                    soin = True
                    print("Legarde utilise", Fiche2['Attaques'][2][0], 35, "PV soignés!")
                    
                                         
            if soin:
                if tourJoueur:
                    Fiche1['PV'] += 35 #les premiers soins soigne 35 de PV
                    if Fiche1['PV'] > 100 :
                        Fiche1['PV'] = 100 #Bloque les PV à 100 en cas de "overhealing"
                    
                else:
                    Fiche2['PV'] += 35 #la capacité soin de Legarde fait de même
                    if Fiche2['PV'] > 100 :
                        Fiche2['PV'] = 100
                    menu_choix()
                    
            else: #Une attaque est utilisé à la place
                if tourJoueur:
                    Fiche2['PV'] -= Attaque
                    if Fiche2['PV'] < 0:
                        Fiche2['PV'] = 0 # bloque les PV à 0
                        gagnant = "Trespasser"
                        break
                else:
                    Fiche1['PV'] -= Attaque2
                    if Fiche1['PV'] < 0:
                        Fiche1['PV'] = 0
                        gagnant = "Legarde"
                        break
                    menu_choix() # Fin du tour 
            # échange de tour
            tourJoueur = not tourJoueur
            tourOrdi = not tourOrdi
            
    # une fois que la boucle du jeu se brise, détermine le gagnant et le félicite
    if gagnant == "Trespasser":
        print("Trespasser PV :", Fiche1['PV'], "Legarde PV :", Fiche2['PV'])
        print("Trespasser a gagné ! Merci d'avoir joué")
    else:
        print("Trespasser PV :", Fiche1['PV'], "Legarde PV :", Fiche2['PV'])
        print("Trespasser a été battu.")
        
    print("Voulez-vous rejouer ? (Oui Non)")
    réponse = input("> ")
    if réponse not in ("Oui","oui"):
        rejouer = False
    
    
    
def menu_choix():
    """
    Affiche les inputs attendues
    """
    print("Trespasser PV :", Fiche1['PV'], " Legarde PV :", Fiche2['PV'])
    print("           EN :", Fiche1['EN'], "         EN :", "???")
    print_lines("Choissisez votre action :","1 Attaques","2 Objets","3 Fuite")
    choix = input("> ")
    if choix == "1" :
        menu_attaque()
    elif choix == "2" :
        menu_objet()
    elif choix == "3" :
        print_lines("NIGERUNDAYO !!!","Vous avez fuit le combat...","Bon bah merci pour rien du tout.")
        quit()
    else:
        print("Mauvaise input ! Veuillez entrer un chiffre qui est affiché ci-dessous.")
        menu_choix()
        

def menu_attaque():
    """
    Affiche les attaques à disposition et renvoie attaque choisi par le joueur 
    """
    global Attaque
    num_attaque = 1
    print("Choissisez une attaque :")
    for attaque in Fiche1['Attaques']:
        print(num_attaque, attaque[0],":", attaque[1],"dégâts", attaque[2],"énergie")
        num_attaque += 1
    print("4 Revenir")
    choix = input("> ")
    if choix == "1" :
        Attaque = Fiche1['Attaques'][0]
    elif choix == "2" :
        Attaque = Fiche1['Attaques'][1]
    elif choix == "3" :
        Attaque = Fiche1['Attaques'][2]
    elif choix == "4" :
        menu_choix()
    else:
        print("Mauvaise input ! Veuillez entrer un chiffre qui est affiché ci-dessous.")
        menu_attaque()
        
    return Attaque
        
    
def menu_objet():
    """
    Affiche les objets à disposition et renvoie l'objet choisi par le joueur
    """
    global Objet, nb_objet1, nb_objet2
    print("Choissisez un objet :")
    print("1 Premier soin",nb_objet1)
    print("2 Ration",nb_objet2)
    print("3 Revenir")
    choix = input("> ")
    if choix == "1" :
        if nb_objet1 == 0: #Les premiers soins deviennent inutisables lorsque le compteur atteint 0
            print("Objet indisponible")
            menu_objet()
        else:
            Objet = "premier soin"
    elif choix == "2" :
        if nb_objet2 == 0:
            print("Objet indisponible")
            menu_objet
        else:
            Objet = "ration"
    elif choix == "3" :
        menu_choix()
    else:
        print("Mauvaise input ! Veuillez entrer un chiffre qui est affiché ci-dessous.")
        menu_objet()
    
    return Objet

#Stats des persos et de leurs attaques ("nom de l'attaque", dégats, coût. Or Legarde n'utilise pas d'énergie.)
Fiche1 = {'nom' : 'Trespasser',
          'PV' : 100,
          'EN' : 100,
          'Attaques' : [("Trespass", 35, 50), ("Slash", 15, 10),("Devil's dance", 25, 30)] 
              } 

Fiche2 = {'nom' : 'Legarde',
          'PV' : 100,
          'EN' : 100,
          'Attaques' : [("Longinus", 30),("Pierce", 20),("Soin", 35)] 
              } #Legarde peut se soigner avec Soin (soigne 25 PV et consomme 10 d'énergie)

Attaque = None #Variables qui sera utilisé dans les fonctions ci-dessus 
Objet = None
Attaque2 = None #Attaque choisis par l'ennemi dans combat()
movepool = None #Devient une liste de liste dans combat()
nb_objet1 = 3 #nombre d'objet disponible (premier soin)
nb_objet2 = 3 #(ration)
                                     
menu_choix()
combat()
