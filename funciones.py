contador_id = 0

def mostrar_menu():
    """
    Muestra el menu de opciones. 
    """

    print("""
    Sistema de Gestion de Clinica
    1. Cargar pacientes
    2. Mostrar todos los pacientes
    3. Buscar pacientes por numero de Historia Clinica
    4. Ordenar pacientes por numero de historia clinica
    5. Mostrar pacientes con mas dias de internacion
    6. Mostrar paciente con menos dias de internacion
    7. Cantidad de pacientes con mas de 5 dias de internacion
    8. Promedio de dias de internacion de todos los pacientes
    9. Salir      
    """)

def cargar_pacientes(lista: list):
    """
    Carga un paciente en la lista.
    - Recibe por parametro:
        - lista (list): Lista de pacientes.

    Retorna un mensaje una vez que se cargaron los pacientes de forma exitosa.
    """
    global contador_id
    # contador_id += 1
    # paciente_id = contador_id

    cant = int(input("¿Cuantos pacientes desea ingresar?: "))
    print("-" * 50)

    for _ in range(cant):
        contador_id += 1
        paciente_id = contador_id
        # paciente_id = contador_id
        nombre = str(input("Ingrese el nombre del paciente: ")).capitalize()
        edad = int(input("Ingrese la edad del paciente "))
        diagnostico = str(input("Ingrese el diagnostico del paciente: ")).capitalize()
        cant_dias_internado = int(input("Ingrese la cantidad de dias que estuvo internado: "))
        print("-" * 50)

        lista.append([paciente_id, nombre, edad, diagnostico, cant_dias_internado])
    
    print("Pacientes cargados exitosamente.")

def mostrar_pacientes(lista: list):
    """
    Muestra a todos los pacientes.

    - Recibe por parametro:
        - Lista (list): La lista de pacientes
    """
    print("--- Mostrando lista de pacientes ---")

    for paciente in lista:
        print(f"ID: {paciente[0]}, Nombre: {paciente[1]}, Edad: {paciente[2]}, Diagnostico: {paciente[3]}, Dias internado: {paciente[4]}.")

    return lista

def buscar_pacientes(lista: list, numero: int):
    """
    Busca a los pacientes de la lista en base al numero ingresado.

    - Recibe por parametro:
        - Lista (list): La lista de pacientes.
        - Numero (int): Numero del paciente a buscar.

    Retorna los datos del paciente si fue encontrado y otro mensaje si no fue encontrado-
    """
    paciente_encontrado = False

    for i in range(len(lista)):
        if lista[i][0] == numero:
            print(f"El paciente {lista[i][1]} fue encontrado")
            paciente_encontrado = True

            print(f"ID: {lista[i][0]}, Nombre: {lista[i][1]}, Edad: {lista[i][2]}, Diagnostico: {lista[i][3]}, Dias internado: {lista[i][4]}.")

        # return lista

    if paciente_encontrado == False:
        print("Paciente no encontrado.")

def ordenar_pacientes(lista: list):
    """
    Ordena a los pacientes de forma ascendente.

    - Recibe por parametro:
        - Lista (list): La lista de pacientes

    Retorna la lista con los pacientes ordenas de forma ascendente.
    """
    for i in range(len(lista)): #recorremos el lista
        for j in range(len(lista) - i - 1):
            if lista[j][0] > lista[j + 1][0]:
                auxiliar = lista[j]
                lista[j] = lista[j + 1]
                lista[j + 1] = auxiliar

    print(f"El lista de pacientes se ordeno de manera exitosa de forma ascendente.")

    for paciente in lista:
        print(f"ID: {paciente[0]}, Nombre: {paciente[1]}, Edad: {paciente[2]}, Diagnostico: {paciente[3]}, Dias internado: {paciente[4]}.")

    return lista

def paciente_mayor_tiempo_internado(lista: list):
    """
    Muestra al paciente con mayor tiempo estando internado.

    - Recibe por parametro:
        - Lista (list): La lista de pacientes

    Retorna los datos del paciente con mayor tiempo internado.
    """
    paciente_mayor_dias_internado = lista[0]

    for paciente in lista:
        if paciente[4] > paciente_mayor_dias_internado[4]:
            paciente_mayor_dias_internado = paciente

    print(f"El paciente con mas dias internado es: {paciente_mayor_dias_internado[1]}")
    print(f"ID: {paciente_mayor_dias_internado[0]}, Nombre: {paciente_mayor_dias_internado[1]}, Edad: {paciente_mayor_dias_internado[2]}, Diagnostico: {paciente_mayor_dias_internado[3]}, Dias internado: {paciente_mayor_dias_internado[4]}.")

def paciente_menor_tiempo_internado(lista: list):
    """
    Muestra al paciente con menor tiempo estando internado.

    - Recibe por parametro:
        - Lista (list): La lista de pacientes

    Retorna los datos del paciente con menor tiempo internado.
    """
    paciente_menor_dias_internado = lista[0]

    for paciente in lista:
        if paciente[4] < paciente_menor_dias_internado[4]:
            paciente_menor_dias_internado = paciente

    print(f"El paciente con menos dias internado es: {paciente_menor_dias_internado[1]}")
    print(f"ID: {paciente_menor_dias_internado[0]}, Nombre: {paciente_menor_dias_internado[1]}, Edad: {paciente_menor_dias_internado[2]}, Diagnostico: {paciente_menor_dias_internado[3]}, Dias internado: {paciente_menor_dias_internado[4]}.")

def cantidad_pacientes_mas_5_dias(lista: list):
    """
    Muestra los pacientes con mas de 5 dias internados.

    - Recibe por parametro:
        - Lista (list): La lista de pacientes

    Retorna los datos de los pacientes con mas de 5 dias internados.
    """
    print("Los pacientes con mas de 5 dias internados son: ")

    for paciente in lista:
        if paciente[4] > 5:
            print(f"ID: {paciente[0]}, Nombre: {paciente[1]}, Edad: {paciente[2]}, Diagnostico: {paciente[3]}, Dias internado: {paciente[4]}")

def calcular_promedio_pacientes_dias_internacion(lista: list):
    """
    Calcula el promedio de los pacientes.

    - Recibe por parametro:
        - Lista (list): La lista de pacientes

    Retorna el promedio de los dias de internacion de todos los pacientes ingreados.
    """
    total_dias_internados = 0

    for paciente in lista:
        total_dias_internados += paciente[4]

    promedio = total_dias_internados // len(lista)

    return promedio
