import re
import os
import csv
import json

def leer_csv(ruta:str) -> list:
    """recibe la ruta de un archivo csv y lo lee, retornando una lista con un diccionario dentro con el contenido separado por comas

    Args:
        ruta (str): ruta del archivo a leer

    Returns:
        list: lista del archivo leido
    """
    with open(ruta, "r", encoding="utf-8") as archivo:
        lista_elementos = []
        lector_csv = csv.reader(archivo) 
        next(lector_csv) # Saltear el encabezado del archivo CSV 
        for linea in lector_csv:
            caracteristicas = linea[4].split("~")
            precio = linea[3].replace("$", "")
            elemento = {"ID": linea[0], "NOMBRE": linea[1],"MARCA": linea[2], "PRECIO": precio, "CARACTERISTICAS": caracteristicas}
            lista_elementos.append(elemento)
        return lista_elementos
     
def leer_csv_marcas(ruta):
    """recibe una ruta a un archivo, lo abre y devuelve una lista con las marcas separadas por el "\n"

    Args:
        ruta (_type_): ruta para leer marcas

    Returns:
        _type_: la lista con las marcas leidas
    """
    lista_retorno = []
    with open(ruta, "r") as archivo:
        for marca in archivo:
            marca = marca.replace("\n", "").capitalize()
            lista_retorno.append(marca)
    return lista_retorno     
            
def ingresar_str() -> str:
    str = input("Ingresa las caracteristicas a buscar: ")
    return str

def mostrar_marcas(ruta):
    """muestra las marcas que hay en el archivo de la ruta que se pasa por parametro

    Args:
        ruta (_type_): ruta para leer las marcas
    """
    marcas = leer_csv_marcas(ruta)
    for marca in marcas:
        imprimir_dato(marca)

def mostrar_lista(lista:list, titulo:str):
    """muestra una lista

    Args:
        lista (list): lista a mostrar
        titulo (string): titulo
    """
    print(f"--- {titulo} ---")
    for item in lista:
        print(item)
    
def mostrar_item(lista:list, item:str) -> None:
    """recorre una lista y muestra el dato que pidas

    Args:
        lista (list): lista a recorrer
        item (str): dato a mostrar
    """
    for elemento in lista:
        print(f"{elemento[item]}")

def mostrar_diccionario(diccionario:dict) -> None:
    """recibe un diccionario, lo recorre e imprime cada una de sus keys

    Args:
        diccionario (dict): diccionario para mostrar sus keys
    """
    if not diccionario:
        print("No hay nada para mostrar.")
    else:
        for key in diccionario:
            print("ID del producuto:", key["ID"])
            print("Nombre del producto:", key["NOMBRE"])
            print("Marca del producto:", key["MARCA"])
            print("Precio del producto: $",key["PRECIO"])
            for key in key["CARACTERISTICAS"]:
                print("Caracteristicas del producto:", key)
            print("")

def imprimir_dato(dato:str) -> None:
    """imprime un str

    Args:
        dato (str): str a imprimir
    """
    print(dato)

def imprimir_menu() -> None:
    """muestra un menu
    """
    imprimir_dato("°----------------------- Menú de opciones -----------------------°")
    imprimir_dato("| Opcion 1: Cargar datos                                         |")
    imprimir_dato("| Opcion 2: Listar cantidad por marca                            |")
    imprimir_dato("| Opcion 3: Listar insumos por marca                             |")
    imprimir_dato("| Opcion 4: Buscar insumo por caracteristica                     |")
    imprimir_dato("| Opcion 5: Listar insumos ordenados por marcas (A-Z)            |")
    imprimir_dato("| Opcion 6: Realizar compras                                     |")
    imprimir_dato("| Opcion 7: Guardar en formato JSON                              |")
    imprimir_dato("| Opcion 8: Leer desde formato JSON                              |")
    imprimir_dato("| Opcion 9: Actualizar precios                                   |")
    imprimir_dato("| Opcion 10: Agregar producto                                    |")
    imprimir_dato("| Opcion 11: Guardar en archivo                                  |")
    imprimir_dato("| Opcion 12: Salir del programa                                  |")
    imprimir_dato("°----------------------------------------------------------------°")
    
