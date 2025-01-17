# Auteur : Farouk Mohamed Bendeddouche

from Hero import *
from Les4StructureDeDonnees.ListeChainee import ListeChainee
from Deck import *
from Minion import *

class Player:
    def __init__(self, hero, deck, mana, name, fatigue):
        """
        Initialise un joueur avec un héros, un deck, une quantité de mana, un nom et une fatigue.
        
        Args:
        hero (Hero): L'objet héros du joueur.
        deck (Deck): L'objet deck du joueur.
        mana (int): Le mana actuel du joueur.
        name (str): Le nom du joueur.
        fatigue (int): Le niveau de fatigue du joueur.
        """
        self.hero = hero
        self.deck = deck
        self.hand = ListeChainee()
        self.mana = mana
        self.maxMana = 1 
        self.name = name
        self.fatigue = fatigue
        self.board = ListeChainee() 
        self.ennemy = None
        self.graveyard = Pile()

    def drawCard(self):
        """
        Pioche une carte du deck et l'ajoute à la main. Si le deck est vide, applique la fatigue.
        """
        if self.deck.taille() == 0:
            self.appliquerFatigue()  # Applique les effets de la fatigue si le deck est vide
        else:
            self.hand.ajouter(self.deck.retirerCarte())  # Ajoute la carte du deck à la main
            print(self.name, "a pioché une carte")

    def appliquerFatigue(self):
        """
        Applique la fatigue au joueur, augmentant les dégâts subis à chaque fois qu'il pioche une carte 
        après un deck vide.
        """
        self.fatigue += 1  # Augmente le niveau de fatigue
        self.takeDamage(self.fatigue)  # Applique les dégâts de fatigue
        print(f"{self.name} subit {self.fatigue} dégâts de fatigue !")

    def takeDamage(self, amount):
        """
        Inflige des dégâts au héros du joueur.
        
        Args:
        amount (int): Le nombre de dégâts infligés au héros.
        """
        self.hero.hp -= amount

    def healHero(self, amount):
        """
        Soigne le héros du joueur.
        
        Args:
        amount (int): La quantité de points de vie à restaurer.
        """
        self.hero.hp += amount

    def regenererMana(self):
        """
        Régénère le mana du joueur à sa valeur maximale.
        """
        self.mana = self.maxMana

    def addManaMax(self, amount):
        """
        Augmente le mana maximum du joueur.
        
        Args:
        amount (int): La quantité de mana à ajouter au mana maximum.
        """
        self.maxMana += amount

    def getManaMax(self):
        """
        Retourne la valeur du mana maximum du joueur.
        
        Returns:
        int: Le mana maximum du joueur.
        """
        return self.maxMana
    
    def getEnnemy(self):
        """
        Retourne l'ennemi du joueur.
        
        Returns:
        Player: L'objet joueur ennemi.
        """
        return self.ennemy

    def setEnnemy(self, ennemy):
        """
        Définit l'ennemi du joueur.
        
        Args:
        ennemy (Player): L'objet joueur ennemi.
        """
        self.ennemy = ennemy

    def getGraveYard(self):
        """
        Retourne la pile des cartes mortes si elle n'est pas vide.
        
        Returns:
        Pile: La pile des cartes mortes, ou un message d'erreur si vide.
        """
        if not self.graveyard.estVide():
            return self.graveyard
        else:
            print("Vous n'avez pas de serviteur à réincarner")

    def getBoard(self):
        """
        Affiche l'état actuel du plateau du joueur et de l'ennemi.
        """
        print("#-------------------------------------------------------------------------#")
        print("#\tAffichage du plateau :")
        print("#-------------------------------------------------------------------------#")
        print("Num :  0   | PV de",self.ennemy.name, ":", self.ennemy.hero.hp)
        self.board.afficher()
        print("#-------------------------------------------------------------------------#")

    def attaque(self):
        """
        Permet au joueur d'attaquer avec ses serviteurs, ou de passer son tour s'il n'a pas de serviteur.
        """
        if self.board.taille() == 0:
            print(f"{self.name} n'a pas de serviteurs.")
            print("#-------------------------------------------------------------------------#")
            return
        
        if self.ennemy.board.taille() == 0:
            print(f"Votre adversaire n'a pas de serviteurs.")
            print("#-------------------------------------------------------------------------#")
            return 
        
        print("Serviteurs disponibles pour attaquer :")
        self.getBoard()

        # Choisir un attaquant
        choix_attaquant = input("Choisissez un serviteur pour attaquer (-1 pour passer le tour) : ")
        try:
            choix_attaquant = int(choix_attaquant)
        except ValueError:
            print("Entrée invalide. Action annulée.")
            return

        while choix_attaquant == 0:
            choix_attaquant = input("Choisissez un serviteur et non un héros (-1 pour passer le tour) : ")
            try:
                choix_attaquant = int(choix_attaquant)
            except ValueError:
                print("Entrée invalide. Action annulée.")
                return

        if choix_attaquant == -1:
            return
        if 1 <= choix_attaquant <= self.board.taille():
            attaquant = self.board.getNoeud(choix_attaquant-1).valeur
        else:
            print("Choix invalide. Action annulée.")
            return

        # Choisir une cible
        print("Choisissez une cible parmi les serviteurs ennemis ou le héros adverse.")
        adversaire = self.getEnnemy()
        print("Serviteurs ennemis disponibles :")
        self.ennemy.getBoard()

        choix_cible = input("Entrez le numéro de la cible : ")
        try:
            choix_cible = int(choix_cible)
        except ValueError:
            return

        if choix_cible == 0:
            attaquant.attaquerHero(self.ennemy.hero)
            print(f"{attaquant.name} inflige {attaquant.ap} point de dégâts à {self.ennemy.name} !")
            print(f"{self.ennemy.name} n'a plus que {self.ennemy.hero.hp} pv!")
            return
        elif 1 <= choix_cible <= adversaire.board.taille():
            cible = adversaire.board.getNoeud(choix_cible).valeur
        else:
            print("Choix invalide. Action annulée.")
            return

        print(f"{attaquant.name} inflige {attaquant.ap} point de dégâts à {cible.name} !")
        attaquant.attaquer(cible)  # Méthode à définir dans `Hero` et `Minion`
        
        # Supprimer les serviteurs morts
        self.nettoyerPlateau(self.board)
        adversaire.nettoyerPlateau(adversaire.board)

    def jouerCarte(self):
        """
        Permet au joueur de jouer une carte de sa main et de l'ajouter à son plateau.
        """
        if self.hand.taille() == 0:
            return
        print("#-------------------------------------------------------------------------#")
        print("#\tAffichage de la main :")
        print("#-------------------------------------------------------------------------#")
        self.hand.afficher()
        print("#-------------------------------------------------------------------------#")
        try:
            num = input("#Veuillez jouer une carte (par son numéro) (-1 pour ne pas jouer) : ")
            if num == "-1":
                print("#-------------------------------------------------------------------------#")
                return
            carteJouee = self.hand.getNoeud(int(num)-1)
            if carteJouee is None:
                print("#Indice invalide. Aucune carte n'a été jouée.\n")
                return

            # Accéder à la valeur pour l'ajouter au plateau
            self.board.ajouter(carteJouee.valeur)

            # Supprimer le nœud de la main
            self.hand.supprimerNoeud(carteJouee)
            print(f"#La carte '{carteJouee.valeur.getName()}' a été jouée.")

            print("#-------------------------------------------------------------------------#")
        except ValueError:
            print("Entrée invalide. Veuillez entrer un numéro valide.")

    def nettoyerPlateau(self, board):
        """
        Supprime les serviteurs du plateau dont les points de vie sont inférieurs ou égaux à 0.
        
        Args:
        board (ListeChainee): Le plateau à nettoyer.
        """
        courant = board.tete
        precedent = None

        while courant is not None:
            if courant.valeur.hp <= 0:
                print(courant.valeur.name, " a péri")
                if precedent is None:  # Le nœud courant est la tête
                    board.tete = courant.suivant
                else:  # On connecte le précédent au suivant
                    precedent.suivant = courant.suivant
            else:
                precedent = courant  # On avance le précédent uniquement si le nœud n'a pas été supprimé

            courant = courant.suivant
