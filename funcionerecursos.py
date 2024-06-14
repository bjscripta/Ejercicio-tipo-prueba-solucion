import msvcrt
import csv
import os

trabajadores = []

def limpiar():
    print("Presione una tecla para continuar...")
    msvcrt.getch()
    os.system("cls")

def validarNombre(nombre):
    for i in range(len(trabajadores)):
        if trabajadores[i][0] == nombre: 
            return i
    return -1

def guardarTrabajador(nombre, apellido, cargo, sueldo):
    if validarNombre(nombre) == -1: 
        if len(nombre) >= 3:  
            trabajadores.append([nombre, apellido, cargo, sueldo])
            print("*" * 20)
            print("Trabajador registrado!")
            print("*" * 20)
            reporteTrabajadores("registroTrabajadores.csv", trabajadores)
        else:
            print("Error, Nombre no válido")
    else:
        print("Error, Nombre repetido")

def mostrar():
    if len(trabajadores) > 0:  
        for i in range(len(trabajadores)):
            print(f"Trabajador: {trabajadores[i][0]} Cargo: {trabajadores[i][2]} Sueldo: {trabajadores[i][3]}")
    else:
        print("No hay trabajadores registrados")

def reporteTrabajadores(ruta, lista):
    with open(ruta, "w", newline="") as archivo:
        writer = csv.writer(archivo)
        writer.writerows(lista)

def cargos(cargo):
    if cargo in ["CEO", "ANALISTA DE DATOS", "DESARROLLADOR".upper()]:
        pass
    else:
        print("Error, no existe este cargo:", cargo)


