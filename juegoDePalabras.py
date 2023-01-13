import random
import time
import platform
import os


def borrar(): #funcion para borar pantalla
    so=platform.system()
    windows="Windows"
    linux="Linux"
    if so == windows:
        os.system("cls")
    else: 
        os.system("clear")

print("Bienvenido a esta prueba de conocimiento, sigue las instrucciones y trata de adivinar el texto mezclado")
time.sleep(2) #Tiempo de espera a modo de efecto
usuario1 = input("Por favor escribe algo: ")
mezcla = usuario1.split() #separando el texto ingresado por el usuario
borrar()
print("Cargando información...")
time.sleep(4)
random.shuffle(mezcla) #Barajeando el texto ingresado por el usuario
print()
uniendoUsuario1 = " ".join(mezcla).upper() #pasando de minusculas a mayusculas

 #Presentando el texto del usuario para que pueda adivinar
print(f"Por favor trata de adivinar el texto que se encuentra mezclado \" {uniendoUsuario1} \" ")
intentos = 0

while True:
    usuario2 = input("Adivina el texto y escribe algo aqui: ")
    print()
    print(usuario2)
    print()
    intentos += 1
 #Utilizando las condicionales
    if usuario1.lower() == usuario2.lower():
        print(f"Haz acertado en {intentos} intentos")
        break
    else:
        print(f"Haz errado en {intentos} intentos")
    print()