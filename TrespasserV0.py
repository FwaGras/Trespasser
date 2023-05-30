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
    #mise en place de la boucle du jeu
    while (Fiche1['PV'] or Fiche2['PV']):
        
        soin = False #Détermine si un premier a été utilisé
        récup = False #Détermine si une ration a été utilisé
        miss = False #Détermine si un coup rate
        
        
def menu_choix():
    """
    Affiche les inputs attendues
    """
    print("Trespasser PV :", Fiche1['PV'], " Legarde PV :", Fiche2['PV'])
    print_lines("Choissisez votre action :","1 Attaques","2 Objets","3 Fuite")
    choix = input("> ")
    if choix == "1" :
        menu_attaque()
    elif choix == "2" :
        menu_objet()
    elif choix == "3" :
        print_lines("NIGERUNDAYO !!!","Vous avez fuit le combat...","Bon bah merci pour rien du tout.")
        
    else:
        print("Mauvaise input ! Veuillez entrer un chiffre qui est affiché ci-dessous.")
        menu_choix()
        

def menu_attaque():
    """
    Affiche les attaques à disposition et renvoie attaque choisi par le joueur 
    """
    Attaque = None
    num_attaque = 1
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

    nb_objet1 = 3 #nombre d'objet utilisable 
    nb_objet2 = 3
    print("Choissisez un objet :")
    print("1 Premier soin",nb_objet1)
    print("2 Ration",nb_objet2)
    print("3 Revenir")
    choix = input("> ")
    if choix == "1" :
        print("toto")
    elif choix == "2" :
        print("toto")
    elif choix == "3" :
        menu_choix()
    else:
        print("Mauvaise input ! Veuillez entrer un chiffre qui est affiché ci-dessous.")
        menu_objet()
    

#Stats des persos et de leurs attaques ("nom de l'attaque", dégats, coût)
Fiche1 = {'nom' : 'Trespasser',
          'PV' : 100,
          'EN' : 100,
          'Attaques' : [("Trespass", 35, 50), ("Slash", 15, 10),("Devil's dance", 25, 50)] 
              } 

Fiche2 = {'nom' : 'Legarde',
          'PV' : 100,
          'EN' : 100,
          'Attaques' : [("Longinus", 30, 25),("Pierce", 20, 15),("Counter", 35, 50)]
              }

menu_choix()