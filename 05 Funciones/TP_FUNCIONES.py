# 1. Crear una función llamada imprimir_hola_mundo que imprima por
# pantalla el mensaje: “Hola Mundo!”. Llamar a esta función desde el
# programa principal.

def imprimir_hola_mundo():
    """
    Esta función imprime el mensaje "Hola Mundo!" en la consola.
    """
    print("Hola Mundo!")

# --- Programa Principal ---
# Llamada a la función imprimir_hola_mundo
imprimir_hola_mundo()

# 2. Crear una función llamada saludar_usuario(nombre) que reciba
# como parámetro un nombre y devuelva un saludo personalizado.
# Por ejemplo, si se llama con saludar_usuario("Marcos"), deberá devolver: “Hola Marcos!”. Llamar a esta función desde el programa
# principal solicitando el nombre al usuario.
def saludar_usuario(nombre):
    """
    Esta función recibe un nombre y devuelve un saludo personalizado.
    
    :param nombre: str - El nombre del usuario.
    :return: str - Un saludo personalizado.
    """
    return f"Hola {nombre}!"
nombre_usuario = input("Por favor, introduce tu nombre: ")

# 3. Crear una función llamada informacion_personal(nombre, apellido,
# edad, residencia) que reciba cuatro parámetros e imprima: “Soy
# [nombre] [apellido], tengo [edad] años y vivo en [residencia]”. Pedir los datos al usuario y llamar a esta función con los valores ingresados.

def informacion_personal(nombre, apellido, edad, residencia):
    """
    Esta función imprime información personal del usuario.
    
    :param nombre: str - El nombre del usuario.
    :param apellido: str - El apellido del usuario.
    :param edad: int - La edad del usuario.
    :param residencia: str - La residencia del usuario.
    """
    print(f"Soy {nombre} {apellido}, tengo {edad} años y vivo en {residencia}.")
# Solicitar datos al usuario
nombre = input("Introduce tu nombre: ")
apellido = input("Introduce tu apellido: ")
edad = int(input("Introduce tu edad: "))
residencia = input("Introduce tu lugar de residencia: ")

# Llamar a la función con los datos ingresados
informacion_personal(nombre, apellido, edad, residencia)
# Llamar a la función saludar_usuario con el nombre ingresado
print(saludar_usuario(nombre_usuario))

#4. Crear dos funciones: calcular_area_circulo
# (radio) que reciba el radio como parámetro y devuelva el área del círculo.
# calcular_perimetro_circulo(radio) que reciba el radio como parámetro y devuelva el perímetro del círculo. 
# Solicitar el radio al usuario y llamar ambas funciones para mostrar los resultados.
import math
def calcular_area_circulo(radio):
    """
    Esta función calcula el área de un círculo dado su radio.
    
    :param radio: float - El radio del círculo.
    :return: float - El área del círculo.
    """
    return math.pi * (radio ** 2)

def calcular_perimetro_circulo(radio):
    """
    Esta función calcula el perímetro de un círculo dado su radio.

    :param radio: float - El radio del círculo.
    :return: float - El perímetro del círculo.
    """
    return 2 * math.pi * radio

# Solicitar el radio al usuario
radio_usuario = float(input("Introduce el radio del círculo: "))

# Llamar a ambas funciones y mostrar los resultados
print(f"Área del círculo: {calcular_area_circulo(radio_usuario)}")
print(f"Perímetro del círculo: {calcular_perimetro_circulo(radio_usuario)}")

# 5.Crear una función llamada segundos_a_horas(segundos) que reciba
# una cantidad de segundos como parámetro y devuelva la cantidad
# de horas correspondientes. Solicitar al usuario los segundos y mostrar el resultado usando esta función.

def segundos_a_horas(segundos):
    """
    Esta función convierte una cantidad de segundos a horas.
    
    :param segundos: int - La cantidad de segundos.
    :return: float - La cantidad de horas correspondientes.
    """
    return segundos / 3600

