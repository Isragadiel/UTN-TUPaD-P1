# Actividades
# 1) Dado el diccionario precios_frutas
# precios_frutas = {'Banana': 1200, 'Ananá': 2500, 'Melón': 3000, 'Uva':
# 1450}
# Añadir las siguientes frutas con sus respectivos precios:
# ● Naranja = 1200
# ● Manzana = 1500
# ● Pera = 2300
from collections import deque
import math

precios_frutas = {'Banana': 1200, 'Ananá': 2500, 'Melón': 3000, 'Uva': 1450}
precios_frutas['Naranja'] = 1200
precios_frutas['Manzana'] = 1500
precios_frutas['Pera'] = 2300
print(precios_frutas)

# 2) Siguiendo con el diccionario precios_frutas que resulta luego de ejecutar el código
# desarrollado en el punto anterior, actualizar los precios de las siguientes frutas:
# ● Banana = 1330
# ● Manzana = 1700
# ● Melón = 2800
precios_frutas["Banana"]= 1330
precios_frutas["Manzana"]= 1700
precios_frutas["Melón"]= 2800
print(precios_frutas)

# 3) Siguiendo con el diccionario precios_frutas que resulta luego de ejecutar el código
# desarrollado en el punto anterior, crear una lista que contenga únicamente las frutas sin los
# precios.
frutas= list(precios_frutas.keys())
print(frutas )

# 4) Escribí un programa que permita almacenar y consultar números telefónicos.
# • Permití al usuario cargar 5 contactos con su nombre como clave y número como valor.
# • Luego, pedí un nombre y mostrale el número asociado, si existe.
# Ejemplo:
Contactos = {}
for i in range(5):
    nombre = input("Ingrese el nombre del contacto: ")
    numero = input("Ingrese el número de teléfono: ")
    Contactos[nombre] = numero
print(Contactos)
nombre_consulta = input("Ingrese el nombre del contacto a consultar: ")
if nombre_consulta in Contactos:
    print(f"El número de {nombre_consulta} es: {Contactos[nombre_consulta]}")
else:
    print(f"No se encontró el contacto: {nombre_consulta}")


# 5) Solicita al usuario una frase e imprime:
# • Las palabras únicas (usando un set).
# • Un diccionario con la cantidad de veces que aparece cada palabra.
# Ejemplo:
frase = input("Ingrese una frase: ")
palabras = frase.split()
palabras_unicas = set(palabras)
print("Palabras únicas:", palabras_unicas)
contador_palabras = {palabra: palabras.count(palabra) for palabra in palabras_unicas}
print("Cantidad de veces que aparece cada palabra:", contador_palabras)



# 6) Permití ingresar los nombres de 3 alumnos, y para cada uno una tupla de 3 notas.
# Luego, mostrá el promedio de cada alumno.
# Ejemplo:
def procesar_alumnos_y_notas():
    alumnos = {}

    print("--- Ingreso de datos de alumnos ---")
    for i in range(3):
        while True:
            nombre = input(f"Ingrese el nombre del alumno {i+1}: ").strip()
            if nombre:
                break
            else:
                print("El nombre no puede estar vacío. Intente de nuevo.")

        while True:
            notas_str = input(f"Ingrese las 3 notas de {nombre} separadas por comas (ej. 7,8,9): ")
            try:
                notas_lista = [int(nota.strip()) for nota in notas_str.split(',')]
                if len(notas_lista) == 3:
                    alumnos[nombre] = tuple(notas_lista)
                    break
                else:
                    print("Debe ingresar exactamente 3 notas. Intente de nuevo.")
            except ValueError:
                print("Notas inválidas. Asegúrese de ingresar números enteros separados por comas. Intente de nuevo.")
            except Exception as e:
                print(f"Ocurrió un error inesperado: {e}. Intente de nuevo.")

    print("\n--- Promedios de los alumnos ---")
    if not alumnos:
        print("No se ingresaron datos de alumnos.")
    else:
        for nombre, notas in alumnos.items():
            promedio = sum(notas) / len(notas)
            print(f"El promedio de {nombre} es: {promedio:.2f}")

# Ejecutar el programa
if __name__ == "__main__":
    procesar_alumnos_y_notas()

# 7) Dado dos sets de números, representando dos listas de estudiantes que aprobaron Parcial 1
# y Parcial 2:
# • Mostrá los que aprobaron ambos parciales.
# • Mostrá los que aprobaron solo uno de los dos.
# • Mostrá la lista total de estudiantes que aprobaron al menos un parcial (sin repetir).
parcial_1 = {101, 102, 103, 104}
parcial_2 = {103, 104, 105, 106}

