import Ex3
# Crear un objecte banc
banc = Ex3.Banc()

# Crear alguns clients
c1 = Ex3.Fixe("Manel", "123456789", "manel@example.com", 1000, "Plaç 1", 5)
c2 = Ex3.Estalvi("Maria", "987654321", "maria@example.com", 500, 200)

# Afegir clients al banc
banc.afegir_client(c1)
banc.afegir_client(c2)

# Mostrar el menú
while True:
    print("Menú:")
    print("1. Afegir un client")
    print("2. Llistar clients")
    print("3. Mostrar les dades d'un client")
    print("4. Buscar client")
    print("5. Modificar un client")
    print("6. Eliminar un client")
    print("7. Sortir")
    print("")

    opcio = input("Introdueix una opció: ")

    if opcio == "1":
        nom = input("Introdueix el nom del client: ")
        telefon = input("Introdueix el telèfon del client: ")
        email = input("Introdueix l'email del client: ")
        saldo = Ex3.llegir_numero("Introdueix el saldo del client: ")   
        tipus = input("Introdueix el tipus de compte (Fixe o Estalvi): ")
        if tipus == "Fixe":
            plac = input("Introdueix el plaç del compte: ")
            interes = Ex3.llegir_numero("Introdueix l'interès del compte: ")
            client = Ex3.Fixe(nom, telefon, email, saldo, plac, interes)
        elif tipus == "Estalvi":
            diners = Ex3.llegir_numero("Introdueix els diners estalviats: ")
            client = Ex3.Estalvi(nom, telefon, email, saldo, diners)
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
        saldo = Ex3.llegir_numero("Introdueix el saldo del client: ")
        banc.modificar_client(nom, telefon, email, saldo)

    elif opcio == "6":
        nom = input("Introdueix el nom del client: ")
        banc.eliminar_client(nom)

    elif opcio == "7":
        break

    else: 
        print("Opció no vàlida")