def validar_entero(dato:str) -> bool:
    if re.match("^\d+$", dato):
        return True
    else:
        return False 

def validar_numero(dato: str) -> bool:
    """analiza un string y si es solo de numeros retorna True

    Args:
        dato (str): string para comprobar si es numerico

    Returns:
        bool: True es correcto, False no
    """
    if re.match("^\d+$", dato) or re.match("^\d+\.\d+$", dato):
        return True
    else:
        return False

def menu_principal():
    imprimir_menu()
    opcion = input("Ingrese una opcion: ")
    if validar_entero(opcion):
        opcion = int(opcion)
        if opcion < 1 or opcion > 12:
            print("ERROR. Opcion no valida")
        else:
            return opcion
    else:
        imprimir_dato("ERROR. Eso no es un numero.")
        return -1  

def insumos_menu_principal():
    bandera_1 = False
    while True:
        opcion = menu_principal()
        match(opcion):
            case 1:
                lista_insumos = leer_csv("C:\\Users\\lauta\\Desktop\\parcial_Labo\\insumos.csv")
                bandera_1 = True
            case 2:
                if bandera_1:
                    mostrar_cant_por_marca(listar_cant_por_marca(lista_insumos))
                else:
                    imprimir_dato("ERROR. Primero debes ingresar a la opcion 1.")
            case 3:
                if bandera_1:
                    mostrar_insumos_por_marca(listar_insumos_por_marca(lista_insumos))
                else:
                    imprimir_dato("ERROR. Primero debes ingresar a la opcion 1.")
            case 4:
                if bandera_1:
                    caracteristica = ingresar_str()
                    mostrar_diccionario(buscar_por_caracterisitica(lista_insumos, caracteristica))
                else:
                    imprimir_dato("ERROR. Primero debes ingresar a la opcion 1.")
            case 5:
                if bandera_1:
                    listar_insumos_ordenados(lista_insumos)                
                else:
                    imprimir_dato("ERROR. Primero debes ingresar a la opcion 1.")
            case 6:
                if bandera_1:
                    realizar_compras(lista_insumos)
                else:
                    imprimir_dato("ERROR. Primero debes ingresar a la opcion 1.")
            case 7:
                if bandera_1:
                    guardar_en_json_alimento(lista_insumos)            
                else:
                    imprimir_dato("ERROR. Primero debes ingresar a la opcion 1.")
            case 8:
                if bandera_1:
                    leer_json("productos_alimento.json")                
                else:
                    imprimir_dato("ERROR. Primero debes ingresar a la opcion 1.")
            case 9:
                if bandera_1:
                    actualizar_precios("insumos_copy.csv")
                else:
                    imprimir_dato("ERROR. Primero debes ingresar a la opcion 1.")
            case 10:
                if bandera_1:
                    nuevos_prod = agregar_nuevo_producto()
                else:
                    ("ERROR. Primero debes ingresar a la opcion 1.")
            case 11:
                if bandera_1:
                    formato = input("Ingrese el formato que quieres guardar: 'csc' o 'json'")
                    nombre_archivo = input("Ingrese el nombre que le quieres dar al archivo.")
                    guardar_datos_actualizados(formato,nombre_archivo, lista_insumos)
                else:
                    ("ERROR. Primero debes ingresar a la opcion 1.")
            case 12:
                respuesta = input("Seguro que quieres salir? (s/n): ")
                if respuesta == "s":
                    break
                else:
                    continue
        os.system("pause")      
        os.system("cls")

def listar_cant_por_marca(lista:list) -> dict:
    """cuenta la cantidad de insumos que hay de cada marca

    Args:
        lista (list): lista a contar marcas

    Returns:
        dict: un diccionario con la marca y la cantidad
    """
    contador_marcas = {}
    for elemento in lista:
        marca = elemento["MARCA"]
        if marca in contador_marcas:
            contador_marcas[marca] += 1
        else:
            contador_marcas[marca] = 1
        
    return contador_marcas

def mostrar_cant_por_marca(diccionario:dict) -> None:
    """recibe un diccionario con marcas y cantidad e imprime cada dato

    Args:
        diccionario (dict): diccionario a imprimir
    """
    for marca, cantidad in diccionario.items():
        imprimir_dato(f"De la marca {marca} hay {cantidad} insumos.") 

