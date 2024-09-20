class Compte:
    def __init__(self, nom, telefon, email, saldo):
        self.nom = nom
        self.telefon = telefon
        self.email = email
        self.saldo = saldo
    def info(self):
        print(f"Nom: {self.nom}, Telefon: {self.telefon}, Email: {self.email}, Saldo{self.saldo} ")

class Fixe(Compte):
    def __init__(self, nom, telefon, email, saldo, plaç, interes):
        super().__init__(nom, telefon, email, saldo)
        self.plaç = plaç
        self.interes = interes
    def Calculinteres(self, quantitat):
        x = quantitat*self.interes/100
    def info(self):
        print (f"Dades titular: {self.nom}, Plaç: {self.plaç}, Interès: {self.interes}, Total: {self.saldo + self.calcul_interes(self.saldo)}")

class Estalvi(Compte):
    def __init__(self, nom, telefon, email, saldo, diners):
        super().__init__(nom, telefon, email, saldo)
        self.diners = diners

    def mostraEstalvis(self):
        print(f"Estalvis: {self.diners}")
 