def mostrar_menu():
    print("\nAGENDA TELEFÓNICA")
    print("1. Añadir/Modificar Contacto")
    print("2. Buscar Contacto")
    print("3. Borrar Contacto")
    print("4. Listar Contactos")
    print("5. Salir")
    
def anadir_modificar_contacto(agenda):
    nombre = input("Ingrese el nombre del contacto: ").strip()
    if nombre in agenda:
        print(f"El número actual de {nombre} es: {agenda[nombre]}")
        opcion = input("¿Desea modificarlo? (s/n): ").strip().lower()
        if opcion == 's':
            telefono = input("Ingrese el nuevo número: ").strip()
            agenda[nombre] = telefono
            print("Contacto actualizado.")
    else:
        telefono = input("Ingrese el número de teléfono: ").strip()
        agenda[nombre] = telefono
        print("Contacto añadido.")

def buscar_contacto(agenda):
    cadena = input("Ingrese el inicio del nombre a buscar: ").strip()
    resultados = {nombre: telefono for nombre, telefono in agenda.items() if nombre.startswith(cadena)}
    if resultados:
        for nombre, telefono in resultados.items():
            print(f"{nombre}: {telefono}")
    else:
        print("No se encontraron contactos con esa búsqueda.")

def borrar_contacto(agenda):
    nombre = input("Ingrese el nombre del contacto a eliminar: ").strip()
    if nombre in agenda:
        opcion = input(f"¿Está seguro de eliminar a {nombre}? (s/n): ").strip().lower()
        if opcion == 's':
            del agenda[nombre]
            print("Contacto eliminado.")
        else:
            print("Operación cancelada.")
    else:
        print("El contacto no existe en la agenda.")

def listar_contactos(agenda):
    if agenda:
        print("\nLista de Contactos:")
        for nombre, telefono in agenda.items():
            print(f"{nombre}: {telefono}")
    else:
        print("La agenda está vacía.")

def main():
    agenda = {}
    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción: ").strip()
        if opcion == '1':
            anadir_modificar_contacto(agenda)
        elif opcion == '2':
            buscar_contacto(agenda)
        elif opcion == '3':
            borrar_contacto(agenda)
        elif opcion == '4':
            listar_contactos(agenda)
        elif opcion == '5':
            print("Saliendo de la agenda...")
            break
        else:
            print("Opción no válida. Inténtelo de nuevo.")

if __name__ == "__main__":
    main()
