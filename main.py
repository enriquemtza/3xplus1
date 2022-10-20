# Secuencia 4, 2, 1 para cualquier numero natural

from os import system

def main():
    while True:
        system("clear")
        opcion = input("""Programa para realizar la secuencia 3x + 1

        Introduzca la opcion a realizar:

        1. Introducir un numero para obtener su secuencia
        0. salir
        
Opcion a seleccionar: """)
        
        if opcion == "0":
            break
        elif opcion == "1":
            lista = []

            system("clear")
            n = int(input("Introduzca un numero: "))

            lista.append(n)

            while True:
                if n == 1:
                    break
                else:
                    if n % 2 == 0:
                        n = n / 2
                        lista.append(n)
                    elif n % 2 != 0:
                        n = (3 * n) + 1
                        lista.append(n)

            system("clear")
            print("Los numeros de la secuencia 3x + 1 del numero", lista[0], "son:\n")
            for c in lista:
                print(int(c))

            input("\nPresione enter para continuar...")

main()
