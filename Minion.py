# Auteur : Farouk Bendeddouche

from Card import card
from Les4StructureDeDonnees.File import *

class Minion(card):
    def __init__(self, attackPoints, healthPoints, name, cost):
        """
        Initialise un serviteur avec des points d'attaque, de vie, un nom et un coût.
        
        Args:
        attackPoints (int): Les points d'attaque du serviteur.
        healthPoints (int): Les points de vie du serviteur.
        name (str): Le nom du serviteur.
        cost (int): Le coût de la carte serviteur.
        """
        super().init(name, cost)
        self.ap = attackPoints
        self.hp = healthPoints
        self.effet = File()

    def changerAP(self, attackPoints):
        """
        Modifie les points d'attaque du serviteur.
        
        Args:
        attackPoints (int): Les nouveaux points d'attaque du serviteur.
        """
        self.ap = attackPoints

    def changerHP(self, healthPoints):
        """
        Modifie les points de vie du serviteur.
        
        Args:
        healthPoints (int): Les nouveaux points de vie du serviteur.
        """
        self.hp = healthPoints

    def getName(self):
        """
        Retourne le nom du serviteur.
        
        Returns:
        str: Le nom du serviteur.
        """
        return self.name

    def getAP(self):
        """
        Affiche et retourne les points d'attaque du serviteur.
        """
        print("L'attaque de cette carte est de : " + str(self.ap))

    def getHP(self):
        """
        Affiche et retourne les points de vie du serviteur.
        """
        print("La vie de cette carte est de : " + str(self.hp))

    def attaquer(self, minion):
        """
        Permet à un serviteur d'attaquer un autre serviteur et échange leurs points de vie.
        
        Args:
        minion (Minion): Le serviteur cible de l'attaque.
        """
        self.hp = self.hp - minion.ap
        minion.hp = minion.hp - self.ap

    def attaquerHero(self, hero):
        """
        Permet à un serviteur d'attaquer un héros et de lui infliger des dégâts.
        
        Args:
        hero (Hero): Le héros cible de l'attaque.
        """
        hero.hp -= self.ap

    def __str__(self):
        """
        Retourne une représentation sous forme de chaîne de caractères du serviteur.
        
        Returns:
        str: La chaîne de caractères représentant le serviteur.
        """
        return f"| {self.name:<10} | Attaque: {self.ap:<2} | Défense: {self.hp:<2} | Coût: {self.cost:<2} |"

    def ajouterEffet(self, effet):
        """
        Ajoute un effet à la file d'effets du serviteur.
        
        Args:
        effet (Effet): L'effet à ajouter à la file d'effets du serviteur.
        """
        self.effet.enfiler(effet)