print("Aprobaron ambos parciales:", parcial_1 & parcial_2)
print("Aprobaron solo uno de los dos:", (parcial_1 | parcial_2) - (parcial_1 & parcial_2))
print("Aprobaron al menos un parcial:", parcial_1 | parcial_2)  


# 8) Armá un diccionario donde las claves sean nombres de productos y los valores su stock.
# Permití al usuario:
# • Consultar el stock de un producto ingresado.
# • Agregar unidades al stock si el producto ya existe.
# • Agregar un nuevo producto si no existe.
productos_stock = {}
def gestionar_stock_productos():
    while True:
        print("\n--- Gestión de Stock de Productos ---")
        print("1. Consultar stock de un producto")
        print("2. Agregar unidades al stock de un producto existente")
        print("3. Agregar un nuevo producto")
        print("4. Salir")

        opcion = input("Seleccione una opción (1-4): ")

        if opcion == '1':
            producto = input("Ingrese el nombre del producto a consultar: ")
            if producto in productos_stock:
                print(f"Stock de {producto}: {productos_stock[producto]} unidades")
            else:
                print(f"El producto '{producto}' no existe en el stock.")

        elif opcion == '2':
            producto = input("Ingrese el nombre del producto a actualizar: ")
            if producto in productos_stock:
                try:
                    unidades = int(input(f"Ingrese la cantidad de unidades a agregar al stock de {producto}: "))
                    productos_stock[producto] += unidades
                    print(f"Stock actualizado de {producto}: {productos_stock[producto]} unidades")
                except ValueError:
                    print("Cantidad inválida. Debe ingresar un número entero.")
            else:
                print(f"El producto '{producto}' no existe en el stock.")

        elif opcion == '3':
            producto = input("Ingrese el nombre del nuevo producto: ")
            if producto not in productos_stock:
                try:
                    unidades = int(input(f"Ingrese la cantidad inicial de unidades para {producto}: "))
                    productos_stock[producto] = unidades
                    print(f"Producto '{producto}' agregado con {unidades} unidades al stock.")
                except ValueError:
                    print("Cantidad inválida. Debe ingresar un número entero.")
            else:
                print(f"El producto '{producto}' ya existe en el stock.")

        elif opcion == '4':
            print("Saliendo del programa...")
            break

        else:
            print("Opción inválida. Intente nuevamente.")



# 9) Creá una agenda donde las claves sean tuplas de (día, hora) y los valores sean eventos.
# Ejemplo:
# Permití consultar qué actividad hay en cierto día y hora.
agenda = {
    (1, '10:00'): 'Reunión con el equipo',
    (1, '14:00'): 'Cita médica',
    (2, '09:00'): 'Clase de yoga',
    (3, '11:00'): 'Presentación del proyecto'
}
def consultar_agenda(dia, hora):
    evento = agenda.get((dia, hora))
    if evento:
        print(f"El evento programado para el día {dia} a las {hora} es: {evento}")
    else:
        print(f"No hay eventos programados para el día {dia} a las {hora}.")
# Ejemplo de uso
dia = int(input("Seleccione el día para consultar la agenda: "))
hora = input("Seleccione la hora para consultar la agenda: ")
consultar_agenda(dia, hora)


# 10) Dado un diccionario que mapea nombres de países con sus capitales, construí un nuevo
# diccionario donde:
# • Las capitales sean las claves.
# • Los países sean los valores.
# Ejemplo:
def invertir_diccionario_paises_capitales(diccionario_original):
    diccionario_invertido = {}
    for pais, capital in diccionario_original.items():
        diccionario_invertido[capital] = pais
    return diccionario_invertido

# Diccionario de ejemplo como el de la imagen
original_paises_capitales = {
    "Argentina": "Buenos Aires",
    "Chile": "Santiago",
    "España": "Madrid",
    "Francia": "París",
    "Alemania": "Berlín"
}

print("Diccionario original (País: Capital):")
print(original_paises_capitales)

# Invertir el diccionario
invertido_capitales_paises = invertir_diccionario_paises_capitales(original_paises_capitales)

print("\nNuevo diccionario (Capital: País):")
print(invertido_capitales_paises)

# Ejemplo con el diccionario de la imagen para verificar
ejemplo_imagen = {"Argentina": "Buenos Aires", "Chile": "Santiago"}
ejemplo_invertido_imagen = invertir_diccionario_paises_capitales(ejemplo_imagen)
print("\nEjemplo de la imagen (Capital: País):")
print(ejemplo_invertido_imagen)