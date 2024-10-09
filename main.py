from funciones import *

pacientes = [
    [12, "Axel", 20, "Fiebre", 7],
    [3, "Leo", 15, "Alergias", 10],
    [8, "Ariel", 25, "Nauseas", 9],
    [2, "juan", 10, "vomitos", 4],
]

run = True

while run:

    mostrar_menu()
    opcion = input("Elija una opcion: ")

    match opcion:

        case "1":
            cargar_pacientes(pacientes)
        case "2":
            if not pacientes:
                print("Aun no hay pacientes para mostrar")
            else:
                mostrar_pacientes(pacientes)
            
        case "3":
            if not pacientes:
                print("Aun no hay pacientes para buscar.")
            else:
                num_historia_clinica = input("Ingrese el numero de Historia clinica del paciente a buscar: ")
                num_historia_clinica = int(num_historia_clinica)
                buscar_pacientes(pacientes, num_historia_clinica)
        case "4":
            if not pacientes:
                print("Aun no hay pacientes para ordenar.")
            else:
                ordenar_pacientes(pacientes)
        case "5":
            if not pacientes:
                print("Aun no hay pacientes para mostrar.")
            else:
                paciente_mayor_tiempo_internado(pacientes)
        case "6":
            if not pacientes:
                print("Aun no hay pacientes para mostrar.")
            else:
                paciente_menor_tiempo_internado(pacientes)
        case "7":
            if not pacientes:
                print("Aun no hay pacientes para mostrar.")
            else:
                cantidad_pacientes_mas_5_dias(pacientes)
        case "8":
            if not pacientes:
                print("Aun no hay pacientes para calcular su promedio.")
            else:
                promedio = calcular_promedio_pacientes_dias_internacion(pacientes)
                print(f"El promedio de dias internados de todos los pacientes es de: {promedio} dias")
        case "9":
            print("... Saliendo ...")
            break
        case _:
            print("Error. Opcion invalida")       