def listar_insumos_por_marca(lista:list) -> dict:
    """guarda en un diccionario la marca, nombre y precio de los insumos de la lista pasados por parametro

    Args:
        lista (list): lista para guardar 

    Returns:
        dict: retorna un diccionario con marca, nombre y precio
    """
    dict_marcas = {}
    for elemento in lista:
        id_insumo = elemento["ID"]
        nombre = elemento["NOMBRE"]
        marca = elemento["MARCA"].capitalize()
        precio = elemento["PRECIO"]
        caracteristicas = elemento["CARACTERISTICAS"]
        insumo = {
            "ID": id_insumo,
            "NOMBRE": nombre,
            "PRECIO": precio,
            "CARACTERISTICAS": caracteristicas
        }
        if marca in dict_marcas:
            dict_marcas[marca].append(insumo)
        else:
            dict_marcas[marca] = [insumo]
    return dict_marcas

def mostrar_insumos_por_marca(diccionario:dict) -> None:
    """muestra el nombre y precio de cada insumo por marca

    Args:
        diccionario (dict): diccionario para mostrar
    """
    for marca, insumos in diccionario.items():
        print(f"Marca: {marca}")
        for elemento in insumos:
            nombre = elemento["NOMBRE"]
            precio = elemento["PRECIO"]
            print(f"--> Insumo: {nombre} | Precio: ${precio}")
        print("")

def buscar_por_caracterisitica(lista:list, caracteristica:str) -> None:
    """recibe una lista para buscar y una caracteristica la cual va a buscar en esa lista

    Args:
        lista (list): lista en la cual buscar
        caracteristica (str): caracteristica a buscar

    Returns:
        _type_: 0 si no se encontró nada, o una lista con los insumos encontrados con esas caracteristicas
    """
    insumos_encontrados = []
    caracteristica = caracteristica.strip().lower()
    encontro = False
    for elemento in lista:
        caracteristicas = elemento["CARACTERISTICAS"]
        for palabra in caracteristicas:
            if caracteristica in palabra.lower():
                encontro = True
                insumos_encontrados.append(elemento)
    if not encontro:
        return 0
    return insumos_encontrados

def listar_insumos_ordenados(lista) -> None:
    tam = len(lista)
    for i in range(tam - 1):
        for j in range(i + 1, tam):
            if (lista[i]["MARCA"] == lista[j]["MARCA"] and lista[i]["PRECIO"] < lista[j]["PRECIO"]) or (lista[i]["MARCA"] > lista[j]["MARCA"]):
                    aux = lista[i]
                    lista[i] = lista[j]
                    lista[j] = aux
    for item in lista:
        print('ID: ',item["ID"])
        print('Nombre: ',item["NOMBRE"])
        print('Precio: $',item["PRECIO"])
        print('Marca: ',item["MARCA"])
        print('Primer caracteristica: ',item["CARACTERISTICAS"][0])
        print("")

def mostrar_insumos_por_marca_elegida(diccionario:dict, marca_ingresada:str) -> None:
    """muestra el nombre y precio de cada insumo por marca

    Args:
        diccionario (dict): diccionario para mostrar
    """
    hay_insumo = False
    marca_ingresada = marca_ingresada.strip()
    if not diccionario:
        print("N/A")
    else:
        for marca, insumos in diccionario.items():
            if marca_ingresada == marca:
                hay_insumo = True
                print(f"Marca: {marca}")
                for elemento in insumos:
                    id = elemento[0]
                    nombre = elemento[1]
                    precio = elemento[2]
                    print(f"--> ID: {id:<2} | Insumo: {nombre:<20} | Precio: ${precio:<6}")
                print("")
        if not hay_insumo:
            print("No hay ningun insumo de la marca: ",marca_ingresada)