# Solicitar al usuario los segundos
segundos_usuario = int(input("Introduce la cantidad de segundos: "))

# Mostrar el resultado usando la función
print(f"Equivalente en horas: {segundos_a_horas(segundos_usuario)}")
# 6.Crear una función llamada tabla_multiplicar(numero) que reciba un
# número como parámetro y imprima la tabla de multiplicar de ese
# número del 1 al 10. Pedir al usuario el número y llamar a la función.
def tabla_multiplicar(numero):
    """
    Esta función imprime la tabla de multiplicar de un número del 1 al 10.
    
    :param numero: int - El número para el cual se desea imprimir la tabla de multiplicar.
    """
    for i in range(1, 11):
        print(f"{numero} x {i} = {numero * i}")

# Solicitar al usuario el número
numero_usuario = int(input("Introduce un número para ver su tabla de multiplicar: "))

# Llamar a la función con el número ingresado
tabla_multiplicar(numero_usuario)

# 7.Crear una función llamada operaciones_basicas(a, b) que reciba
# dos números como parámetros y devuelva una 
# tupla con el resultado de sumarlos, restarlos, multiplicarlos y dividirlos. Mostrar los resultados de forma clara.

def operaciones_basicas(a, b):
    """
    Esta función realiza operaciones básicas entre dos números.
    """
    suma = a + b
    resta = a - b
    multiplicacion = a * b
    division = a / b if b != 0 else None

    return (suma, resta, multiplicacion, division)

# 8.Crear una función llamada calcular_imc(peso, altura) que reciba el
# peso en kilogramos y la altura en metros, y devuelva el índice de
# masa corporal (IMC). Solicitar al usuario los datos y llamar a la función para mostrar el resultado con dos decimales.
def calcular_imc(peso, altura):
    """
    Esta función calcula el índice de masa corporal (IMC).
    """
    imc = peso / (altura ** 2) if altura > 0 else None
    return imc

# Solicitar al usuario los datos
peso_usuario = float(input("Introduce tu peso en kilogramos: "))
altura_usuario = float(input("Introduce tu altura en metros: "))

# Llamar a la función y mostrar el resultado
imc_usuario = calcular_imc(peso_usuario, altura_usuario)
if imc_usuario is not None:
    print(f"Tu IMC es: {imc_usuario:.2f}")
else:
    print("Altura no válida.")
#     9. Crear una función llamada celsius_a_fahrenheit(celsius) que reciba
# una temperatura en grados Celsius y devuelva su equivalente en
# Fahrenheit. Pedir al usuario la temperatura en Celsius y mostrar el
# resultado usando la función.
def celsius_a_fahrenheit(celsius):
    """
    Esta función convierte una temperatura de Celsius a Fahrenheit.
    
    :param celsius: float - La temperatura en grados Celsius.
    :return: float - La temperatura equivalente en grados Fahrenheit.
    """
    return (celsius * 9/5) + 32
# Solicitar al usuario la temperatura en Celsius
temperatura_celsius = float(input("Introduce la temperatura en grados Celsius: "))
# Mostrar el resultado usando la función
print(f"Equivalente en Fahrenheit: {celsius_a_fahrenheit(temperatura_celsius)}")

# 10.Crear una función llamada calcular_promedio(a, b, c) que reciba
# tres números como parámetros y devuelva el promedio de ellos.
# Solicitar los números al usuario y mostrar el resultado usando esta
# función.
def calcular_promedio(a, b, c):
    """
    Esta función calcula el promedio de tres números.
    
    :param a: float - Primer número.
    :param b: float - Segundo número.
    :param c: float - Tercer número.
    :return: float - El promedio de los tres números.
    """
    return (a + b + c) / 3
# Solicitar los números al usuario
numero1 = float(input("Introduce el primer número: "))
numero2 = float(input("Introduce el segundo número: "))
numero3 = float(input("Introduce el tercer número: "))

# Mostrar el resultado usando la función
print(f"El promedio es: {calcular_promedio(numero1, numero2, numero3)}")