from modulos.usuarios import Usuario
from modulos.pedido import Pedido

usuarios_creados = []
articulos = {
    "Tazas": {"precio": "$5000", "descripcion": "Tazas de cerámica con diferentes diseños para grandes y chicos"},
    "Sahumerios": {"precio": "$400", "descripcion": "Sahumerios de diferentes aromas"},
    "Termos Stanley": {"precio": "$35000", "descripcion": "Termos de diferentes colores y medidas"}
}

def registro_usuarios():
    while True:
        nombre = input("Por favor, ingrese su nombre: ")
        apellido = input("Por favor, ingrese su apellido: ")
        correo_electrónico = input("Ingrese su correo electrónico: ")
        password = input("Ingrese su contraseña deseada: ")
        repetir_password = input("Por favor repita su contraseña: ")

        if password == repetir_password:
            registro_de_datos = {"nombre_usuario": nombre, "apellido_usuario": apellido, "contraseña": password, "correo electrónico": correo_electrónico}
            usuarios_creados.append(registro_de_datos)
            with open("Datos_de_usuarios.txt", "a") as datos:
                datos.write(str(registro_de_datos) + "\n")
            print("Usuario creado: ", Usuario(nombre, apellido, correo_electrónico))
            break
        else:
            print("No se pudo crear su usuario, las contraseñas no coinciden.")

def ingreso_usuarios(usuarios_creados):
    while True:
        nombre = input("Ingrese su nombre: ")
        apellido = input("Ingrese su apellido: ")
        password = input("Ingrese su contraseña: ")
        for registro_de_datos in usuarios_creados:
            if nombre == registro_de_datos["nombre_usuario"] and apellido == registro_de_datos["apellido_usuario"] and password == registro_de_datos["contraseña"]:
                print(f"Bienvenido a la tienda, {nombre}")
                return
        print("El usuario que ha ingresado es incorrecto, vuelva a intentar.")
        
def realizar_compra():
    print("Seleccione un artículo para comprar:")
    for producto, detalles in articulos.items():
        print(f"{producto}: {detalles['precio']} - {detalles['descripcion']}" )
    producto = input("Seleccione un producto o presione Enter para salir: ")
    if producto in articulos:
        producto_comprado = articulos[producto]
        pedido = Pedido(producto, producto_comprado["descripcion"])
        print(f"Ha comprado {pedido}.")
    else:
        print("Opción inválida.")
def menu():
    while True:
        print("\n😊​ Bienvenido/a a WadaTienda, Elige una opción 😊​")
        print("1. Registro de usuario")
        print("2. Iniciar sesión usuario")
        print("3. Salir")
        print("4. Comprar articulos")
        
        opcion = input("Seleccione una opción: ")
        if opcion == "1":
            registro_usuarios()
        elif opcion == "2":
            ingreso_usuarios(usuarios_creados)
            break
        elif opcion == "3":
            print("Gracias por visitarnos en nuestra página.")
            break
        elif opcion == "4":
            realizar_compra()
            break
        else:
            print("Opción incorrecta, por favor vuelva a elegir.")
menu()