def realizar_compras(lista:list) -> None:
    """pide al usuario que ingrese una marca, el insumo que quiere comprar y la cantidad hasta que el usuario decida dejar de comprar. Luego se muestra el total de la compra y se genera un archivo txt con los datos de la misma.

    Args:
        lista (list): lista sobre la cual se va a comprar
    """
    compra_realizada = []     #lista para almacenar los insumos comprados
    insumos_por_marcas = listar_insumos_por_marca(lista)
    
    while True:
        marca_ingresada = input("Ingresa la marca de los insumos que quieres comprar (en caso de salir ingresa 'finalizar'): ").capitalize()
        if marca_ingresada.lower() == "finalizar": 
            break  # si el usuario ingresa finalizar se romple el bucle while
        if marca_ingresada in insumos_por_marcas: #si la marca coincide con alguna de las marcas de los isumos entra al if
            imprimir_dato(f"Productos disponibles de la marca {marca_ingresada}:")
            insumos = insumos_por_marcas[marca_ingresada] 
            for elemento in insumos: #recorro cada insumo de la marca elegida por el usuario
                id_producto = elemento["ID"]
                nombre = elemento["NOMBRE"]
                precio = elemento["PRECIO"]
                imprimir_dato(f"ID: {id_producto:<2} | Producto: {nombre:<20} | Precio: ${precio:<6}")
                
            id_compra = input("Ingresa el ID del producto que quieres comprar: ")
            if validar_entero(id_compra):
                id_compra = int(id_compra)
                id_encontrado = False #bandera para el caso que el id no coincida con el de los insumos de X marca
                for elemento in insumos: #recorro cada elemento de X marca
                    id_producto = int(elemento["ID"])
                    if id_compra == id_producto: #si el id coincide
                        id_encontrado = True #la bandera cambia a verdadera
                        cantidad_compra = input("Por ultimo, ingrese la cantidad que quiere comprar: ") #pide la cantidad para comprar
                        if validar_entero(cantidad_compra):
                            cantidad_compra = int(cantidad_compra) #se castea
                            precio = float(elemento["PRECIO"])
                            subtotal = precio * cantidad_compra #en subtotal se guarda el monto de la ultima compra que realizó
                            compra_realizada.append({"Producto": elemento["NOMBRE"], "Cantidad": cantidad_compra, "Subtotal": subtotal}) #se agregan a la lista los insumos comprados en un diccionario con respectivas keys
                            imprimir_dato("Compra realizada.")
                        else:
                            imprimir_dato("La cantidad ingresada no es correcta.")
                if not id_encontrado:
                    imprimir_dato("El ID ingresado no pertenece a ningun insumo")
            else:
                imprimir_dato("El ID ingresado no es correcto.")
        else:
            imprimir_dato(f"No se encontró la marca {marca_ingresada}")
            
    monto_total = 0
    for item in compra_realizada: #se recorre cada insumo en la lista de compras
        monto_total += item["Subtotal"] #se suman todos los subtotales y se asignan a la compra total
        
    # generar_factura(compra_realizada, monto_total) #se genera el archivo txt
    
    with open("factura.txt", "w") as archivo: #abre el archivo en modo escritura y escribe los datos de la compra
        archivo.write("FACTURA DE COMPRA\n\n")
        archivo.write(f"Producto{' ' * 20}Cantidad  Subtotal\n") # uso ese formato para dejar 20 espacios y que quedé prolija la impresion
        archivo.write("---------------------------------------------\n")
        for item in compra_realizada:
            archivo.write(f"{item['Producto']:<24}      {item['Cantidad']:<3}      {item['Subtotal']:<8}\n") # aca tambien busco que quede prolijo
        archivo.write("---------------------------------------------\n")
        archivo.write(f"Total de la compra:      ${monto_total}")
    
    
    imprimir_dato(f"Total de la compra: ${monto_total}") #se muestra el total

def guardar_en_json_alimento(lista:list) -> None:
    """recibe una lista la cual de la cual va a recorrer sus elementos y si en su nombre contienen la palabra "alimento" se los agrega a una nueva lista, la cual al finalizar será abierta en un archivo .json

    Args:
        lista (list): lista donde se busca la palabra "alimento"
    """
    productos_coincidentes = []
    for producto in lista:
        nombre = producto["NOMBRE"]
        if "alimento" in nombre.lower():
            productos_coincidentes.append(producto)
            
    with open("productos_alimento.json", "w", encoding="utf-8") as archivo: #uso el encoding para las palabras que estan acentuadas
        json.dump(productos_coincidentes, archivo, ensure_ascii=False) 

def leer_json(ruta:str) -> None:
    with open(ruta, "r", encoding="utf-8") as archivo:
        data = json.load(archivo)
        for insumo in data:
            imprimir_dato(insumo)

