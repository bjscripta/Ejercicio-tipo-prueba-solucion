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

def reporteTrabajadores(ruta, lista):
    with open(ruta, "w", newline="") as archivo:
        writer = csv.writer(archivo)
        writer.writerows(lista)

def listar_trabajadores(trabajadores):
    if trabajadores:
        print("Lista de todos los trabajadores:")
        for trabajador in trabajadores:
            nombre, apellido, cargo, sueldo = trabajador
            desc_salud = round(sueldo * 0.07, 2)
            desc_afp = round(sueldo * 0.12, 2)
            liquido_pagar = round(sueldo - desc_salud - desc_afp, 2)
            print(f"Trabajador:{nombre} {apellido}:  Cargo:{cargo}  Sueldo Bruto:{sueldo}:  Desc.Salud:{desc_salud}  Desc.AFP:{desc_afp}  Sueldo Liquido:{liquido_pagar}")
    else:
        print("No hay trabajadores registrados.")


cargos_disponibles = ["CEO", "Desarrollador", "Analista de datos"]

def imprimir_planilla(trabajadores):
    print("Imprimir planilla de sueldos")
    print("1. Imprimir todos los trabajadores")
    print("2. Imprimir por cargo específico")
    opcion = input("Seleccione una opción: ")

    if opcion == "1":
        print("Planilla de sueldos de todos los trabajadores:")
        for trabajador in trabajadores:
            print(f"Trabajador: {trabajador[0]}, Cargo: {trabajador[1]}, Sueldo: {trabajador[2]}")
    elif opcion == "2":
        print("Cargos disponibles:")
        for cargo in cargos_disponibles:
            print(cargo)
        cargo_seleccionado = input("Seleccione un cargo por su nombre: ")
        print(f"Planilla de sueldos para el cargo {cargo_seleccionado}:")
        for trabajador in trabajadores:
            if trabajador[1] == cargo_seleccionado:
                print(f"Trabajador: {trabajador[0]}, Sueldo: {trabajador[2]}")
    else:
        print("Opción no válida.")




