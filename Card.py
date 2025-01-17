class Card:
    def __init__(self, name, cost):
        """
        Initialise une carte avec un nom et un coût.

        Args:
        name (str): Le nom de la carte.
        cost (int): Le coût de la carte.
        """
        self.name = name
        self.cost = cost 

    def __str__(self):
        """
        Retourne une chaîne de caractères représentant la carte avec son nom et son coût.

        Returns:
        str: La représentation de la carte sous forme de chaîne.
        """
        return f"{self.name} {self.cost}"
