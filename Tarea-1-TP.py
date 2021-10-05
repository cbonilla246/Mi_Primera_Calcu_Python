import os
def pedirNumeros():
    numeroA=int(input("Favor ingresar el valor de numeroA:"))
    numeroB=int(input("Favor ingresar el valor de numeroB:"))
    os.system("cls")
    return numeroA,numeroB
def suma(numeroA,numeroB):

    return numeroA+numeroB

def resta(numeroA,numeroB):

    return numeroA-numeroB

def multiplicacion(numeroA,numeroB):

    return numeroA*numeroB

def division(numeroA,numeroB):

    return numeroA/numeroB

def menu(numeroA,numeroB):
    while True:
        print(f"Que tipo de operacion matematica deseas realizar con {numeroA} y {numeroB}\n\
s para sumar\n\
r para restar\n\
m para multiplicar\n\
d para dividir\n\
x para salir:")
        opcion=input()
        if opcion=='s':
            print(f"Resultado es:{suma(numeroA,numeroB)}")
        if opcion=='r':
            print(f"Resultado es:{resta(numeroA,numeroB)}")
        if opcion=='m':
            print(f"Resultado es:{multiplicacion(numeroA,numeroB)}")
        if opcion=='d':
            print(f"Resultado es:{division(numeroA,numeroB)}")
        if opcion=='x':
            break
        input("Presione cualquier tecla")
        os.system("cls")
numeroA,numeroB=pedirNumeros()
menu(numeroA,numeroB)