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
        return x
    def info(self):
        print (f"Dades titular: {self.nom}, Plaç: {self.plaç}, Interès: {self.interes}, Total: {self.saldo + self.Calculinteres(self.saldo)}")

class Estalvi(Compte):
    def __init__(self, nom, telefon, email, saldo, diners):
        super().__init__(nom, telefon, email, saldo)
        self.diners = diners

    def mostraEstalvis(self):
        print(f"Estalvis: {self.diners}")

# ----------------------------------------------------------------------------
class Banc():
    def __init__(self):
        self.clients = []

    def afegir_client(self, client):
        self.clients.append(client)

    def llistar_clients(self):
        for client in self.clients:
            client.info()
            print()

    def mostrar_client(self, nom):
        for client in self.clients:
            if client.nom == nom:
                client.info()
                if isinstance(client, Fixe):
                    print(f"Plaç: {client.plaç}, Interès: {client.interes}, Total: {client.saldo + client.Calculinteres(client.saldo)}")
                elif isinstance(client, Estalvi):
                    client.mostraEstalvis()
                return
        print("Client no trobat")

    def buscar_client(self, nom):
        for client in self.clients:
            if client.nom == nom:
                return client
        return None

    def modificar_client(self, nom, telefon, email, saldo):
        client = self.buscar_client(nom)
        if client:
            client.telefon = telefon
            client.email = email
            client.saldo = saldo
        else:
            print("Client no trobat")

    def eliminar_client(self, nom):
        client = self.buscar_client(nom)
        if client:
            self.clients.remove(client)
        else:
            print("Client no trobat")


# Create a bank object
banc = Banc()

# Create some clients
c1 = Fixe("Manel", "123456789", "manel@example.com", 1000, "Plaç 1", 5)
c2 = Estalvi("Maria", "987654321", "maria@example.com", 500, 200)

# Add clients to the bank
banc.afegir_client(c1)
banc.afegir_client(c2)

# Show the menu
while True:
    print("Menu:")
    print("1. Afegir un client")
    print("2. Llistar clients")
    print("3. Mostrar les dades d'un client")
    print("4. Buscar client")
    print("5. Modificar un client")
    print("6. Eliminar un client")
    print("7. Sortir")

    opcio = input("Introdueix una opció: ")

    if opcio == "1":
        nom = input("Introdueix el nom del client: ")
        telefon = input("Introdueix el telèfon del client: ")
        email = input("Introdueix l'email del client: ")
        saldo = float(input("Introdueix el saldo del client: "))
        tipus = input("Introdueix el tipus de compte (Fixe o Estalvi): ")
        if tipus == "Fixe":
            plac = input("Introdueix el plaç del compte: ")
            interes = float(input("Introdueix l'interès del compte: "))
            client = Fixe(nom, telefon, email, saldo, plac, interes)
        elif tipus == "Estalvi":
            diners = float(input("Introdueix els diners estalviats: "))
            client = Estalvi(nom, telefon, email, saldo, diners)
        banc.afegir_client(client)
    elif opcio == "2":
        banc.llistar_clients()
    elif opcio == "3":
        nom = input("Introdueix el nom del client: ")
        banc.mostrar_client(nom)
    elif opcio == "4":
        nom = input("Introdueix el nom del client: ")
        client = banc.buscar_client(nom)
        if client:
            print("Client trobat")
        else:
            print("Client no trobat")
    elif opcio == "5":
        nom = input("Introdueix el nom del client: ")
        telefon = input("Introdueix el telèfon del client: ")
        email = input("Introdueix l'email del client: ")
        saldo = float(input("Introdueix el saldo del client: "))
        banc.modificar_client(nom, telefon, email, saldo)
    elif opcio == "6":
        nom = input("Introdueix el nom del client: ")
        banc.eliminar_client(nom)
    elif opcio == "7":
        break
    else: 
        print("Opció no vàlida")