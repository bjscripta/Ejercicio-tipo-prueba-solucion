#Añadimos funciones

from funcionerecursos import *

while True:
    print("-"*25)
    print("""1. Registrar un  trabajador
    2. Ver todos los trabajadores
    3. Imprimir planilla de sueldos
    4. Salir del programa""")
    print("-"*25)
    opc = input("Ingrese opcion: ")
    limpiar()
    if opc == "1":
        nombre = input("Ingrese nombre: ").title()
        apellido = input("Ingrese apellido: ").title()
        cargo = input("Ingrese cargo: ").upper()
        sueldo = float(input("Ingrese sueldo: "))
        guardarTrabajador(nombre,apellido,cargo,sueldo)

    elif opc=="2":
        print("Lista de trabajadores")
        listar_trabajadores(trabajadores)
    elif opc == "3":
        print("Imprimir planilla")
        imprimir_planilla(trabajadores)
    elif opc=="4":
        print("Saliendo del programa...")
        break
    else:
        print("Error, opcion no valida")