import csv

def cargar_empleados():
    empleados = []

    try:
        with open("empleados.csv", "r", encoding="utf-8") as archivo:
            lector = csv.DictReader(archivo)

            for fila in lector:
                empleados.append({ "legajo": fila["legajo"], "nombre": fila["nombre"],"dias_disponibles": int(fila["dias_disponibles"]),"estado": fila["estado"]})

    except FileNotFoundError:
        print("No se encontró el archivo empleados.csv")

    return empleados


def buscar_empleado(empleados, legajo):
    for empleado in empleados:
        if empleado["legajo"] == legajo:
            return empleado
    return None


def consultar_saldo(empleados):
    legajo = input("Ingrese su legajo: ")

    empleado = buscar_empleado(empleados, legajo)

    if empleado:
        print(f"\nEmpleado: {empleado['nombre']}")
        print(f"Días disponibles: {empleado['dias_disponibles']}\n")
    else:
        print("\nLegajo inexistente.\n")

def ver_estado(empleados):

    legajo = input("Ingrese su legajo: ")

    empleado = buscar_empleado(empleados, legajo)

    if empleado:
        print(f"\nEmpleado: {empleado['nombre']}")
        print(f"Estado actual: {empleado['estado']}\n")
    else:
        print("\nLegajo inexistente.\n")

def solicitar_vacaciones(empleados):
    legajo = input("Ingrese su legajo: ")

    empleado = buscar_empleado(empleados, legajo)

    if empleado is None:
        print("\nLegajo inexistente.\n")
        return

    print(f"\nBienvenido/a {empleado['nombre']}")
    print(f"Usted posee {empleado['dias_disponibles']} días disponibles.\n")

    try:
        dias = int(input("¿Cuántos días desea solicitar?: "))
    except ValueError:
        print("\nError. Debe ingresar un número válido.\n")
        return

    if dias <= 0:
        print("\nLa cantidad de días debe ser mayor que cero.\n")

    elif dias <= empleado["dias_disponibles"]:
        empleado["estado"] = "PENDIENTE DE APROBACIÓN"
        print("\nSolicitud registrada correctamente.")
        print("Solicitud enviada al supervisor.")
        print("Estado: PENDIENTE DE APROBACIÓN\n")

    else:
        print("\nSaldo insuficiente.")
        print("Solicitud rechazada.\n")


def menu():
    empleados = cargar_empleados()

    opcion = ""

    while opcion != "4":

        print("===================================")
        print(" SISTEMA DE GESTIÓN DE VACACIONES")
        print("===================================")
        print("1. Consultar saldo")
        print("2. Solicitar vacaciones")
        print("3. Ver estado de solicitud")
        print("4.Salir")

        opcion = input("\nSeleccione una opción: ")

        if opcion == "1":
            consultar_saldo(empleados)

        elif opcion == "2":
            solicitar_vacaciones(empleados)

        elif opcion == "3":
            ver_estado(empleados)
        
        elif opcion == "4":
            print("\nSesión finalizada correctamente.")

        else:
            print("\nOpción inválida.\n")


menu()