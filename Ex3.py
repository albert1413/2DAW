class Compte:
    def __init__(self, nom, telefon, email, saldo):
        self.nom = nom
        self.telefon = telefon
        self.email = email
        self.saldo = saldo

    def info(self):
        print(f"Nom: {self.nom}, Telèfon: {self.telefon}, Email: {self.email}, Saldo: {self.saldo}")

class Fixe(Compte):
    def __init__(self, nom, telefon, email, saldo, plac, interes):
        super().__init__(nom, telefon, email, saldo)
        self.plac = plac
        self.interes = interes

    def calcul_interes(self, quantitat):
        x = quantitat * self.interes / 100
        return x

    def info(self):
        print(f"Dades titular: {self.nom}, Plaç: {self.plac}, Interès: {self.interes}, Total: {self.saldo + self.calcul_interes(self.saldo)}")

class Estalvi(Compte):
    def __init__(self, nom, telefon, email, saldo, diners):
        super().__init__(nom, telefon, email, saldo)
        self.diners = diners

    def mostra_estalvis(self):
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
                if isinstance(client, Fixe): #isinstance: mira si client es una instancia de la classe Fixe.
                    print(f"Plaç: {client.plac}, Interès: {client.interes}, Total: {client.saldo + client.calcul_interes(client.saldo)}")
                elif isinstance(client, Estalvi):
                    client.mostra_estalvis()
                break
        print("Client no trobat")

    def buscar_client(self, nom):
        nom_lower = nom.lower()
        for client in self.clients:
            client_lower = client.lower()
            if client_lower == nom_lower:
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
            print(f"{nom} eliminat")
        else:
            print("Client no trobat")

def llegir_numero(missatge):
    while True:
        entrada = input(missatge)
        try:
            # Convertim l'entrada a float
            numero = float(entrada)
            if numero<0:
                raise ValueError("Error: introduïu un valor numèric vàlid.")
            return numero  # Retornem el número si és vàlid
        except ValueError:
            # Si no es pot convertir, informem l'usuari
            print("Error: introduïu un valor numèric vàlid.")