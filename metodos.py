def listar_productos():
    productos = []
    with open("nombre.txt", "rt", encoding='utf8') as nombre_file:
        with open("codigo.txt", "rt", encoding='utf8') as codigo_file:
            with open("precio.txt", "rt", encoding='utf8') as precio_file:
                for nombre, codigo, precio in zip(nombre_file, codigo_file, precio_file):
                    productos.append({"nombre": nombre.strip(), "codigo": codigo.strip(), "precio": float(precio.strip())})
    return productos

def agregar_productos(productos):
    contnnombre = input("Ingrese nombre para agregar: ")
    contcodigo = input("Ingrese código para agregar: ")
    contprecio = float(input("Ingrese precio para agregar: "))
    productos.append({"nombre": contnnombre, "codigo": contcodigo, "precio": contprecio})
    print("Producto agregado")

    with open("EP-Parte03/nombre.txt", "a", encoding='utf8') as nombre_file:
        nombre_file.write(f"{contnnombre}\n")
    with open("EP-Parte03/codigo.txt", "a", encoding='utf8') as codigo_file:
        codigo_file.write(f"{contcodigo}\n")
    with open("EP-Parte03/precio.txt", "a", encoding='utf8') as precio_file:
        precio_file.write(f"{contprecio:.2f}\n")