def actualizar_precios(ruta: str) -> None:
    datos = []
    with open(ruta, 'r', encoding='utf-8') as archivo: # lee los datos del archivo CSV
        lector = csv.reader(archivo)
        cabecera = next(lector)  #lee la cabecera
        for fila in lector:
            datos.append(fila)  # agregar cada fila a la lista de datos

    
    datos_actualizados = list(map(lambda fila: [fila[0], fila[1], fila[2], "$" + str(round(float(fila[3].replace("$", "")) * 1.084, 2)), fila[4]], datos)) 
    # datos_actualizados = list(map(lambda fila: [fila[0], fila[1], fila[2], str(round(float(fila[3].replace("$", "")) * 1.084, 2)), fila[4]], datos)) #aplica el aumento del 8.4% a los precios utilizando map

    
    with open(ruta, 'w', encoding='utf-8', newline='') as archivo_salida: #escribe los datos actualizados en el archivo ruta pasado por parametro
        escritor = csv.writer(archivo_salida)
        escritor.writerow(cabecera)  #escribe la cabecera
        escritor.writerows(datos_actualizados)  #escribe los datos actualizados

    print(f"Precios actualizados y guardados en el archivo {ruta}.")

def agregar_nuevo_producto():
    """permite al usuario agregar un nuevo producto, le solicita el ID, la marca, el nombre, el precio y las caracteristicas, pudiendo ingresar de estas un maximo de 3

    Returns:
        list: retorna una lista con los productos nuevos
    """
    while True:
        id_nuevo = input("Ingrese un ID para el producto nuevo: ")
        if validar_entero(id_nuevo):
            id_existe = False
            id_nuevo = int(id_nuevo)
            for insumo in lista_insumos:
                if id_nuevo == int(insumo["ID"]):
                    id_existe = True
                    break
            if not id_existe:
                print("ID ingresado")
                nombre_nuevo = input("Ingrese un nombre para el producto: ").capitalize()
                mostrar_marcas("marcas.txt")
                while True:
                    marca_nueva = input("Ahora ingrese una marca: ").capitalize()
                    if marca_nueva in leer_csv_marcas("marcas.txt"):
                        while True:
                            precio_nuevo = input("Ingrese un precio válido: ")
                            if validar_numero(precio_nuevo):
                                break
                            else:
                                print("Precio inválido. Intente nuevamente.")
                        caracteristicas_nuevas = []
                        for i in range(3):
                            caracteristica = input("Ingrese una característica del producto (o 'q' para finalizar): ").capitalize()
                            if caracteristica.lower() == 'q':
                                break
                            caracteristicas_nuevas.append(caracteristica)
                        producto_nuevo = {"ID": str(id_nuevo),"NOMBRE": nombre_nuevo, "MARCA": marca_nueva, "PRECIO": precio_nuevo, "CARACTERISTICAS": ",".join(caracteristicas_nuevas).split(",")}
                        lista_insumos.append(producto_nuevo)
                        print("Producto agregado con éxito.")
                        return producto_nuevo
                    else:
                        print("Marca no válida. Ingrese una marca existente.")
            else:
                imprimir_dato("El ID ingresado ya existe.")
        else:
            imprimir_dato("ERROR. No ingreso un valor correcto.")

def guardar_datos_actualizados(formato, nombre_archivo, lista):
    if formato == "csv":
        with open(nombre_archivo, "w", newline="", encoding="utf-8") as archivo:
            encabezados = ["ID", "NOMBRE", "MARCA", "PRECIO", "CARACTERISTICAS"]
            linea_encabezados = ",".join(encabezados) + "\n"
            archivo.write(linea_encabezados)
            for insumo in lista:
                linea = f'{insumo["ID"]},{insumo["NOMBRE"]},{insumo["MARCA"]},${insumo["PRECIO"]},{",".join(insumo["CARACTERISTICAS"])}\n'
                archivo.write(linea)
        imprimir_dato("Datos guardados en formato CSV correctamente.")
    elif formato == "json":
        with open(nombre_archivo, "w", newline="", encoding="utf-8") as archivo:
            json.dump(lista, archivo)
            imprimir_dato("Datos guardados en formato JSON correctamente.")
