# Auteur : Farouk Mohamed Bendeddouche

class Hero:
    def __init__(self, name, hp):
        """
        Initialise un héros avec un nom et un nombre de points de vie (hp).
        
        Args:
        name (str): Le nom du héros.
        hp (int): Le nombre de points de vie du héros.
        """
        self.name = name
        self.imgPath = None
        self.hp = hp

    def getName(self):
        """
        Retourne le nom du héros.
        
        Returns:
        str: Le nom du héros.
        """
        return self.name

    def getImgPath(self):
        """
        Affiche le nom du héros et retourne le chemin de l'image du héros.
        
        Returns:
        str: Le chemin de l'image du héros.
        """
        print('Le nom du héros est ' + self.name)
        return self.imgPath

    def setName(self, nvNom):
        """
        Modifie le nom du héros et affiche le changement de nom.
        
        Args:
        nvNom (str): Le nouveau nom du héros.
        """
        oldName = self.name
        self.name = nvNom
        print('Le nom du héros a été changé de ' + oldName + ' à ' + self.name)

    def setImgPath(self):
        """
        Affiche le nom du héros et retourne son nom.
        
        Returns:
        str: Le nom du héros.
        """
        print('Le nom du héros est ' + self.name)
        return self.name
