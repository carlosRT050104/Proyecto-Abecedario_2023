import os 
import numpy as np 
import math
import random
import sys
from cryptography.fernet import Fernet
from pytube import YouTube
from forex_python.converter import CurrencyRates
import csv
from datetime import datetime
import requests

os.system("cls")
def ingresar_matriz():
    filas = int(input("Ingrese el número de filas de la matriz: "))
    columnas = int(input("Ingrese el número de columnas de la matriz: "))

    matriz = []

    print("Ingrese los elementos de la matriz:")
    for i in range(filas):
        fila = []
        for j in range(columnas):
            elemento = float(input(f"Ingrese el elemento en la posición ({i + 1}, {j + 1}): "))
            fila.append(elemento)
        matriz.append(fila)

    return matriz
def es_capicua(numero):
    return str(numero) == str(numero)[::-1]
def agregar_registro():
    nombre = input("Ingresa el nombre: ")
    edad = input("Ingresa la edad: ")

    nuevo_registro = {"Nombre": nombre, "Edad": edad}
    registros.append(nuevo_registro)
    print("Registro agregado con éxito.")

def modificar_registro():
    listar_registros()
    try:
        indice = int(input("Ingresa el índice del registro que quieres modificar: "))
        if 0 <= indice < len(registros):
            nuevo_nombre = input("Ingresa el nuevo nombre: ")
            nuevo_edad = input("Ingresa la nueva edad: ")

            registros[indice]["Nombre"] = nuevo_nombre
            registros[indice]["Edad"] = nuevo_edad
            print("Registro modificado con éxito.")
        else:
            print("Índice no válido.")
    except ValueError:
        print("Por favor, ingresa un número válido.")

def listar_registros():
    if registros:
        print("\nListado de Registros:")
        for i, registro in enumerate(registros):
            print(f"{i}. Nombre: {registro['Nombre']}, Edad: {registro['Edad']}")
    else:
        print("No hay registros para mostrar.")

def eliminar_registro():
    listar_registros()
    try:
        indice = int(input("Ingresa el índice del registro que quieres eliminar: "))
        if 0 <= indice < len(registros):
            del registros[indice]
            print("Registro eliminado con éxito.")
        else:
            print("Índice no válido.")
    except ValueError:
        print("Por favor, ingresa un número válido.")

def agregar_producto():
    nombre = input("Ingresa el nombre del producto: ")
    precio = float(input("Ingresa el precio del producto: "))
    cantidad = int(input("Ingresa la cantidad de unidades: "))

    nuevo_producto = {"Nombre": nombre, "Precio": precio, "Cantidad": cantidad}
    productos.append(nuevo_producto)
    print("Producto agregado con éxito.")

def mostrar_carrito():
    if productos:
        print("\nCarrito de Compras:")
        for i, producto in enumerate(productos):
            print(f"{i+1}. {producto['Nombre']} - Precio: {producto['Precio']:.2f} - Cantidad: {producto['Cantidad']}")
    else:
        print("El carrito está vacío.")

def registrar_cliente():
    global clientes
    nombre_cliente = input("Ingresa el nombre del cliente: ")
    ruc_o_dni_cliente = input("Ingresa el RUC o DNI del cliente: ")

    clientes[ruc_o_dni_cliente] = {"Nombre": nombre_cliente}
    print("Cliente registrado con éxito.")

def generar_factura():
    global nombre_cliente, ruc_o_dni_cliente

    ruc_o_dni_cliente = input("Ingresa el RUC o DNI del cliente: ")

    # Verificar si el cliente está registrado
    if ruc_o_dni_cliente not in clientes:
        print("Cliente no registrado. Registra al cliente primero.")
        return

    nombre_cliente = clientes[ruc_o_dni_cliente]["Nombre"]

    mostrar_carrito()

    # Calcular subtotal, IGV y total
    subtotal = sum(producto['Precio'] * producto['Cantidad'] for producto in productos)
    igv = subtotal * 0.18
    total = subtotal + igv

    # Mostrar información de la factura
    print("\n--- Factura ---")
    print("Cliente:", nombre_cliente)
    print("RUC/DNI:", ruc_o_dni_cliente)
    print("\nDetalle de la Compra:")
    for i, producto in enumerate(productos):
        print(f"{i+1}. {producto['Nombre']} - Precio: {producto['Precio']:.2f} - Cantidad: {producto['Cantidad']}")
    print("\nResumen:")
    print(f"Subtotal: {subtotal:.2f}")
    print(f"IGV (18%): {igv:.2f}")
    print(f"Total: {total:.2f}")

# Funciones para gestión de tareas (Listas de diccionarios)
def agregar_tarea(tareas, nombre, descripcion, fecha_vencimiento):
    for tarea in tareas:
        if tarea["nombre"] == nombre:
            print(f"La tarea '{nombre}' ya existe. Intente con otro nombre.")
            return
    nueva_tarea = {"nombre": nombre, "descripcion": descripcion, "fecha_vencimiento": fecha_vencimiento, "estado": "Pendiente"}
    tareas.append(nueva_tarea)
    print(f"Tarea '{nombre}' agregada con éxito.")

def actualizar_estado_tarea(tareas, nombre, nuevo_estado):
    tarea_encontrada = False
    for tarea in tareas:
        if tarea["nombre"] == nombre:
            tarea["estado"] = nuevo_estado
            tarea_encontrada = True
            print(f"Estado de la tarea '{nombre}' actualizado a '{nuevo_estado}'.")
            break
    if not tarea_encontrada:
        print(f"No se encontró la tarea '{nombre}'.")

def imprimir_tareas(tareas):
    print("\nListado de tareas:")
    for tarea in tareas:
        print(f"{tarea['nombre']}: {tarea['descripcion']} - Fecha de vencimiento: {tarea['fecha_vencimiento']} - Estado: {tarea['estado']}")

# Funciones para gestión de empleados (Diccionarios)
def agregar_empleado(empleados, id_empleado, nombre, cargo):
    if id_empleado not in empleados:
        empleados[id_empleado] = {"nombre": nombre, "cargo": cargo}
        print(f"Empleado {nombre} agregado con éxito.")
    else:
        print(f"El empleado con DNI {id_empleado} ya existe. Intente con otro DNI.")

def actualizar_cargo(empleados, id_empleado, nuevo_cargo):
    if id_empleado in empleados:
        empleados[id_empleado]["cargo"] = nuevo_cargo
        print(f"Cargo del empleado {empleados[id_empleado]['nombre']} actualizado a '{nuevo_cargo}'.")
    else:
        print(f"No se encontró al empleado con ID {id_empleado}.")

def imprimir_empleados(empleados):
    print("\nListado de empleados:")
    for id_empleado, detalles in empleados.items():
        print(f"ID: {id_empleado} - Nombre: {detalles['nombre']} - Cargo: {detalles['cargo']}")

# Funciones para gestión de horarios (Listas de tuplas)
def agregar_horario(horarios, dia, hora_inicio, hora_fin):
    for horario in horarios:
        if horario[0] == dia and (hora_inicio < horario[2] < hora_fin or hora_inicio < horario[3] < hora_fin):
            print(f"Conflicto de horario para el día {dia}. Intente con otro horario.")
            return
    nuevo_horario = (dia, hora_inicio, hora_fin)
    horarios.append(nuevo_horario)
    print(f"Horario para el día {dia} agregado con éxito.")

def imprimir_horarios(horarios):
    print("\nListado de horarios:")
    for horario in horarios:
        print(f"Día: {horario[0]} - Hora inicio: {horario[1]} - Hora fin: {horario[2]}")

def seleccionar_palabra_manual():
    palabra = input("Jugador 1, ingresa la palabra a adivinar: ").lower()
    return palabra

def seleccionar_palabra_aleatoria():
    palabras = ["python", "programacion", "computadora", "tecnologia", "inteligencia"]
    return random.choice(palabras).lower()

def mostrar_tablero(palabra, letras_adivinadas):
    tablero = ""
    for letra in palabra:
        if letra in letras_adivinadas:
            tablero += letra + " "
        else:
            tablero += "_ "
    return tablero.strip()

def mostrar_ahorcado(intentos):
    ahorcado = [
        "  -----\n |     |\n       |\n       |\n       |\n       |\n-------",
        "  -----\n |     |\n O     |\n       |\n       |\n       |\n-------",
        "  -----\n |     |\n O     |\n |     |\n       |\n       |\n-------",
        "  -----\n |     |\n O     |\n/|     |\n       |\n       |\n-------",
        "  -----\n |     |\n O     |\n/|\\    |\n       |\n       |\n-------",
        "  -----\n |     |\n O     |\n/|\\    |\n/      |\n       |\n-------",
        "  -----\n |     |\n O     |\n/|\\    |\n/ \\    |\n       |\n-------"
    ]
    print(ahorcado[intentos])

def obtener_opcion_usuario():
    while True:
        print("1. Piedra")
        print("2. Papel")
        print("3. Tijeras")
        opcion = input("Elige tu opción (1/2/3): ")
        if opcion in ["1", "2", "3"]:
            return int(opcion)
        else:
            print("Opción no válida. Inténtalo de nuevo.")

def obtener_opcion_computadora():
    return random.randint(1, 3)

def determinar_ganador(opcion_usuario, opcion_computadora):
    if opcion_usuario == opcion_computadora:
        return "Empate"
    elif (opcion_usuario == 1 and opcion_computadora == 3) or \
         (opcion_usuario == 2 and opcion_computadora == 1) or \
         (opcion_usuario == 3 and opcion_computadora == 2):
        return "Ganaste"
    else:
        return "La computadora gana"

def generar_contraseña(longitud):
    import secrets
    import string

    caracteres = string.ascii_letters + string.digits + string.punctuation
    contraseña = ''.join(secrets.choice(caracteres) for _ in range(longitud))

    return contraseña

