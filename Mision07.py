# Autor: Erick David Ramírez Martínez, A01748155, Grupo: 02
# Programa que hace diversas cosas, una forma básica de dividir restando números
# encontrar el mayor de un número y un menú para que el usario
# use indefinidamente estas 2 funciones


def dividir(dividendo,divisor):
    residuo = dividendo
    divisiones = 0
    while residuo >= divisor:
        residuo -= divisor
        divisiones+=1

    print("%d / %d = %d, sobra %d" % (dividendo, divisor, divisiones, residuo))


def encontrarMayor():
    print("Teclea una serie de números para encontrar el mayor")
    numero = int(input("Ingresa un número [Ingresa -1 para salir]: "))
    if numero == -1:
        print("No hay valor mayor")
    else:
        mayor = numero
        while numero != -1:
            numero = int(input("Ingresa un número [Ingresa -1 para salir]: "))
            if numero > mayor:
                mayor = numero
        print("El mayor es:", mayor)




def main():
    opcion = 1
    while opcion != 3:
        print("Misión 07. Ciclos While")
        print("Autor: Erick David Ramírez Martínez")
        print("Matrícula: A01748155")
        print("1. Calcular divisiones")
        print("2. Encontrar el mayor de varios números")
        print("3. Salir")

        opcion =  int(input("Teclea el número de la opción de lo que deseas hacer: "))

        if opcion == 1:
            print("")
            print("Calcular divisiones")
            dividendo = int(input("Ingresa el dividendo: "))
            divisor = int(input("Ingresa el divisor: "))
            dividir(dividendo,divisor)
            print("")
        elif opcion == 2:
            print("")
            encontrarMayor()
            print("")
        elif opcion == 3:
            print("")
            print("Gracias por usar este programa, regresa pronto")
        else:
            print("ERROR, teclea 1, 2 o 3")
            print("")


main()