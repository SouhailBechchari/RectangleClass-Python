class Rectangle:
    count = 0

    def __init__(self, largeur, longueur):
        Rectangle.count += 1
        self.nbrec = Rectangle.count
        self.largeur = largeur
        self.longueur = longueur

    def get_largeur(self):
        return self.largeur

    def get_longueur(self):
        return self.longueur

    def get_nbrec(self):
        return self.nbrec

    def set_largeur(self, value):
        self.largeur = value

    def set_longueur(self, value):
        self.longueur = value

    def perimetre(self):
        return 2 * (self.largeur + self.longueur)

    def surface(self):
        return self.largeur * self.longueur

    def to_string(self):
        return f"largeur {self.largeur} longueur {self.longueur}"

    def equals(self, other):
        return self.largeur == other.largeur and self.longueur == other.longueur


class Para(Rectangle):
    count = 0

    def __init__(self, largeur, longueur, hauteur):
        super().__init__(largeur, longueur)
        Para.count += 1
        self.hauteur = hauteur
        self.nbpara = Para.count

    def get_hauteur(self):
        return self.hauteur

    def set_hauteur(self, value):
        self.hauteur = value

    def perimetre(self):
        return 2 * (self.largeur + self.longueur) + 4 * self.hauteur

    def surface(self):
        return 2 * (self.largeur * self.longueur + self.largeur * self.hauteur + self.longueur * self.hauteur)

    def to_string(self):
        return f"{super().to_string()}, hauteur {self.hauteur}"

    def equals(self, other):
        return super().equals(other) and self.hauteur == other.hauteur

    def volume(self):
        return self.largeur * self.longueur * self.hauteur


Rec1 = Rectangle(15, 2)
Rec2 = Rectangle(9, 5)
Rec3 = Rectangle(6, 11)
Par1 = Para(7, 8, 9)
Par2 = Para(7, 8, 4)

print(f"Number of instances in first class: {Rectangle.count}")
print(f"Number of instances in second class: {Para.count}")
print("Rec1", Rec1.to_string())
print("Rec2", Rec2.to_string())
print("Rec3", Rec3.to_string())
print("Rec1 equals Rec2:", Rec1.equals(Rec2))
print("Rec1 equals Rec3:", Rec1.equals(Rec3))
print("Par1 equals Par2:", Par1.equals(Par2))
print("Rec1 surface:", Rec1.surface())
print("Rec2 surface:", Rec2.surface())
print("Rec3 surface:", Rec3.surface())
print("Rec1 perimeter:", Rec1.perimetre())
print("Rec2 perimeter:", Rec2.perimetre())
print("Rec3 perimeter:", Rec3.perimetre())
print("Par1 volume:", Par1.volume())
print("Par2 volume:", Par2.volume())