def encriptar_contraseña(contraseña, clave):
    f = Fernet(clave)
    contraseña_encriptada = f.encrypt(contraseña.encode())
    return contraseña_encriptada

def desencriptar_contraseña(contraseña_encriptada, clave):
    f = Fernet(clave)
    contraseña = f.decrypt(contraseña_encriptada).decode()
    return contraseña

def contar_vocales_consonantes(palabra):
    vocales = "aeiouAEIOU"
    consonantes = "bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ"
    
    num_vocales = sum(1 for char in palabra if char in vocales)
    num_consonantes = sum(1 for char in palabra if char in consonantes)
    num_especiales = len(palabra) - num_vocales - num_consonantes

    return num_vocales, num_consonantes, num_especiales

def descargar_video(url, formato, ruta_guardado="."):
    try:
        # Crear un objeto YouTube
        video = YouTube(url)

        if formato == 'mp4':
            # Obtener la mejor resolución disponible
            stream = video.streams.get_highest_resolution()
        elif formato == 'mp3':
            # Obtener la mejor calidad de audio disponible
            stream = video.streams.filter(only_audio=True).first()
        else:
            print("Formato no válido. Use 'mp4' o 'mp3'.")
            return

        # Descargar el video o audio
        print(f"Descargando: {video.title}")
        stream.download(ruta_guardado)
        print("Descarga completada.")
    except Exception as e:
        print(f"Error al descargar el contenido: {e}")

def convertir_monedas(monto, moneda_origen, moneda_destino):
    c = CurrencyRates()
    tasa_cambio = c.get_rate(moneda_origen, moneda_destino)
    monto_convertido = monto * tasa_cambio
    return monto_convertido

def convertir_temperatura(temp, escala_origen, escala_destino):
    if escala_origen == 'C' and escala_destino == 'F':
        return temp * 9/5 + 32
    elif escala_origen == 'F' and escala_destino == 'C':
        return (temp - 32) * 5/9
    else:
        return "Conversion no soportada."

def calcular_imc(peso, altura):
    imc = peso / (altura ** 2)
    return imc

def calcular_factorial(numero):
    if numero == 0 or numero == 1:
        return 1
    else:
        return numero * calcular_factorial(numero - 1)

def romano_a_entero(romano):
    romanos = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    entero = 0
    prev_valor = 0
    for letra in romano:
        valor = romanos[letra]
        if valor > prev_valor:
            entero += valor - 2 * prev_valor
        else:
            entero += valor
        prev_valor = valor
    return entero

class Transaccion:
    def __init__(self, fecha, tipo, categoria, descripcion, monto):
        self.fecha = fecha
        self.tipo = tipo
        self.categoria = categoria
        self.descripcion = descripcion
        self.monto = monto


class RegistroFinanciero:
    def __init__(self):
        self.lista_transacciones = []

    def agregar_transaccion(self, transaccion):
        self.lista_transacciones.append(transaccion)
        print("Transacción registrada exitosamente.")

    def mostrar_transacciones(self, tipo=None):
        if tipo:
            transacciones_filtradas = [t for t in self.lista_transacciones if t.tipo == tipo]
        else:
            transacciones_filtradas = self.lista_transacciones

        print("\nLista de Transacciones:")
        for transaccion in transacciones_filtradas:
            print(f"Fecha: {transaccion.fecha}, Tipo: {transaccion.tipo}, Categoría: {transaccion.categoria}, Descripción: {transaccion.descripcion}, Monto: ${transaccion.monto}")

    def calcular_balance(self):
        ingresos = sum([t.monto for t in self.lista_transacciones if t.tipo == 'Ingreso'])
        gastos = sum([t.monto for t in self.lista_transacciones if t.tipo == 'Gasto'])
        balance = ingresos - gastos
        print(f"\nBalance Total: ${balance}")
        print(f"Ingresos: ${ingresos} | Gastos: ${gastos}")

    def exportar_a_csv(self, nombre_archivo):
        with open(nombre_archivo, 'w', newline='') as archivo_csv:
            campos = ['Fecha', 'Tipo', 'Categoría', 'Descripción', 'Monto']
            escritor_csv = csv.DictWriter(archivo_csv, fieldnames=campos)
            escritor_csv.writeheader()
            for transaccion in self.lista_transacciones:
                escritor_csv.writerow(vars(transaccion))

    def importar_desde_csv(self, nombre_archivo):
        try:
            with open(nombre_archivo, 'r') as archivo_csv:
                lector_csv = csv.DictReader(archivo_csv)
                for fila in lector_csv:
                    fecha = datetime.strptime(fila['Fecha'], '%Y-%m-%d')
                    tipo = fila['Tipo']
                    categoria = fila['Categoría']
                    descripcion = fila['Descripción']
                    monto = float(fila['Monto'])
                    nueva_transaccion = Transaccion(fecha, tipo, categoria, descripcion, monto)
                    self.lista_transacciones.append(nueva_transaccion)
            print("Datos importados exitosamente.")
        except FileNotFoundError:
            print("El archivo no existe.")
        except Exception as e:
            print(f"Error al importar datos: {e}")


class Contacto:
    def __init__(self, nombre, telefono, correo):
        self.nombre = nombre
        self.telefono = telefono
        self.correo = correo
        self.eliminado = False  
        
    def mostrar_informacion(self):
        print(f"Nombre: {self.nombre}")
        print(f"Teléfono: {self.telefono}")
        print(f"Correo: {self.correo}")

class Agenda:
    def __init__(self):
        self.contactos = []

    def agregar_contacto(self, contacto):
        self.contactos.append(contacto)
        print("Contacto agregado exitosamente.")

    def mostrar_contactos(self, incluir_eliminados=False):
        print("\nLista de Contactos:")
        for i, contacto in enumerate(self.contactos):
            if not contacto.eliminado or incluir_eliminados:
                print(f"{i + 1}.")
                contacto.mostrar_informacion()
                print("------------------------")

    def buscar_contacto(self, nombre):
        for contacto in self.contactos:
            if contacto.nombre.lower() == nombre.lower() and not contacto.eliminado:
                return contacto
        return None

    def actualizar_contacto(self, nombre):
        contacto = self.buscar_contacto(nombre)
        if contacto:
            print("Ingrese los nuevos datos del contacto:")
            nuevo_nombre = input("Nuevo nombre: ")
            nuevo_telefono = input("Nuevo teléfono: ")
            nuevo_correo = input("Nuevo correo: ")
            contacto.nombre = nuevo_nombre
            contacto.telefono = nuevo_telefono
            contacto.correo = nuevo_correo
            print("Contacto actualizado exitosamente.")
        else:
            print(f"No se encontró un contacto con el nombre {nombre}.")

    def eliminar_contacto(self, nombre, eliminacion_logica=True):
        contacto = self.buscar_contacto(nombre)
        if contacto:
            if eliminacion_logica:
                contacto.eliminado = True
                print("Contacto eliminado lógicamente exitosamente.")
            else:
                self.contactos.remove(contacto)
                print("Contacto eliminado físicamente exitosamente.")
        else:
            print(f"No se encontró un contacto con el nombre {nombre}.")


class SistemaBlog:
    def __init__(self):
        self.usuarios = []
        self.posts = []
        self.comentarios = []

    def obtener_usuarios(self):
        url = "https://jsonplaceholder.typicode.com/users"
        respuesta = requests.get(url)
        self.usuarios = respuesta.json()

    def obtener_posts(self):
        url = "https://jsonplaceholder.typicode.com/posts"
        respuesta = requests.get(url)
        self.posts = respuesta.json()

    def obtener_comentarios(self):
        url = "https://jsonplaceholder.typicode.com/comments"
        respuesta = requests.get(url)
        self.comentarios = respuesta.json()

    def mostrar_info_usuario(self, id_usuario):
        usuario = next((u for u in self.usuarios if u['id'] == id_usuario), None)
        if usuario:
            print("\nInformación del Usuario:")
            print(f"ID: {usuario['id']}")
            print(f"Nombre: {usuario['name']}")
            print(f"Nombre de usuario: {usuario['username']}")
            print(f"Correo electrónico: {usuario['email']}")
            print("------------------------")
        else:
            print("Usuario no encontrado.")

    def mostrar_posts_usuario(self, id_usuario):
        posts_usuario = [p for p in self.posts if p['userId'] == id_usuario]
        if posts_usuario:
            print("\nPosts del Usuario:")
            for post in posts_usuario:
                print(f"ID del Post: {post['id']}")
                print(f"Título: {post['title']}")
                print(f"Cuerpo: {post['body']}")
                print("------------------------")
        else:
            print("Este usuario no tiene posts.")

    def mostrar_comentarios_post(self, id_post):
        comentarios_post = [c for c in self.comentarios if c['postId'] == id_post]
        if comentarios_post:
            print("\nComentarios del Post:")
            for comentario in comentarios_post:
                print(f"ID del Comentario: {comentario['id']}")
                print(f"Nombre: {comentario['name']}")
                print(f"Correo electrónico: {comentario['email']}")
                print(f"Cuerpo: {comentario['body']}")
                print("------------------------")
        else:
            print("Este post no tiene comentarios.")

    def crear_usuario(self, nombre, nombre_usuario, correo):
        nuevo_usuario = {
            'id': len(self.usuarios) + 1,
            'name': nombre,
            'username': nombre_usuario,
            'email': correo
        }
        self.usuarios.append(nuevo_usuario)
        print("Usuario creado exitosamente.")
        return nuevo_usuario

    def crear_post(self, id_usuario, titulo, cuerpo):
        nuevo_post = {
            'userId': id_usuario,
            'id': len(self.posts) + 1,
            'title': titulo,
            'body': cuerpo
        }
        self.posts.append(nuevo_post)
        print("Post creado exitosamente.")
        return nuevo_post

    def crear_comentario(self, id_post, nombre, correo, cuerpo):
        nuevo_comentario = {
            'postId': id_post,
            'id': len(self.comentarios) + 1,
            'name': nombre,
            'email': correo,
            'body': cuerpo
        }
        self.comentarios.append(nuevo_comentario)
        print("Comentario creado exitosamente.")
        return nuevo_comentario


