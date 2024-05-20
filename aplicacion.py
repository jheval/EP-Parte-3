import metodos

leerUsuario = open("usuarios.txt", "rt", encoding='utf8')
leerClave = open("claves.txt", "rt", encoding='utf8')
leerNombre = open("nombre.txt", "rt", encoding='utf8')
leerCodigo = open("codigo.txt", "rt", encoding='utf8')
leerPrecio = open("precio.txt", "rt", encoding='utf8')

datosUsuario = leerUsuario.read()
datosClave = leerClave.read()
leerUsuario.close()
leerClave.close()

productos = []

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

def mostrar_menu():
    while True:
        print("*** Datos Producto ***")
        print("1. Listar")
        print("2. Agregar")
        print("3. Salir")
        opcion= input("Ingresar opcion [1,2,3]: ")
        if opcion=="1":
            productos_lista = metodos.listar_productos()
            print("\n".join([f"{producto['nombre']}\t{producto['codigo']}\t{producto['precio']}" for producto in productos_lista]))
        elif opcion == "2":
            metodos.agregar_productos(productos)
        elif opcion == "3":
            break
        else:
            print("Opción incorrecta")

def menu():
    mostrar_menu()

login()

