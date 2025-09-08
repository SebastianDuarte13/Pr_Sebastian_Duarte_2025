productos = {}

def main():
    while True:
        menu()
        try:
            opcion = int(input("Ingrese una opción: "))
            match opcion:
                case 1:
                    agregarProducto()
                case 2:
                    venderProducto()
                case 3:
                    mostrarTotal()
                case 4:
                    verInventario()
                case 5:
                    print("Saliendo...")
                    break
                case _:
                    print("Opción inválida")
        except ValueError:
            print("Por favor, ingresa un número válido.")

def menu():
    print("\nSeleccione su opción:")
    print("1) Agregar producto")
    print("2) Vender producto")
    print("3) Ver total de productos")
    print("4) Ver inventario")
    print("5) Salir")

def agregarProducto():
    nom = input('Ingrese nombre del producto:\n')
    
    if nom in productos:
        print(f"El producto '{nom}' ya existe. Actualizando stock.")
        try:
            extra_stock = int(input(f"Ingrese la cantidad adicional para '{nom}':\n"))
            productos[nom]['stock'] += extra_stock
        except ValueError:
            print("Stock inválido.")
        return

    try:
        stock = int(input(f"Ingrese el stock de '{nom}':\n"))
        precioU = float(input(f"Ingrese el precio por unidad de '{nom}':\n"))
        productos[nom] = {'stock': stock, 'precio': precioU}
        print(f"El producto '{nom}' ha sido agregado exitosamente.")
    except ValueError:
        print("Datos inválidos. Stock debe ser entero y precio un número.")

def venderProducto():
    nom = input('Ingrese el nombre del producto a vender:\n')
    if nom not in productos:
        print(f"El producto '{nom}' no está en el inventario.")
        return

    try:
        cantidad = int(input(f"Ingrese la cantidad a vender de '{nom}':\n"))
        if cantidad <= 0:
            print("La cantidad debe ser mayor que cero.")
        elif cantidad > productos[nom]['stock']:
            print("No hay suficiente stock para esta venta.")
        else:
            productos[nom]['stock'] -= cantidad
            total = cantidad * productos[nom]['precio']
            print(f"Venta realizada. Total: ${total:.2f}")
            if productos[nom]['stock'] == 0:
                print(f"El producto '{nom}' se ha agotado.")
    except ValueError:
        print("Cantidad inválida.")

def mostrarTotal():
    total_items = sum(producto['stock'] for producto in productos.values())
    print(f"Total de productos en inventario: {total_items}")

def verInventario():
    if not productos:
        print("El inventario está vacío.")
        return
    print("\nInventario actual:")
    for nombre, datos in productos.items():
        print(f"- {nombre}: {datos['stock']} unidades | ${datos['precio']} c/u")

if __name__ == "__main__":
    main()
