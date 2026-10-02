productos = []

while True:
    print("-" * 30)
    print("MENU DE OPCIONES")
    print("-" * 30)
    print("1. Agregar producto")
    print("2. Mostrar productos")
    print("3. Buscar producto")
    print("4. Eliminar producto")
    print("5. Salir")

    opcion = input("Seleccione una opción(1-5): ").strip()

    # Validaciones de los datos ingresados por el usuario

    if opcion == "1":
        print("--- Agregar producto ---")

        nombre = input("Ingrese el nombre del producto: ").strip()

        while nombre == "":
            print("ERROR: El nombre del producto no puede estar vacío.")
            nombre = input("Ingrese el nombre del producto: ").strip()

        categoria = input("Ingrese la categoria del producto: ").strip()

        while categoria == "":
            print("ERROR: La categoria del producto no puede estar vacía.")
            categoria = input("Ingrese la categoria del producto: ").strip()

        precio_str = input("Ingrese el precio del producto sin centavos: ").strip()

        while not precio_str.isdigit():
            print("ERROR: El precio del producto debe ser un número entero positivo.")
            precio_str = input("Ingrese el precio del producto sin centavos: ").strip()

        precio = int(precio_str)

        datos = [nombre, categoria, precio]

        productos.append(datos)

        print("Producto agregado correctamente.")

    elif opcion == "2":
        print("--- Mostrar productos ---")

        if len(productos) == 0:
            print("No hay productos registrados.")
        else:
            for i in range(len(productos)):
                print(
                    f"{i + 1}. Nombre: {productos[i][0]}, "
                    f"Categoria: {productos[i][1]}, "
                    f"Precio: {productos[i][2]}"
                )

    elif opcion == "3":
        print("--- Buscar producto ---")

        if len(productos) == 0:
            print("No hay productos registrados.")
        else:
            nombre_buscar = input(
                "Ingrese el nombre del producto a buscar: "
            ).strip()

            encontrado = False

            for producto in productos:
                if producto[0].lower() == nombre_buscar.lower():
                    print(
                        f"Producto encontrado: "
                        f"Nombre: {producto[0]}, "
                        f"Categoria: {producto[1]}, "
                        f"Precio: {producto[2]}"
                    )
                    encontrado = True
                    break

            if not encontrado:
                print(f"No se encontró el producto '{nombre_buscar}'.")

    elif opcion == "4":
        print("--- Eliminar producto ---")

        if len(productos) == 0:
            print("No hay productos registrados.")
        else:
            # Mostrar los productos para que el usuario pueda elegir
            for i in range(len(productos)):
                print(
                    f"{i + 1}. Nombre: {productos[i][0]}, "
                    f"Categoria: {productos[i][1]}, "
                    f"Precio: {productos[i][2]}"
                )

            posicion_str = input(
                "Ingrese el número del producto que desea eliminar: "
            ).strip()

            # Validar que sea un número entero
            while not posicion_str.isdigit():
                print("ERROR: Debe ingresar un número.")
                posicion_str = input(
                    "Ingrese el número del producto que desea eliminar: "
                ).strip()

            posicion = int(posicion_str)

            # Validar que la posición exista
            if posicion < 1 or posicion > len(productos):
                print("ERROR: El número de producto no existe.")
            else:
                producto_eliminado = productos[posicion - 1]

                del productos[posicion - 1]

                print(
                    f"Producto '{producto_eliminado[0]}' "
                    "eliminado correctamente."
                )

    elif opcion == "5":
        print("Saliendo del programa, gracias por usarlo.")
        break