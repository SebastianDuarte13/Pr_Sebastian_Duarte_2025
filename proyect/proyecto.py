import json
import os

ARCHIVO = "proyect/canciones.json"

def cargar_canciones():
    if not os.path.exists(ARCHIVO):
        return []
    with open(ARCHIVO, "r", encoding="utf-8") as f:
        try:
            return json.load(f)
        except json.JSONDecodeError:
            return []

def guardar_canciones(canciones):
    
    with open(ARCHIVO, "w", encoding="utf-8") as f:
        json.dump(canciones, f, indent=4, ensure_ascii=False)

def menu():
    while True:
        print("""
        -----------------------------------
        |        MENÚ PRINCIPAL           |
        -----------------------------------
        | 1. Agregar Canción              |
        | 2. Borrar Canción               |
        | 3. Buscar Canción               |
        | 4. Tiempo Total                 |
        | 5. Salir                        |
        -----------------------------------
        """)
        opcion = input("Elige una opción (1-5): ")

        match opcion:
            case '1':
                os.system('cls')
                agregar_cancion()
            case '2':
                os.system('cls')
                borrar_cancion()
            case '3':
                os.system('cls')
                buscar_cancion()
            case '4':
                os.system('cls')
                tiempo_total()
            case '5':
                print("Saliendo del programa...")
                break
            case _:
                print("Opción no válida. Inténtalo de nuevo.")

def agregar_cancion():
    canciones = cargar_canciones()

    nombre = input("Ingrese el nombre de la canción: ")
    artista = input("Ingrese el nombre del artista: ")
    año = int(input("Ingrese el año de lanzamiento: "))
    genero = input("Ingrese el género musical: ")
    idioma = input("Ingrese el idioma: ")
    duracion = input("Ingrese la duración (mm:ss): ")

    nueva_cancion = {
        "nombre": nombre,
        "artista": artista,
        "año": año,
        "duracion": [duracion],  
        "genero": genero,
        "idioma": idioma
    }

    canciones.append(nueva_cancion)
    guardar_canciones(canciones)

    print(f"Canción '{nombre}' agregada exitosamente.\n")

def borrar_cancion():
    canciones = cargar_canciones()
    nombre = input("Ingrese el nombre de la canción a borrar: ")

    nuevas_canciones = [c for c in canciones if c["nombre"].lower() != nombre.lower()]

    if len(nuevas_canciones) < len(canciones):
        guardar_canciones(nuevas_canciones)
        print(f"Canción '{nombre}' borrada exitosamente.\n")
    else:
        print(f"No se encontró la canción '{nombre}'.\n")

def buscar_cancion():
    canciones = cargar_canciones()
    nombre = input("Ingrese el nombre de la canción a buscar: ")

    encontradas = [c for c in canciones if c["nombre"].lower() == nombre.lower()]

    if encontradas:
        print("""
        -----------------------------------------------------------------------
        | Nombre        | Artista       | Año  | Duración | Género | Idioma   |
        -----------------------------------------------------------------------
        """)
        for c in encontradas:
            print(f"| {c['nombre']:<13}| {c['artista']:<13}| {c['año']:<5}| {c['duracion'][0]:<8}| {c['genero']:<7}| {c['idioma']:<8}|")
        print("-------------------------------------------------------------------\n")
    else:
        print(f"No se encontró la canción '{nombre}'.\n")

def tiempo_total():
    canciones = cargar_canciones()
    total_segundos = 0

    for c in canciones:
        for dur in c["duracion"]:
            minutos, segundos = map(int, dur.split(":"))
            total_segundos += minutos * 60 + segundos

    minutos = total_segundos // 60
    segundos = total_segundos % 60
    print(f"Tiempo total de reproducción: {minutos:02d}:{segundos:02d}\n")

if __name__ == "__main__":
    menu()
