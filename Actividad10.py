inventario = {}

quantity = int(input("¿Cuántos productos desea ingresar? "))

count = 1

while count <= quantity:
    print("\nIngreso de Producto ", count)

    code = input("Código del Producto (ej. P001): ")
    while code in inventario.keys():
        print("Este código ya existe.")
        code = input("Ingresa un código diferente: ")

    name = input("Ingresa el nombre del producto: ")

    category = input("Categoría (Hombre, Mujer, Niño): ")
    while category != "Hombre" and category != "Mujer" and category != "Niño":
        print("Categoría Inválida. Debe ser exactamente Hombre, Mujer o Niño.")
        category = input("Ingresa una categoría válida: ")

    size = input("Talla (S, M, L, XL): ")
    while size != "S" and size != "M" and size != "L" and size != "XL":
        print("Talla inválida. Debe ser exactamente S, M, L o XL.")
        size = input("Ingresa una talla válida: ")

    price = float(input("Precio unitario (mayor a 0): Q"))
    while price <= 0:
        print("¡Precio inválido!")
        price = float(input("Ingresa un precio válido Q: "))

    stock = int(input("Cantidad de stock (entero positivo): "))
    while stock < 0:
        print("¡Cantidad inválida!")
        stock = int(input("Ingresa una cantidad válida: "))

    inventario[code] = {
        "name": name,
        "category": category,
        "size": size,
        "price": price,
        "stock": stock,
    }
    count += 1
print("\nLista de productos registrados: ")
for cod, data in inventario.items():
    print(cod, "|", data["name"], "|", data["category"], "| Talla:", data["size"], "| Q", data["price"], "| Stock:", data["stock"])
print()

searching_code = input("\nIngresa un código de producto para ver sus detalles: ")
if searching_code in inventario.keys():
    prod = inventario[searching_code]
    print("\n----Detalles de tu producto----")
    print("Nombre: ", prod["name"])
    print("Categoría: ", prod["category"])
    print("Talla: ", prod["size"])
    print("Precio: ", prod["price"])
    print("Stock: ", prod["stock"])
else:
    print("Producto no encontrado.")

total = 0
for prod in inventario.values():
    total += prod["price"] * prod["stock"]

print("\nValor total del inventario: Q.", round(total, 2))

man = 0
woman = 0
boy = 0

for prod in inventario.values():
    if prod["category"] == "Hombre":
        man += 1
    if prod["category"] == "Mujer":
        woman += 1
    if prod["category"] == "Niño":
        boy += 1

print("\nCantidad de productos por categoría:")
print("Hombre:", man)
print("Mujer:", woman)
print("Niño:", boy)
