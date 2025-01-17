# Auteur : Farouk Mohamed Bendeddouche

from Card import card

class spell(card):
    def init(self, effect, name, cost):
        """
        Initialise une carte sort avec un effet, un nom et un coût en mana.
        
        Args:
        effect (str): L'effet du sort.
        name (str): Le nom du sort.
        cost (int): Le coût en mana du sort.
        """
        super().init(name, cost)
        self.effect = effect

    def changerEffect(self, effect):
        """
        Modifie l'effet du sort.
        
        Args:
        effect (str): Le nouvel effet du sort.
        """
        self.effect = effect

    def getEffect(self):
        """
        Affiche l'effet actuel du sort.
        """
        print("L'effet de la carte est : " + self.effect)

    def str(self):
        """
        Affiche une représentation du sort avec son nom, coût en mana et effet.
        """
        print("La carte " + self.name + " a pour coût " + str(self.cost) + " mana et a pour effet de " + self.effect)
