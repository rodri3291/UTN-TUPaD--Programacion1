#Ejercicio 1
print ("Hola Mundo!")


#Ejercicio 2
nombre = input("Por favor ingrese su nombre: ")
print (f"Hola {nombre}!")


#Ejercicio 3
nombre = input("Nombre: ")
apellido = input("Apellido: ")
edad = input("Edad: ")
residencia = input("Residencia: ")
print (f"Soy {nombre} {apellido}" f" Tengo {edad} años" f" y soy de {residencia}")


#Ejercicio 4
import math
radio_circulo = float(input("Por favor ingrese el radio del circulo: "))
area_circulo = math.pi * (radio_circulo)**2
perimetro_circulo = 2 * math.pi * radio_circulo
print(f"El área del círculo es de {area_circulo} y el perímetro es de {perimetro_circulo}.")


#Ejercicio 5
cantidad_segundos = float(input("Por favor, ingrese la cantidad de segundos a convertir: "))
cantidad_horas = round(cantidad_segundos / 3600, 2)
print(f"El equivalente a {cantidad_segundos} segundos son {cantidad_horas} horas.")


#Ejercicio 6
numero = int(input("Introduzca un número"))
for i in range (0,11):
    resultado = i * numero
    print(numero, "X" ,i, " =",resultado)


#Ejercicio 7
print("Ingrese el primer número: ")
n1 = float (input())
print("Ingrese el segundo número: ")
n2 = float (input())
suma = n1 + n2
resta = n1 - n2
multiplicación = n1 * n2
division = n1 / n2
print ("La suma es: ", suma)
print ("La resta es: ", resta)
print ("La mulplificación es: ", multiplicación)
print ("La division es: ", division)


#Ejercicio 8
def calcularIMC (p,a):
    return p / (a*a)
def nivelDePeso(IMC):
    if IMC < 18.5:
        return "Bajo peso"
    elif 18.5 <= IMC <= 24.9:
        return "Normal"
    elif 25 <= IMC <= 29.9:
        return "Sobrepeso"
    elif 30 <= IMC <= 34.9:
        return "Obesidad I"
    elif 35 <= IMC <= 39.9:
        return "Obesidad II"
    elif 40 <= IMC <= 49.9:
        return "Obesidad III"
    elif IMC >= 50:
        return "Obesidad IV"
peso = float (input("Ingrese el peso (Kg): "))
altura = float (input ("Ingrese la altura (m): "))
print ("Su nivel de peso es:" ,nivelDePeso(calcularIMC(peso, altura))) 


#Ejercicio 9
def convertir(c):
    return(c * 9/5) + 32
n = float(input("Ingresa los grados celsius:" ))
print(f"La conversión a grados fahrenheit es: {convertir(n)}") 


#Ejercicio 10
a = float(input("Ingresa la nota 1: "))
b = float (input("Ingresa la nota 2: "))
c = float (input("Ingresa la nota 3: ")) 
promedio = (a+b+c)/3
print ("El promedio de las 3 notas es: ", round(promedio))     