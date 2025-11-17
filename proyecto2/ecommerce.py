import requests
import json

# URL de la API de productos
PRODUCTS_API_URL = "https://dummyjson.com/products"
SALES_FILE = "ventas.json"

def load_products():
    """Carga los productos desde la API."""
    try:
        response = requests.get(PRODUCTS_API_URL)
        response.raise_for_status()  # Lanza un error para respuestas HTTP malas (4xx o 5xx)
        return response.json().get('products', [])
    except requests.exceptions.RequestException as e:
        print(f"Error al cargar los productos desde la API: {e}")
        return []

def load_sales():
    """Carga las ventas desde el archivo JSON."""
    try:
        with open(SALES_FILE, 'r') as f:
            return json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        return []

def save_sales(sales):
    """Guarda las ventas en el archivo JSON."""
    with open(SALES_FILE, 'w') as f:
        json.dump(sales, f, indent=4)

def start_sale(products, sales):
    """Maneja el proceso de una nueva venta."""
    cart = []
    total_value = 0

    while True:
        search_term = input("Buscar producto por nombre (o 'fin' para terminar de agregar): ")
        if search_term.lower() == 'fin':
            break

        if not search_term.strip():
            print("Por favor, ingrese un término de búsqueda.")
            continue

        matching_products = [p for p in products if search_term.lower() in p['title'].lower()]

        if not matching_products:
            print("No se encontraron productos.")
            continue

        print("Productos encontrados:")
        for i, p in enumerate(matching_products):
            print(f"{i + 1}. {p['title']} - Precio: ${p['price']} (Stock: {p['stock']})")

        try:
            product_choice = int(input("Seleccione el número del producto a agregar: ")) - 1
            if not 0 <= product_choice < len(matching_products):
                print("Selección no válida.")
                continue
            
            selected_product = matching_products[product_choice]

            quantity = int(input(f"Ingrese la cantidad de '{selected_product['title']}' a comprar: "))
            if quantity > 20:
                print("Alerta: Cantidad no permitida (máximo 20).")
                continue
            if quantity > selected_product['stock']:
                print("No hay suficiente stock disponible.")
                continue

            # Agregar al carrito
            cart_item = {
                "id": selected_product['id'],
                "title": selected_product['title'],
                "price": selected_product['price'],
                "quantity": quantity,
                "total_price": selected_product['price'] * quantity
            }
            cart.append(cart_item)
            total_value += cart_item['total_price']
            
            # Actualizar stock temporalmente (se hará permanente al confirmar)
            selected_product['stock'] -= quantity

            print("\n--- Carrito de Compras ---")
            for item in cart:
                print(f"- {item['title']} (x{item['quantity']}): ${item['total_price']:.2f}")
            print(f"--------------------------")
            print(f"Valor Total Acumulado: ${total_value:.2f}\n")

        except ValueError:
            print("Entrada no válida. Por favor, ingrese un número.")

    if not cart:
        print("No se agregaron productos al carrito. Venta cancelada.")
        return

    confirm = input("¿Desea confirmar la compra? (s/n): ")
    if confirm.lower() == 's':
        customer_name = input("Ingrese su nombre: ")
        customer_email = input("Ingrese su correo electrónico: ")

        new_sale = {
            "customer_name": customer_name,
            "customer_email": customer_email,
            "total_value": total_value,
            "products": cart
        }
        sales.append(new_sale)
        save_sales(sales)
        print("¡Venta realizada con éxito!")
    else:
        # Revertir el stock si la venta es cancelada
        for item in cart:
            for p in products:
                if p['id'] == item['id']:
                    p['stock'] += item['quantity']
                    break
        print("Venta cancelada.")


def view_all_sales(sales):
    """Muestra todas las ventas realizadas."""
    if not sales:
        print("No hay ventas registradas.")
        return

    print("\n--- Todas las Ventas ---")
    for i, sale in enumerate(sales):
        print(f"\nVenta #{i + 1}")
        print(f"  Cliente: {sale['customer_name']} ({sale['customer_email']})")
        print(f"  Valor Total: ${sale['total_value']:.2f}")
        print("  Productos:")
        for item in sale['products']:
            print(f"    - {item['title']} (x{item['quantity']}) - Código: {item['id']} - Precio Unit.: ${item['price']:.2f} - Total: ${item['total_price']:.2f}")

def view_sales_by_customer(sales):
    """Busca y muestra ventas por nombre o email del cliente."""
    if not sales:
        print("No hay ventas registradas.")
        return

    query = input("Ingrese el nombre o correo electrónico del cliente a buscar: ").lower()
    
    found_sales = [
        s for s in sales 
        if query in s['customer_name'].lower() or query in s['customer_email'].lower()
    ]

    if not found_sales:
        print("No se encontraron ventas para ese cliente.")
        return

    print(f"\n--- Ventas para '{query}' ---")
    view_all_sales(found_sales) # Reutilizamos la función de mostrar ventas


def main():
    """Función principal del programa."""
    products = load_products()
    sales = load_sales()

    if not products:
        print("No se pudieron cargar los productos. El programa no puede continuar.")
        return

    # Ajustar el stock inicial con las ventas ya realizadas
    for sale in sales:
        for sold_product in sale['products']:
            for p in products:
                if p['id'] == sold_product['id']:
                    p['stock'] -= sold_product['quantity']
                    break

    while True:
        print("\n--- Menú E-commerce ---")
        print("1. Iniciar una venta")
        print("2. Consultar las ventas realizadas")
        print("3. Consulta de ventas por cliente")
        print("4. Salir")

        choice = input("Seleccione una opción: ")

        if choice == '1':
            start_sale(products, sales)
        elif choice == '2':
            view_all_sales(sales)
        elif choice == '3':
            view_sales_by_customer(sales)
        elif choice == '4':
            print("Gracias por usar el programa. ¡Hasta luego!")
            break
        else:
            print("Opción no válida. Por favor, intente de nuevo.")

if __name__ == "__main__":
    main()