productos = []
registros = []
clientes = {}
tareas = []
empleados = {}
horarios = []

while True:
    print("=================Menu de opciones ABECEDARIO 2023============================:")
    print("A = Suma de n numeros")
    print("B = Promedio de n notas con situacion academica y estado")
    print("C = Area de las figuras geometricas")
    print("D = Operaciones con matrices")
    print("E = Glorsario Python")
    print("F = Promedio de IDAT")
    print("G = Numero Capicua")
    print("H = Ordenamiento de Burbuja")    
    print("I = Adivina el numero en 3 intentos")
    print("J = Operaciones Basicas de n Numeros")
    print("K = Crud basico con listas")
    print("L = Carrito de Compras /Facturacion")
    print("M = Promedio UTP /Con Validaciones")
    print("N = Programa para Solución Integral para Tareas, Empleados y Horarios en la Oficina ")
    print("Ñ = Juego del Ahocardo con dos jugadores")
    print("O = Juego de Piedra Papel y Tijera")
    print("P = Encriptar y Desepcritar una palabra")
    print("Q = Contador de Letras de una palabra")
    print("R = Herramienta de Descarga de YouTube")
    print("S = Convertidor de Monedas (S/.) a otro tipo de moneda")
    print("T = Convertidor de Temperatura")
    print("U = Calculadora de IMC (Índice de Masa Corporal)")
    print("V = Calculadora de Factorial")
    print("W = Conversor de Números Romanos a Enteros")
    print("X = Sistema de Agenda de Contactos")
    print("Y = Sistema de Registros Financieros con CSV")
    print("Z = Sistema de Blogs con JSON")
    print("0 = Salir")

    opcion = input("Ingrese la letra de la opción que desea ejecutar (o '0' para salir): ").upper()

    if opcion == 'A' or opcion=="a":
        print("====SUMA DE N NUMEROS======")
        n = int(input("Ingrese la cantidad de números a sumar: "))
        suma = 0
        for _ in range(n):
            numero = float(input("Ingrese un número: "))
            suma += numero
        print(f"La suma de los números es: {suma}")

    elif opcion == 'B' or opcion=="b":
        print("====PROMEDIO DE N NUMEROS======")
        n = int(input("Ingrese la cantidad de notas: "))
        suma_notas = 0
        for _ in range(n):
            nota = float(input("Ingrese una nota: "))
            suma_notas += nota
        promedio = suma_notas / n

        if promedio >= 6:
            situacion = "Aprobado"
        else:
            situacion = "Reprobado"

        estado = "Regular" if n >= 3 else "Irregular"

        print(f"Promedio: {promedio}")
        print(f"Situación académica: {situacion}")
        print(f"Estado: {estado}")

    elif opcion == 'C'or opcion=="c":
        print("====AREA DE FIGURAS  GEOMETRICAS======")
        figura = input("Ingrese el nombre de la figura (cuadrado, triángulo, círculo): ").lower()
        
        if figura == 'cuadrado':
            lado = float(input("Ingrese el lado del cuadrado: "))
            area = lado * lado
        elif figura == 'triangulo':
            base = float(input("Ingrese la base del triángulo: "))
            altura = float(input("Ingrese la altura del triángulo: "))
            area = (base * altura) / 2
        elif figura == 'circulo':
            radio = float(input("Ingrese el radio del círculo: "))
            area = 3.1416 * radio**2
        else:
            print("Figura no válida. Intente nuevamente.")
            continue

        print(f"El área de la figura es: {area}")

    elif opcion == 'D' or opcion=="d":
        print("====OPERACIONES CON MATRICES ======")
        num_matrices = int(input("Ingrese el número de matrices a operar: "))

        if num_matrices < 1:
            print("Debe ingresar al menos una matriz.")
            continue

        suma_resultado = np.array(ingresar_matriz())
        producto_resultado = suma_resultado

        for _ in range(num_matrices - 1):
            suma_resultado = np.add(suma_resultado, np.array(ingresar_matriz()))

            producto_resultado = np.dot(producto_resultado, np.array(ingresar_matriz()))

        print("\nSuma de matrices:")
        print(suma_resultado)
        print("\nProducto de matrices:")
        print(producto_resultado)


    elif opcion == 'E' or opcion=="e":
        print("====GLOSARIO PYTHON ======")
        opciones=1
        while opciones!=27:
            print("\n")
            print("      |---------------------------–-----------------|")
            print("      |------------APRENDIENDO PYTHON---------------|")
            print("      |---------------------------------------------|\n")
            print("\n")

                
            print("[!] GLOSARIO\n")
            print("  1. Que es python?")
            print("  2. Estructura de datos")
            print("  3. Números en python ")
            print("  4. Operaciomes matemáticas simples")
            print("  5. Operaciones matemáticas avanzadas")
            print("  6. Variables")
            print("  7. Cadenas de texto (String-Str)")
            print("  8. Listas")
            print("  9. Diccionarios")
            print(" 10. Tuplas")
            print(" 11. Sets")
            print(" 12. Booleanos")
            print(" 13. Encadenando comparadores de operación")
            print(" 14. Condicionales if, elif y else")
            print(" 15. Ciclos For")
            print(" 16. Ciclos While")
            print(" 17. Usando While y Else")
            print(" 18. Palabras clave utiles (Extra)")
            print(" 19. Operadores Utiles (Extra)")
            print(" 20. Comprehension de listas")
            print(" 21. Funciones")
            print(" 22. Expresiones Lambda, Mapas y Filtros")
            print(" 23. Programación orientada a objetos")
            print(" 24. Modulos y paquetes en python")
            print(" 25. __name___ y '__main__'")
            print(" 26. Manejo de errores y excepciones")
            print(" 27. ACERCA DEL CREADOR DE ESTE PROGRAMA ")
            print("\n")
            print("ELIGE EL TEMA QUE QUIERAS!!\n")
            opciones = input("Elige el número con el tema que quieres trabajar\n---> ")

            if opciones =="1":
                print("                   QUE ES PYTHON?\n")
                print("Python es un lenguaje de programación multiparadigma en el\ncual puedes desarrollar todo tipo de programa que quieras,\npuedes desarrollar paginas web, interfaces graficas,\nhacking etico y muchas cosas mas,si te interesa el tema\nquedate aquí y sigue navegando en el programa,hay muchos\ntemas!! ")
                print("\n")
                
            if opciones =="2":
                print("                     ESTRUCTURA DE DATOS\n\n")
                print("NOMBRE                 TIPO          DESCRIPCION\n")
                print("Enteros                Int           3 500 50000\n")  
                print("Decimales              Float         2.5 6.76 56.856\n")
                print("Cadena de texto        Str          'Hola','Joel', '20.000' \n")      
                print("Listas                 List          [10,'Hola',200.4]\n")  
                print("Diccionarios           Dic           {'Palabra':'significado                                     ',clave:'valor'}\n")  
                print("Tuplas                 Tup           orden inmutable(10,'Hola',200,4)\n")  
                print("Sets                   Set           Coleccion de objetos no ordenados{'a','b'}\n")
                print("Booleanos              Bool          True o False\n\n")


            if opciones =="3":
                print("                       NUMEROS EN PYTHON\n")
                print("Enteros-(Int)\n")
                print("a=4+4")
                print("print(a)")
                print("resultado: 8\n")
                print("Tambien lo podemos imprimir así:\n")
                print("print(4+4)")
                print("resultado: 8\n\n")
                print("Decimales-(Float)\n")
                print("b=4.5+4.56")
                print("print(b)")
                print("resultado: 9.05999...")
                print("\n")
                
            if opciones =="4":
                    print("             Operaciones matemáticas simples\n".upper())
                    print("Podemos hacer restas, sumas, multiplicacion y division de la siguiente manera:\n")
                    print("RESTAS (-)\n")
                    print("a=4-4")
                    print("print(a)")
                    print("resultado: 0\n\n")
                    print("SUMAS (+)\n")
                    print("b=5+5")
                    print("print(b)")
                    print("resultado: 10\n\n")
                    print("MULTIPLICACION (*)\n")
                    print("c=2*2")
                    print("print(c)")
                    print("resultado: 4\n\n")
                    print("DIVISION (/)\n")
                    print("d=4/2")
                    print("print(d)")
                    print("resultado: 2\n\n")

            if opciones=="5":
                    print("           OPERACIONES MATEMATICAS AVANZADAS")
                    print("MODULUS\n")
                    print("Modulus lo que hace es retornar la sobra de la division, ver si el numero es divisible, o si es par o impar para\nello utilizamos este signo(%)\n")
                    print("RESTO O SOBRA\n")
                    print("a=7%4")
                    print("print(a)")
                    print("resultado: 3\n")
                    print("DIVISIBLE\n")
                    print("a=50%5")
                    print("print(a)")
                    print("resultado: 0\n")
                    print("PAR\n")
                    print("a=23%1")
                    print("print(a)")
                    print("resultado: 0 ←par\n\n")
                    print("IMPAR\n")
                    print("a=23%2")
                    print("print(a)")
                    print("resultado: 1 ←impar\n\n\n")
                    print("POTENCIA\n")
                    print("La potencia de cada numero, lo que hace es que eleva o \nmultiplica 2 veces el numero que queremos multiplicar, para ello utilizamos dos veces el signo de multiplicar(**)")
                    print("p=20**2")
                    print("print(p)")
                    print("resultado: 400\n")
                    print("p2=10**2")
                    print("print(p2)")
                    print("resultado: 100\n")
                    print("Tambien podemos hacer operaciones mas complejas a esto se le conoce como Betmas usando los signos de operaciones\nmatematicas de la siguiente manera:\n")
                    print("BETMAS\n")
                    print("a=2+10*10+4")
                    print("print(a)")
                    print("resultado: 106\n\n")
                    print("a=(2+10)*(10+4)")
                    print("print(a)")
                    print("resultado: 168\n\n") 
                    
            if opciones =="6":
                print("                     VARIABLES")
                print("Acabamos de trabajar con numeros,pero es dificil saber que\nrepresentan estos numeros si no les asignamos una variable.\n")
                print("Seria bueno asignar a estos tipos de datos un nombre para\npoder reconocerlos.\n\n")
                print("Por ejemplo:\n\n")
                print("Mis_casas=2\n")
                print("Reglas para nombrar variables:\n")
                print("[]Se considera buena practica usar nombres en minúsculas.\n")
                print("[] Evita usar palabras con significado especial como\n'list' o 'Str'.\n\n")
                print("Python usa nomenclatura dinámica\n")
                print("[]Esto significa que puedes re-asignar variables a otros\ntipos de datos.\n")
                print("[]Esto hace python bastante flexible al momento de asignar\nvariables\n")
                print("mis_casas = 2\n")
                print("mis_casas = ['casa1','casa2'\n")
                print("Esto es correcto en python!!\n")
                
            if opciones =="7":
                print("                    CADENAS DE TEXTO  \n")
                print("Las cadenas de texto son secuencias de caracter,\nusan sintaxis con comillas simples o comillas dobles\n")
                print("[] 'Hola'\n")
                print("[]  caracter = 'cadena de texto con muchos caracteres'\n")
                print("Debido a que las cadenas de texto son secuencias ordenadas\nsignifica que podemos usar indexado y slicing para agarrar\nsub-secciones de una cadena.\n")
                print("Notacion de indexado: [], asignado despues de la cadena\n")
                print("Imdexado: Permite agarrar un caracter singular de una cadena de texto.\n")
                print("Slicing: Permite agarrar una subseccion de multiples\ncaracteres, un 'slice' de una cadena.\n")
                print("Tiene la siguiente sintaxis:\n")
                print("[start:stop:step]→[0:4:2]\n")
                print("Start: Es un indice numerico para el slice iniciar.\n")
                print("Stop: Es el numero donde paramos el slice.\n")
                print("Step: Son los pasos que damos.\n\n")
                print("Indexado:\n")
                print("micadena=('Hola Mundo')")
                print("print(micadena[2]")
                print("resultado: l \n\n")
                print("Slicing:\n")
                print("micadena = 'Hola Mundo'\n")
                print("print(micadena[0:4]")
                print("resultado: Hola\n\n")
                
            if opciones =="8":
                    print("                          LISTAS \n")
                    print("Las listas son secuencias ordenadas que guardan una variedad de tipos de datos")
                    print("Usan [] braquets y comas para separar objetos en una lista:\n")
                    print("[1,2,3,4,5]\n")
                    print("Las listas soportan indexados y slicing\n")
                    print("Puedes tener listas adentro de listas y pueden guardar\nmetodos que pueden ser llamados.\n")
                    print("milista=[1,2,3]")
                    print("print(milista)")
                    print("resultado: [1,2,3]\n\n")

            if opciones =="9":
                    print("                      DICCIONARIOS\n ")
                    print("[] Son mapeos desordenados para guaradar objetos\n")
                    print("[] Previamente vimos como las listas guardan objetos en una secuencia ordenada\n")
                    print("[] Los diccionarios utilizan orden basado en par\nclave/valor.\n")
                    print("[] Los diccionarios usan llaves abiertas y cerradas {} y dos puntos : para simbolizar las llaves y su valor asociado.\n\n")
                    print("Cuando deberiamos escoger una lista o un diccionario?\n")
                    print("[] Diccionarios: Objetos retornados por llave\n")
                    print("[] Desordenado y no se guarda, bueno para cuando no\nsabes donde se encuentra algo\n")
                    print("Listas: Objetos retornados por locación\n")
                    print("[] Puede ser Indexado o Slicing\n\n")
                    print("mi_diccionario = {'llave1':'valor1','llave2':'valor2'}")
                    print("print(mi_diccionario)")
                    print("resultado: {'llave1':'valor1','llave2':'valor2'}\n\n")
                    print("mi_diccionario = {'llave1':'valor1','llave2':'valor2'}")
                    print("print(mi_diccionario['llave1'])")
                    print("resultado: valor1\n\n")
            
            if opciones =="10":
                print("                        TUPLAS\n")
                print("Las tuplas son similares a las listas.Sin embargo, tienen\nuna diferencia (inmutabilidad)\n")
                print("Una vez que un elemento se encuentra en una tupla, este no\npuede ser re-asignado.\n")
                print("Las tuplas usan parentesis: (1,2,3)\n")
                print("t=('a','a','b')")
                print("t[0]='Nuevo'")
                print("print(t)\n")
                print("Esto dará un error ya que las tuplas no se pueden re-asignar\n")
                
            if opciones =="11":
                print("                            SETS\n")
                print("Los sets son una coleccion unica y deaordenada de elementos.\n")
                print("Solamente puede haber UNA representacion del mismo objeto.\n\n")
                print("miset = set()")
                print("miset.add (1)")
                print("miset.add (2)")
                print("print(miset)")
                print("resultado: {1,2}\n")
                
            if opciones =="12":
                print("                       BOOLEANOS\n")
                print("Los booleanos son valores que permiten declarar verdadero o falso.\n")
                print("Son muy importantes cuando quieres hacer logicas.\n")
                print("print(2>3)")
                print("False\n")
                print("print(2<3)")
                print("True\n")
                print("print(2==3)")
                print("False\n")
                print("print(2>=2)")
                print("True\n\n")
                print("  COMPARADORES DE OPERACION\n")
                print("== comparacion (a==b) Falso\n")
                print("<> Mayor o menor (2>3) Falso, (2<3) Verdadero\n")
                print(">= Mayor o igual a (2>=2) Verdadero, (2>=3) Falso\n")
                print("<= Menor o igual a (1<=2) Verdadero, (2<=1) Falso\n")
                print("!= No son iguales (a!=b) Verdadero, (a!=a) Falso\n\n")
                
            if opciones =="13":
                print("        ENCADENANDO COMPARADORES DE OPERACION\n")
                print("Podemos usar operadores logicos para combinar comparaciones:\n")
                print("[] And\n")
                print("[] Or\n")
                print("[] Not\n")
                print("1<2 and 2<3")
                print("True\n")
                print("'y'=='y' or 3==3")
                print("True\n")
                print("300>6000")
                print("False\n")
                print("not 300>6000")
                print("True\n\n")
                
            if opciones =="14":
                print("            CONDICIONALES IF, ELIF, ELSE\n")
                print("Usamos las declaraciones para controlar el flujo de nuestro programa\n")
                print("Usualmente solo queremos que ciero código sea ejecutado\ncuando una condicion particular ocurra.\n")
                print("Por ejemplo, if mi perro tiene hambre aplicar logica),\nelse (aplicar logica si mi perro no tiene hambre)\n")
                print("Para controlar este flujo de logica usamos palabras clave:\n")
                print("[] if\n")
                print("[] elif\n")
                print("[] else\n")
                print("\n")
                print("COMO DECLARAMOS ESTAS CONDICIONES?\n\n")
                print("Sintaxis de una condicion (if)\n")
                print("if alguna_conficion:\n\n")
                print("Sintaxis de una declaracion (if/else)\n")
                print("if alguna_condicion:")
                print("    ejecutamos codigo\n")
                print("if opcion == "":")
                print("  aplicar algo mas\n\n")
                print("Sintaxis de una declaracion elif\n")
                print("if alguna_condicion:")
                print("       ejecutamos codigo\n")
                print("elif alguna_otra_condicion:")
                print("            algo distinto\n")
                print("if opcion == "":")
                print("   hacer algo mas\n\n")
                print("Ejemplo:\n")
                print("aprendiendo = True")
                print("if aprendiendo == True:")
                print("    print('Estamos aprendiendo')\n")
                print("if opcion == "":")
                print("   print('No estamos aprendiendo')")
                print("resultado: Estamos aprendiendo\n")
                print("si fuera false, el resultado seria No estamos aprendiendo\n\n")
                
            if opciones =="15":
                print("                        CICLOS FOR\n")
                print("Varios objetos en python son 'iterables', significa que podemos iterar sobre cada elemento en el objeto\n")
                print("Podemos iterar a travez de una lista o todos los caracteres en una cadena de texto\n")
                print("Podemos usar ciclos, For para ejecutar un bloque de codigo en cada iteracion\n")
                print("Sintaxis para un ciclo for:\n")
                print("lista_iterable = [1,2,3]")
                print("for nombre_item in lista_iterable:")
                print("          print(nombre_item)\n\n")
                print("Ejemplo:\n")
                print("milista=[1,2,3,4,5,6,7,8,9,10]")
                print("for num in milista:")
                print("       print(num)")
                print("resultado: \n")
                print("1\n2\n3\n4\n5\n6\n7\n8\n9\n10\n\n")
                print("milista=[1,2,3,4,5,6,7,8,9,10]")
                print("for num in milista:")
                print("       print('hola')")
                print("resultado: \n")
                print("hola\nhola\nhola\nhola\nhola\nhola\nhola\nhola\nhola\nhola\n\n")
                
            if opciones =="16":
                print("                    CICLOS WHILE\n\n")
                print("Los ciclos while van a continuar ejecutando un bloque\nde codigo. While (mientras) una condicion siga siendo\nverdadera\n\n")
                print("Sintaxis para ciclo while:\n")
                print("while condicion_booleana:")
                print("           hacer algo\n\n")
                print("Puedes combinar con if opcion == "":\n")
                print("while condicion_booleana:")
                print("           hacer algo")
                print("if opcion == "":")
                print("   hacer algo distinto\n\n")
                print("Ejemplo:\n")
                print("x=0")
                print("while x < 5:")
                print("      print(f'El valor actual de x es{x}')")
                print("x= x+1")
                print("resultado: El valor de x es 0\nEl valor de x es 1\nEl valor de x es 2\nEl valor de x es 3\nEl valor de x es 4\nEl valor de x es 5\n\n")
                
            if opciones == "17":
                print("                USANDO WHILE Y ELSE\n\n")
                print("x = 0")
                print("while x < 5:")
                print("      print(f'El valor actual de x es {x}')\n")
                print("if opcion == "":")
                print("print('El ciclo terminó!!)")
                print("resultado: El valor de x es 0\nEl valor de x es 1\nEl valor de x es 2\nEl valor de x es 3\nEl valor de x es 4\nEl valor de x es 5\nEl ciclo terminó!!\n\n")
                
            if opciones =="18":
                print("                 PALABRAS CLAVE UTILES (EXTRA)\n\n")
                print("pass: Sirve para pasar de un problema o para saltar\nel problema\n")
                print("Ejemplo:\n")
                print("x=[1,2,3]")
                print("for item in x:")
                print("     #comentario")
                print("print('Fin del programa')\n")
                print("ESTO DARÁ UN ERROR\n\n")
                print("x=[1,2,3]")
                print("for item in x:")
                print("     #comentario")
                print("     pass")
                print("print('Fin del programa')")
                print("Fin del programa\n\n")
                print("continue: Se usa para saltar letras o palabras\n\nEjemplo:\n")
                print("x=Python")
                print("for letra in x:")
                print("      if letra =='y':")
                print("           continue")
                print("      print('letra')")
                print("resultado: Pthon\n\n")
                print("break: Se usa para parar o romper las cadenas o el bloque de codigo donde quieras que se detenga\n\nEjemplo:\n")
                print("x='Python'")
                print("for letra in x:")
                print("      if letra =='t':")
                print("             break")
                print("      print(letra)")
                print("resultado: Py\n")
                print("Como ves se detiene en la letra t\n\n")
                
            if opciones =="19":
                print("                   OPERADORES UTILES (EXTRA)\n\n")
                print("range: Sirve para colocar un rango a los numeros o palabras que queramos\n")
                print("Ejemplo:\n")
                print("for num in range(10):")
                print("        print('num')")
                print("resultado: \n0\n1\n2\n3\n4\n5\n6\n7\n8\n9\n")
                print("El numero 10 no se muestra ya que python lo cuenta desde el numero cero, si queremos que aparesca el numero 10 tenemos\nque escribir en range el numero 11.\n\n")
                print("input: Sirve para las entradas que ingrese el usuario.\n")
                print("Ejemplo:\n")
                print("resultado = input('Escribe un numero aquí')")
                print("print(resultado)")
                print("resultado:\n Escribe un numero aquí\n")
                print("Como ves te aparecerá para que escribas un numero o texto y esto es lo que aparece despues\n")
                print("Escribe un numero aquí 10")
                print("10\n\n")
                
            if opciones =="20":
                print("                COMPREHENSION DE LISTAS\n\n")
                print("Manera unica de crear una lista de python rapidamente\n")
                print("Si te encuentras usando un ciclo for con .append() para\ncrear una lista, puedes usar una comprehension de lista en\nsu lugar\n\n")
                print("Con metodo .append()\n")
                print("mi_cadena = 'hola'")
                print("mi_lista = []")
                print("for letras in mi_cadena:")
                print("       mi_lista.append(letras)")
                print("print(mi_lista)")
                print("resultado:\n['h','o','l','a']\n\n")
                print("Con metodo comprehension de listas:\n\n")
                print("mi_lista = [x for x in range(0,11)]")
                print("print(mi_lista)")
                print("resultado:\n")
                print("[1,2,3,4,5,6,7,8,9,10]\n")
                print("Mucho mas rapido!!\n\n")
                
            if opciones =="21":
                print("                            FUNCIONES\n\n")
                print("Las funciones sirven para crear codigo limpio,ordenado y\nrepetible es muy importante para nosotros ser efectivos\nprogramando\n")
                print("Las funciones son un gran salto en tu carrera como\nprogramador python.\n")
                print("Esto significa que los problemas se pondran mas dificiles!\n\n")
                print("Sintaxis de funciones:\n")
                print("Crear funciones requiere de una sintaxis especial, empezamos con def.\n")
                print("veamos una funcion:\n")
                print("def nombre_de_funcion(nombre):")
                print("#corremos codigo")
                print("          print('Las funciones retornan algo' + nombre\n\n")
                print("Tipicamente usamos la palabra clave return para retornar el valor de una funcion\n")
                print("Funcion de suma:\n")
                print("def suma(num1,num2):")
                print("      return num1+num2\n\n")
                print("Ejemplo:\n\n")
                print("def decir_hola():")
                print("     print('Hola')")
                print("     print('Como')")
                print("     print('Estas')")
                print("decir_hola()\n")
                print("resultado:\n\nHola\nComo\nEstas\n\n")
                    
            if opciones =="22":
                print("            EXPRESIONES LAMBDA,MAPAS Y FILTROS\n\n")
                print("Mapas: La funcion de mapa es muy utiñ cuando quieres llenar una funcion con una lidta de datos.\n")
                print("Ejemplo:\n")
                print("numeros = [1,2,3,4,5]")
                print("def raiz_cuadrada(num):")
                print("              resultado = num**2")
                print("              print(resultado)")
                print("              return resultado\n")
                print("for lista in map(raiz_cuadrada,numeros):")
                print("          print(lista)\n")
                print("resultado:\n\n1\n4\n9\n16\n25\n\n")
                print("Filtros: Esta funcion nos ayuda a hacer filtros\n")
                print("Ejemplo:\n")
                print("numeros pares:\n")
                print("numeros = [1,2,3,4,5,6,7]")
                print("def chequear_numeros_pares(num):")
                print("        return num % 2 == 0")
                print("for pares in filter(chequear_numeros_pares,numeros):")
                print("print(pares)\n")
                print("resultado:\n")
                print("2\n4\n6\n\n")
                print("Lambda: La funcion lambda se utiliza para hacer mas\nfunciones o cuando utilizamos mas funciones\n")
                print("Ejemplo:\n")
                print("raiz_cuadrada = lambda num: num**2")
                print("print(raiz_cuadrada(5))\n")
                print("resultado:\n25\n\n")
            
            if opciones =="23":
                print("              PROGRAMACION ORIENTADA A OBJETOS\n\n")
                print("[] Permite a los programadores crear sus propios objetos que tienen metodos y atributos.\n")
                print("[] Podemos llamar distintos metodos que se encuentran en una clase.\n")
                print("Veamos un ejemplo:\n")
                print("Sintaxis para metodos (class)\n")
                print("class nombre_clase():")
                print("       def __init__(self,param1,param2):")
                print("              self.param1 = param1")
                print("              self.param2 = param2")
                print("       def otra_funcion(self):")
                print("               #accion")
                print("               print(self.param1)\n\n")
                print("Ejemplo:\n")
                print("class Perro():")
                print("    def __init__(self,raza,nombre,puntos):")
                print("    self.raza = raza")
                print("    self.nombre = nombre")
                print("    self.puntos = puntos")
                print("huskie = Perro(raza='Huskie',nombre='Max',puntos=False\n\n")
                print("HERENCIA Y POLIMORFISMO:\n")
                print("class Animal():")
                print("   def __init__(self):")
                print("         print('ANIMAL CRADO')\n")
                print("   def quien_soy(self):")
                print("        print('soy un animal')\n")
                print("   def  comer(self):")
                print("       print('estoy comiendo')\n\n")
                print("   class Perro(Animal):")
                print("       def __init__(self):")
                print("            Animal.__init__(self):")
                print("               print('Perro Creado')")
                print("        def quien_soy(self):")
                print("            print('Soy un perro')")
                print("mi.Perro = Perro()")
                print("miperro.quien_soy()\n")
                print("resultado:\n")
                print("ANIMAL CREADO\nPerro Creado\nSoy un perro\n\n")
            
            if opciones =="24":
                print("              MODULOS Y PAQUETES\n\n")
                print("Modulos: Son simples archivos .py que llamamos desde otro\narchivo.\n")
                print("Paquetes: Son una coleccion de modulos\n")
                print("Crearemos nuestro propio modulo\n")
                print("De la clase pasada hablamos de las clases sobre el animal,\nperro lo importamos de la siguiente manera:\n")
                print("from clases import Animal,Perro\n")
                print("miPerro = Perro()")
                print("miPerro.quien_soy()\n")
                print("resultado:\nANIMAL CREADO\nPerro Creado\nSoy un perro\n\n")
                
            if opciones =="25":
                print("               __NAME___ Y '__MAIN__'\n\n")
                print("Cuando corremos codigo avanzado descargado del internet\nmuchas veces vemos esta linea de codigo en la parte de\nabajo.\n\n")
                print(" if __name__=='__main___':\n")
                print("Cuando importamos un modulo queremos saber si las funciones usadas estan siendo usadas como import o si estas en el\narchivo original del archivo .py del modulo.\n\n")
                print("Exploremos esto en codigo para entenderlo mejor!:\n\n")
                print("Archivo uno.py\n")
                print("def funcion():")
                print("       print('funcion() en UNO.py')")
                print("print('Nivel Top en UNO.py')\n")
                print("if __name__=='__main__':")
                print("       print('UNO.py está siendo corrido Directamente!!\n")
                print("if opcion == "":")
                print("   print('UNO.py esta siendo importado!!\n\n")
                print("resultado:\nNivel Top en UNO.py\nUNO.py está siendo corrido directamente!!\n\n")
                print("Archivo dos.py\n\n")
                print("import uno\n")
                print("print('Nivel Top en Dos.py')\n")
                print("uno.funcion()")
                print("if __name__=='__main__':")
                print("    print('Dos.py está siendo corrido directamente!!')\n")
                print("if opcion == "":")
                print("print('UNO.py está siendo importado!')\n\n")
                print("resultado:\n")
                print("Nivel Top en UNo.py\n")
                print("UNO.py está siendo importado!\n")
                print("Nivel Top en Dos.py\n")
                print("funcion() en UNO.py\n")
                print("Dos.py está siendo corrido directamente!!\n\n")
            
            if opciones =="26":
                print("               MANEJO DE ERRORES Y EXCEPCIONES\n\n")
                print("Podemos usar manejo de errores para poder planear posibles\ncasos de uso donde ocurra un error.\n")
                print("Usamos palabras claves:\n")
                print("Try: Esto bloquea el codigo de ser corrido.\n")
                print("Except: Bloque de codigo es ejecutado en caso de haber un\nerror en el bloque Try.\n")
                print("Finally: bloque de codigo ejecutado finalmente sin importar el error.\n\n")
                print("Ejemplos:\n")
                print("try:")
                print("  resultado: = 10+'10'\n")
                print("except:")
                print("   print('Parece que hay un error, escribe correctamente las variables')\n")
                print("resultado:\nParece que hay un erro, escribe correctamente las variables.\n\n")
                
            if opciones=="27":
                print("           ACERCA DEL CREADOR DE ESTE PROGRAMA\n\n")
                print("Nombre Completo del creador: Carlos Roberto Rodriguez Torres\n")
                print("Nombre del Programa: Aprendiendo Python\n")
                print("Whatsapp: +51991413707")
                print("Correo: pt72505342@gmail.com\n")
                print("MANDAME UN MENSAJE AL WHATSAPP SI TE GUSTÓ EL PROGRAMA :D \n")
                print("NO TE RINDAS LUCHA POR TUS SUEÑOS!!\n")

    elif opcion == 'F' or opcion=="f":
        print("========Promedio de IDAT====================")
        nota1 = float(input("Ingrese la nota 1: "))
        nota2 = float(input("Ingrese la nota 2: "))
        nota3 = float(input("Ingrese la nota 3: "))
        nota4 = float(input("Ingrese la nota 4: "))

        peso_nota1 = 0.04
        peso_nota2 = 0.12
        peso_nota3 = 0.24
        peso_nota4 = 0.6

        promedio_final = (nota1 * peso_nota1) + (nota2 * peso_nota2) + (nota3 * peso_nota3) + (nota4 * peso_nota4)

        situacion_academica = "Aprobado" if promedio_final >= 13 else "Desaprobado"

        if promedio_final >= 0 and promedio_final < 7:
            estado = "Pesimo"
        elif promedio_final < 10:
            estado = "Muy malo"
        elif promedio_final < 12:
            estado = "Malo"
        elif promedio_final < 13:
            estado = "Regular"
        elif promedio_final < 16:
            estado = "Bueno"
        elif promedio_final <= 20:
            estado = "Excelente"
        else:
            estado = "Nota no válida"

        print(f"\nPromedio final: {promedio_final}")
        print(f"Situación académica: {situacion_academica}")
        print(f"Estado: {estado}")
        
        break
    
    elif opcion == 'G' or opcion=="g":
        print("======NUMERO CAPICUA VERIIFICAR===================")
        num = int(input("Ingrese un número para verificar si es capicúa: "))
        if str(num) == str(num)[::-1]:
            print(f"{num} es un número capicúa.")
        else:
            print(f"{num} no es un número capicúa.")
        break
    
    elif opcion == 'H' or opcion=="h":
        cantidad = int(input("Ingrese la cantidad de números que desea ordenar: "))
        numeros = []
        for i in range(cantidad):
            numero = int(input(f"Ingrese el número {i + 1}: "))
            numeros.append(numero)

        print("Lista original:", numeros)

        n = len(numeros)
        for i in range(n - 1):
            for j in range(0, n - i - 1):
                if numeros[j] > numeros[j + 1]:
                    numeros[j], numeros[j + 1] = numeros[j + 1], numeros[j]

        print("Lista ordenada:", numeros)
    
    
    elif opcion == 'I' or opcion=="i":
        print("\n¡Bienvenido al juego de adivinanzas de números!")

        # Solicitar al usuario el rango de números
        try:
            rango_minimo = int(input("Ingresa el rango mínimo: "))
            rango_maximo = int(input("Ingresa el rango máximo: "))
        except ValueError:
            print("Por favor, ingresa números válidos para el rango.")
            continue

        # Validar que el rango sea válido
        if rango_minimo >= rango_maximo:
            print("Error: El rango mínimo debe ser menor que el rango máximo.")
            continue

        # Elegir un número aleatorio dentro del rango
        numero_a_adivinar = random.randint(rango_minimo, rango_maximo)

        print(f"Adivina el número entre {rango_minimo} y {rango_maximo}. Tienes 3 intentos.")

        intentos = 3

        while intentos > 0:
            # Solicitar al usuario que ingrese un número
            try:
                guess = int(input("Ingresa tu adivinanza: "))
            except ValueError:
                print("Por favor, ingresa un número válido.")
                continue

            # Verificar si el número es correcto
            if guess == numero_a_adivinar:
                print(f"¡Felicidades! Has adivinado el número {numero_a_adivinar}.")
                break
            else:
                # Proporcionar pistas de "cerca" o "lejos"
                diferencia_actual = abs(numero_a_adivinar - guess)
                if intentos == 3:
                    print("Cerca" if diferencia_actual <= 10 else "Lejos")
                elif intentos == 2:
                    print("Muy cerca" if diferencia_actual <= 5 else "Muy lejos")
                elif intentos == 1:
                    print("Extremadamente cerca" if diferencia_actual <= 2 else "Extremadamente lejos")

                intentos -= 1

        if intentos == 0:
            print(f"\nLo siento, te has quedado sin intentos. El número correcto era {numero_a_adivinar}.")

    
    elif opcion == 'J' or opcion=="j":
        print("\n--- OPERACIONES BÁSICAS CON N NÚMEROS ---")
        try:
            n = int(input("Ingresa la cantidad de números: "))
        except ValueError:
            print("Por favor, ingresa un número válido para la cantidad de números.")
            continue

        if n <= 0:
            print("Error: La cantidad de números debe ser mayor que cero.")
            continue

        # Inicializar una lista para almacenar los números
        numeros = []

        # Solicitar al usuario ingresar los números
        for i in range(n):
            try:
                numero = float(input(f"Ingrese el número {i + 1}: "))
                numeros.append(numero)
            except ValueError:
                print("Por favor, ingresa un número válido.")

        # Realizar operaciones básicas
        suma = sum(numeros)
        resta = numeros[0] - sum(numeros[1:])
        multiplicacion = 1
        for num in numeros:
            multiplicacion *= num
        division = numeros[0] if len(numeros) == 1 else numeros[0] / max(1, sum(numeros[1:]))

        # Mostrar resultados
        print("\nResultados:")
        print(f"Suma: {suma}")
        print(f"Resta: {resta}")
        print(f"Multiplicación: {multiplicacion}")
        print(f"División: {division}")
    
    elif opcion == 'K' or opcion=="k":
        print("\n--- CRUD Basico en Consola ---")
        while True:
            print("\n--- CRUD en Consola ---")
            print("1. Agregar Registro")
            print("2. Modificar Registro")
            print("3. Listar Registros")
            print("4. Eliminar Registro")
            print("5. Salir")

            try:
                opcion = int(input("Ingresa tu opción (1-5): "))
            except ValueError:
                print("Por favor, ingresa un número válido.")
                continue

            if opcion == 1:
                agregar_registro()
            elif opcion == 2:
                modificar_registro()
            elif opcion == 3:
                listar_registros()
            elif opcion == 4:
                eliminar_registro()
            elif opcion == 5:
                print("Gracias por usar el programa. ¡Hasta luego!")
                break
            else:
                print("Opción no válida. Por favor, elige un número del 1 al 5.")    
    
    
    
    
    elif opcion == 'L' or opcion=="l":
        print("\n--- Carrito de Compras ---")
        while True:
            print("\n--- Carrito de Compras ---")
            print("1. Agregar Producto")
            print("2. Mostrar Carrito")
            print("3. Registrar Cliente")
            print("4. Generar Factura")
            print("5. Salir")

            try:
                opcion = int(input("Ingresa tu opción (1-5): "))
            except ValueError:
                print("Por favor, ingresa un número válido.")
                continue

            if opcion == 1:
                agregar_producto()
            elif opcion == 2:
                mostrar_carrito()
            elif opcion == 3:
                registrar_cliente()
            elif opcion == 4:
                generar_factura()
            elif opcion == 5:
                print("Gracias por usar el programa. ¡Hasta luego!")
                break
            else:
                print("Opción no válida. Por favor, elige un número del 1 al 5.")


    elif opcion == 'm' or opcion=="M":
        print("\n--- PROMEDIO UTP / CON VALIDACIONES ---")
        try:
            cantidad_notas = int(input("Ingrese la cantidad de notas: "))
            total_puntos = 0
            total_pesos = 0

            for i in range(cantidad_notas):
                nombre_nota = input(f"Ingrese el nombre de la nota {i + 1}: ")
                nota = float(input(f"Ingrese la nota para {nombre_nota}: "))
                peso_porcentaje = float(input(f"Ingrese el peso en porcentaje para {nombre_nota}: "))
                peso_decimal = peso_porcentaje / 100  
                total_puntos += nota * peso_decimal
                total_pesos += peso_decimal

            promedio_ponderado = total_puntos / total_pesos

            print(f"\nPromedio Ponderado: {promedio_ponderado:.2f}")

            if 0 <= promedio_ponderado <= 5:
                estado = "Pesimo"
            elif 6 <= promedio_ponderado <= 11.4:
                estado = "Malo"
                falta_para_aprobar = 11.5 - promedio_ponderado
                print(f"Falta {falta_para_aprobar:.2f} para aprobar.")
            elif 11.5 <= promedio_ponderado <= 13:
                estado = "Regular"
            elif 13.1 <= promedio_ponderado <= 16:
                estado = "Bueno"
            elif 17 <= promedio_ponderado <= 18:
                estado = "Muy Bueno"
            elif 19 <= promedio_ponderado <= 20:
                estado = "Excelente"
            else:
                estado = "Fuera de rango"

            print(f"Estado: {estado}")

        except ValueError as e:
            print(f"Error: {e}")

    elif opcion == 'n' or opcion=="N":
        print("\n ----Programa para Solución Integral para Tareas, Empleados y Horarios en la Oficina-------------------------")
        while True:
            print("\n ----Programa para Solución Integral para Tareas, Empleados y Horarios en la Oficina:")
            print("1. Gestionar tareas")
            print("2. Gestionar empleados")
            print("3. Gestionar horarios")
            print("4. Mostrar listas, tuplas y diccionarios")
            print("5. Salir")

            opcion = input("Seleccione una opción (1-4): ")

            if opcion == "1":
                print("\n--- Gestión de Tareas ---")
                subopcion_tareas = input("Seleccione una opción (1: Agregar tarea, 2: Actualizar estado, 3: Mostrar tareas, 4: Volver): ")
                if subopcion_tareas == "1":
                    # Agregar tarea
                    nombre = input("Nombre de la tarea: ")
                    descripcion = input("Descripción de la tarea: ")
                    fecha_vencimiento = input("Fecha de vencimiento (YYYY-MM-DD): ")
                    agregar_tarea(tareas, nombre, descripcion, fecha_vencimiento)
                elif subopcion_tareas == "2":
                    # Actualizar estado de tarea
                    nombre = input("Nombre de la tarea a actualizar: ")
                    nuevo_estado = input("Nuevo estado de la tarea: ")
                    actualizar_estado_tarea(tareas, nombre, nuevo_estado)
                elif subopcion_tareas == "3":
                    # Mostrar tareas
                    imprimir_tareas(tareas)
                elif subopcion_tareas == "4":
                    pass
                else:
                    print("Opción no válida.")

            elif opcion == "2":
                print("\n--- Gestión de Empleados ---")
                subopcion_empleados = input("Seleccione una opción (1: Agregar empleado, 2: Actualizar cargo, 3: Mostrar empleados, 4: Volver): ")
                if subopcion_empleados == "1":
                    # Agregar empleado
                    id_empleado = input("DNI del empleado: ")
                    nombre = input("Nombre del empleado: ")
                    cargo = input("Cargo del empleado: ")
                    agregar_empleado(empleados, id_empleado, nombre, cargo)
                elif subopcion_empleados == "2":
                    # Actualizar cargo de empleado
                    id_empleado = input("DNI del empleado a actualizar: ")
                    nuevo_cargo = input("Nuevo cargo del empleado: ")
                    actualizar_cargo(empleados, id_empleado, nuevo_cargo)
                elif subopcion_empleados == "3":
                    # Mostrar empleados
                    imprimir_empleados(empleados)
                elif subopcion_empleados == "4":
                    pass
                else:
                    print("Opción no válida.")

            elif opcion == "3":
                print("\n--- Gestión de Horarios ---")
                subopcion_horarios = input("Seleccione una opción (1: Agregar horario, 2: Mostrar horarios, 3: Volver): ")
                if subopcion_horarios == "1":
                    # Agregar horario
                    dia = input("Día de la semana: ")
                    hora_inicio = input("Hora de inicio (HH:MM): ")
                    hora_fin = input("Hora de fin (HH:MM): ")
                    agregar_horario(horarios, dia, hora_inicio, hora_fin)
                elif subopcion_horarios == "2":
                    # Mostrar horarios
                    imprimir_horarios(horarios)
                elif subopcion_horarios == "3":
                    pass
                else:
                    print("Opción no válida.")
                    
            elif opcion == "4":
                print("\n--- Listas, Tuplas y Diccionarios ---")
                print("\nLista de tareas:")
                imprimir_tareas(tareas)

                print("\nLista de empleados:")
                imprimir_empleados(empleados)

                print("\nLista de horarios:")
                imprimir_horarios(horarios)

                print("\nDiccionario de empleados con horarios:")
                for id_empleado, detalles in empleados.items():
                    if "horarios" in detalles:
                        print(f"\nID: {id_empleado} - Nombre: {detalles['nombre']} - Horarios:")
                        imprimir_horarios(detalles['horarios'])

            elif opcion == "5":
                print("Saliendo del programa. ¡Hasta luego!")
                break

            else:
                print("Opción no válida. Por favor, seleccione una opción válida.")

    elif opcion == 'n' or opcion=="N":
        print("\n ----Juego del Ahocardo dos jugadores----------------")
        print("\n¡Bienvenido al juego del Ahorcado!")

        while True:
            print("\nMenú:")
            print("1. Ingresar palabra manualmente (Jugador 1)")
            print("2. Elegir palabra al azar (Jugador 1)")
            print("3. Salir")
            
            opcion = input("Seleccione una opción: ")
            if opcion == "1":
                palabra_secreta = seleccionar_palabra_manual()
                break
            elif opcion == "2":
                palabra_secreta = seleccionar_palabra_aleatoria()
                break
            elif opcion == "3":
                print("¡Hasta luego!")
                sys.exit()
            else:
                print("Opción no válida. Intente de nuevo.")

        letras_adivinadas = []
        intentos_maximos = 6
        intentos = 0

        while True:
            letra = input("\nJugador 2, ingresa una letra: ").lower()

            if letra.isalpha() and len(letra) == 1:
                if letra in letras_adivinadas:
                    print("Ya has adivinado esa letra. ¡Inténtalo de nuevo!")
                elif letra in palabra_secreta:
                    letras_adivinadas.append(letra)
                    print("¡Correcto!")
                else:
                    intentos += 1
                    print("Incorrecto. ¡Te quedan {} intentos!".format(intentos_maximos - intentos))
                    mostrar_ahorcado(intentos)
            else:
                print("Ingresa una letra válida.")

            print(mostrar_tablero(palabra_secreta, letras_adivinadas))

            if set(letras_adivinadas) == set(palabra_secreta):
                print("¡Felicidades! Has adivinado la palabra: '{}'".format(palabra_secreta))
                break

            if intentos == intentos_maximos:
                print("Lo siento, has agotado todos tus intentos. La palabra era: '{}'".format(palabra_secreta))
                mostrar_ahorcado(intentos)
                break
        
    elif opcion == 'O' or opcion=="o":
        print("\n ----Juego de Piedra Papel y Tijera----------------")
        print("Bienvenido a Piedra, Papel o Tijeras")
        while True:
            opcion_usuario = obtener_opcion_usuario()
            opcion_computadora = obtener_opcion_computadora()

            print(f"\nTu elección: {opcion_usuario}")
            print(f"Elección de la computadora: {opcion_computadora}")

            resultado = determinar_ganador(opcion_usuario, opcion_computadora)
            print(f"\nResultado: {resultado}\n")

            jugar_otra_vez = input("¿Quieres jugar otra vez? (s/n): ").lower()
            if jugar_otra_vez != 's':
                print("¡Gracias por jugar! Hasta luego.")
                break
            
    elif opcion == 'P' or opcion=="p":
        print("Generador de Contraseñas Seguras")
        longitud = int(input("Ingrese la longitud de la contraseña: "))

        # Generar contraseña segura
        contraseña = generar_contraseña(longitud)
        print(f"\nContraseña generada: {contraseña}")

        # Solicitar una palabra para encriptar y desencriptar
        palabra = input("\nIngrese una palabra para encriptar y desencriptar: ")

        # Generar clave para encriptación
        clave = Fernet.generate_key()

        # Encriptar la palabra
        palabra_encriptada = encriptar_contraseña(palabra, clave)
        print(f"\nPalabra encriptada: {palabra_encriptada}")

        # Desencriptar la palabra
        palabra_desencriptada = desencriptar_contraseña(palabra_encriptada, clave)
        print(f"Palabra desencriptada: {palabra_desencriptada}")

    elif opcion == 'Q' or opcion=="q":    
        print("Q = Contador de Letras de una palabra")
        palabra = input("Ingrese una palabra: ")
        num_vocales, num_consonantes, num_especiales = contar_vocales_consonantes(palabra)
        print(f"\nNúmero de vocales: {num_vocales}")
        print(f"Número de consonantes: {num_consonantes}")
        print(f"Número de caracteres especiales: {num_especiales}")
                
    elif opcion == 'R' or opcion=="r":    
        print("Herramienta de Descarga de YouTube")
        while True:
            print("\nOpciones:")
            print("1. Descargar en MP4")
            print("2. Descargar en MP3")
            print("3. Salir")

            opcion = input("Seleccione una opción (1/2/3): ")

            if opcion == '1':
                formato = 'mp4'
            elif opcion == '2':
                formato = 'mp3'
            elif opcion == '3':
                print("Saliendo...")
                break
            else:
                print("Opción no válida. Intente de nuevo.")
                continue

            url = input("Ingrese la URL del video de YouTube: ")
            ruta_guardado = input("Ingrese la ruta de guardado (presiona Enter para usar la carpeta actual): ")

            # Descargar el video o audio
            descargar_video(url, formato, ruta_guardado)
            
            
    elif opcion == 's' or opcion=="S":    
        print("--Convertidor de Monedas (S/.) a otro tipo de moneda--")
        monto = float(input("Ingrese el monto en Soles (PEN): "))
        moneda_origen = "PEN"

        # Definir monedas de destino comunes
        monedas_destino = ["USD", "MXN", "ARS", "COP", "EUR", "BRL", "PYG", "GTQ", "CUP", "BOB", "VEF"]

        # Mostrar las monedas de destino disponibles
        print("\nMonedas de Destino Disponibles:")
        for moneda in monedas_destino:
            print(moneda)

        # Ingresar la moneda de destino
        moneda_destino = input("Ingrese el código de la moneda de destino: ")

        # Validar la moneda de destino
        if moneda_destino not in monedas_destino:
            print("Código de moneda no válido.")
            sys.exit()


        # Realizar la conversión
        resultado = convertir_monedas(monto, moneda_origen, moneda_destino)

        # Mostrar el resultado
        print(f"\n{monto} {moneda_origen} es equivalente a {resultado:.2f} {moneda_destino}")


    elif opcion == 'T' or opcion=="t":    
        print("-----Convertidor de Temperatura------------")
        temperatura = float(input("Ingrese la temperatura: "))
        escala_origen = input("Ingrese la escala de origen (C o F): ").upper()
        escala_destino = input("Ingrese la escala de destino (C o F): ").upper()

        resultado_conversion = convertir_temperatura(temperatura, escala_origen, escala_destino)
        print(f"Resultado de la conversión: {resultado_conversion}")
    
    elif opcion == 'u' or opcion=="U":    
        print("Calculadora de IMC (Índice de Masa Corporal)")
        peso_usuario = float(input("Ingrese su peso en kg: "))
        altura_usuario = float(input("Ingrese su altura en metros: "))

        resultado_imc = calcular_imc(peso_usuario, altura_usuario)
        print(f"Su Índice de Masa Corporal (IMC) es: {resultado_imc:.2f}")
    
    elif opcion == 'v' or opcion=="V":    
        print("---Calculadora de Factorial-----")
        numero_usuario = int(input("Ingrese un número para calcular su factorial: "))
        resultado_factorial = calcular_factorial(numero_usuario)
        print(f"El factorial de {numero_usuario} es: {resultado_factorial}")
    
    elif opcion == 'w' or opcion=="W":    
        print("--- Conversor de Números Romanos a Enteros-----")
        numero_romano = input("Ingrese un número romano: ")
        numero_entero = romano_a_entero(numero_romano)
        print(f"El equivalente en números enteros es: {numero_entero}")
    
    elif opcion == 'x' or opcion=="X":    
        print("----Sistema de Agenda de Contactos-----")
        agenda = Agenda()
        while True:
            print("\nSistema de Agenda de Contactos")
            print("1. Agregar Contacto")
            print("2. Mostrar Contactos")
            print("3. Actualizar Contacto")
            print("4. Eliminar Contacto (Lógicamente)")
            print("5. Eliminar Contacto (Físicamente)")
            print("0. Salir")

            opcion = input("Seleccione una opción: ")

            if opcion == '1':
                nombre = input("Ingrese el nombre del contacto: ")
                telefono = input("Ingrese el teléfono del contacto: ")
                correo = input("Ingrese el correo del contacto: ")
                nuevo_contacto = Contacto(nombre, telefono, correo)
                agenda.agregar_contacto(nuevo_contacto)
            elif opcion == '2':
                incluir_eliminados = input("¿Desea incluir contactos eliminados lógicamente? (S/N): ").upper() == 'S'
                agenda.mostrar_contactos(incluir_eliminados)
            elif opcion == '3':
                nombre_actualizar = input("Ingrese el nombre del contacto a actualizar: ")
                agenda.actualizar_contacto(nombre_actualizar)
            elif opcion == '4':
                nombre_eliminar_logico = input("Ingrese el nombre del contacto a eliminar lógicamente: ")
                agenda.eliminar_contacto(nombre_eliminar_logico)
            elif opcion == '5':
                nombre_eliminar_fisico = input("Ingrese el nombre del contacto a eliminar físicamente: ")
                agenda.eliminar_contacto(nombre_eliminar_fisico, eliminacion_logica=False)
            elif opcion == '0':
                print("Saliendo del programa.")
                break
            else:
                print("Opción no válida. Inténtelo de nuevo.")

    elif opcion == 'y' or opcion=="Y":    
        print("--Sistema de Registros Financieros con CSV------")
        registro_financiero = RegistroFinanciero()
        while True:
            print("--Sistema de Registros Financieros con CSV------")
            print("1. Registrar Gasto")
            print("2. Registrar Ahorro")
            print("3. Mostrar Transacciones")
            print("4. Calcular Balance")
            print("5. Exportar a CSV")
            print("6. Importar desde CSV")
            print("0. Salir")

            opcion = input("Seleccione una opción: ")

            if opcion == '1':
                fecha = datetime.now()
                categoria = input("Ingrese la categoría del gasto: ")
                descripcion = input("Ingrese la descripción del gasto: ")
                monto = float(input("Ingrese el monto del gasto: "))
                nueva_transaccion = Transaccion(fecha, 'Gasto', categoria, descripcion, monto)
                registro_financiero.agregar_transaccion(nueva_transaccion)
            elif opcion == '2':
                fecha = datetime.now()
                categoria = input("Ingrese la categoría del ahorro: ")
                descripcion = input("Ingrese la descripción del ahorro: ")
                monto = float(input("Ingrese el monto del ahorro: "))
                nueva_transaccion = Transaccion(fecha, 'Ingreso', categoria, descripcion, monto)
                registro_financiero.agregar_transaccion(nueva_transaccion)
            elif opcion == '3':
                tipo_filtro = input("Filtrar por tipo (Gasto/Ingreso) o presione Enter para mostrar todo: ").capitalize()
                registro_financiero.mostrar_transacciones(tipo=tipo_filtro)
            elif opcion == '4':
                registro_financiero.calcular_balance()
            elif opcion == '5':
                nombre_archivo = input("Ingrese el nombre del archivo CSV para exportar: ")
                registro_financiero.exportar_a_csv(nombre_archivo)
            elif opcion == '6':
                nombre_archivo = input("Ingrese el nombre del archivo CSV para importar: ")
                registro_financiero.importar_desde_csv(nombre_archivo)
            elif opcion == '0':
                print("Saliendo del programa.")
                break
            else:
                print("Opción no válida. Inténtelo de nuevo.")
            
    elif opcion == 'z' or opcion=="Z":    
        print("----------Sistema de Blogs con JSON-------------")
        sistema_blog = SistemaBlog()
        sistema_blog.obtener_usuarios()
        sistema_blog.obtener_posts()
        sistema_blog.obtener_comentarios()

        while True:
            print("----------Sistema de Blogs con JSON-------------")
            print("1. Mostrar Información de Usuario")
            print("2. Mostrar Posts de Usuario")
            print("3. Mostrar Comentarios de Post")
            print("4. Crear Usuario")
            print("5. Crear Post")
            print("6. Crear Comentario")
            print("0. Salir")

            opcion = input("Selecciona una opción: ")

            if opcion == '1':
                id_usuario = int(input("Ingresa el ID del usuario: "))
                sistema_blog.mostrar_info_usuario(id_usuario)
            elif opcion == '2':
                id_usuario = int(input("Ingresa el ID del usuario: "))
                sistema_blog.mostrar_posts_usuario(id_usuario)
            elif opcion == '3':
                id_post = int(input("Ingresa el ID del post: "))
                sistema_blog.mostrar_comentarios_post(id_post)
            elif opcion == '4':
                nombre = input("Ingresa el nombre del usuario: ")
                nombre_usuario = input("Ingresa el nombre de usuario: ")
                correo = input("Ingresa el correo electrónico del usuario: ")
                sistema_blog.crear_usuario(nombre, nombre_usuario, correo)
            elif opcion == '5':
                id_usuario = int(input("Ingresa el ID del usuario: "))
                titulo = input("Ingresa el título del post: ")
                cuerpo = input("Ingresa el cuerpo del post: ")
                sistema_blog.crear_post(id_usuario, titulo, cuerpo)
            elif opcion == '6':
                id_post = int(input("Ingresa el ID del post: "))
                nombre = input("Ingresa tu nombre: ")
                correo = input("Ingresa tu correo electrónico: ")
                cuerpo = input("Ingresa el cuerpo del comentario: ")
                sistema_blog.crear_comentario(id_post, nombre, correo, cuerpo)
            elif opcion == '0':
                print("Saliendo del Sistema de Blog. ¡Hasta luego!")
                break
            else:
                print("Opción no válida. Intenta de nuevo.")
            
    if opcion == '0':
        print(" ---Gracias Por Usar el Programa--- \n")
        print(" ---Creado Por:--- \n")
        print("Nombre Completo del creador: Carlos Roberto Rodriguez Torres\n")
        print("Nombre del Programa: Menu de opciones ABECEDARIO 2023\n")
        print("Whatsapp: +51991413707")
        print("Correo: pt72505342@gmail.com\n")
        print("MANDAME UN MENSAJE AL WHATSAPP SI TE GUSTÓ EL PROGRAMA :D \n")
        print("NO TE RINDAS LUCHA POR TUS SUEÑOS!!\n")        
        break







