#Añadimos funciones

from funcionerecursos import *

while True:
    limpiar()
    print("-"*25)
    print("""1. Registrar un  trabajador
    2. Ver todos los trabajadores
    3. Imprimir planilla de sueldos
    4. Salir del programa""")
    print("-"*25)
    opc = input("Ingrese opcion: ")
    limpiar()
    if opc=="1":
        nombre = input("Ingrese nombre: ").title()
        validarNombre(nombre)
        apellido = input("Ingrese apeliido: ").title()
        cargo = input("Ingrese cargo: ").upper()
        cargos(cargo)
        sueldo = input("Ingrese sueldo: ")
        guardarTrabajador(nombre,apellido,cargo,sueldo)
    elif opc=="2":
        print("Lista de trabajadores")
        mostrar()
    elif opc == "3":
        print("Imprimir planilla")
        cargo = input("Ingrese el cargo a filtrar: ")
        if cargos(cargo):
            trabajadores_filtrados = [t for t in trabajadores if t[2] == cargo]
            if trabajadores_filtrados:
                reporteTrabajadores("planilla_sueldos.txt", trabajadores_filtrados)
                print(f"Imprimiendo planilla con el cargo:{cargo} generada en planilla_sueldos.txt")
        else:
            print("Error, cargo no valido.")
        limpiar()
    elif opc=="4":
        print("Saliendo del programa...")
        break
    else:
        print("Error, opcion no valida")