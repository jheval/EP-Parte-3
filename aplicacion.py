leerUsuario = open("Ep-Parte01/usuarios.txt", "rt", encoding='utf8')
leerClave = open("Ep-Parte01/claves.txt", "rt", encoding='utf8')


datosUsuario = leerUsuario.read()
datosClave = leerClave.read()


def login():
    intentos_restantes = 3
    while intentos_restantes > 0:
        usuario = input("Ingrese su usuario: ").strip()
        password = input("Ingrese su contraseña: ").strip()
       
        if usuario == datosUsuario and password == datosClave:
            menu()
            return  # Salir de la función si las credenciales son correctas
        else:
            intentos_restantes -= 1
            if intentos_restantes > 0:
                print(f"Credenciales incorrectas. Te quedan {intentos_restantes} intento.")
            else:
                print("Has excedido el número máximo de intentos.")
                exit()


def menu():
    print("*** Datos Producto ***")
    print("1. Listar")
    print("2. Agregar")
    print("3. Salir")


login()    