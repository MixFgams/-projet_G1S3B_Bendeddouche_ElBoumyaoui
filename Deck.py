# Auteur : Farouk Mohamed Bendeddouche

class Deck:
    def __init__(self, nom, taille_max):
        """
        Initialise un deck avec un nom et une taille maximale.
        
        Args:
        nom (str): Le nom du deck.
        taille_max (int): La taille maximale du deck.
        """
        self.nom = nom
        self.cartes = Pile()
        self.tailleMax = taille_max

    def ajouterCartes(self, carte):
        """
        Ajoute une carte au deck.
        
        Args:
        carte (obj): La carte à ajouter au deck.
        """
        self.cartes.empiler(carte)

    def retirerCarte(self):
        """
        Retire une carte du deck et la retourne.
        
        Returns:
        obj: La carte retirée du deck.
        """
        carteRetirer = self.cartes.depiler()
        return carteRetirer

    def afficherDeck(self):
        """
        Affiche toutes les cartes présentes dans le deck.
        """
        self.cartes.afficher()

    def estVide(self):
        """
        Vérifie si le deck est vide.
        
        Returns:
        bool: True si le deck est vide, sinon False.
        """
        if self.cartes.estVide() == True:
            return True
        else:
            return False

    def taille(self):
        """
        Retourne la taille actuelle du deck.
        
        Returns:
        int: La taille actuelle du deck.
        """
        return self.cartes.taille()
