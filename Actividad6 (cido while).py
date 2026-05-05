opcion = ""
while opcion != "C":
    print("Menú de opciones:")
    print("Opción A: Saludar")
    print("Opción B: Mostrar mensaje")
    print("Opción C: Salir")

    opcion = input("Seleccione una opcion")

    if opcion == "A":
        print("Hola")
    elif opcion == "B":
        print("Estamos aprendiendo ciclos while")
    elif opcion == "C":
        print("Saliendo del programa")
    else:
        print("Opción no válida")