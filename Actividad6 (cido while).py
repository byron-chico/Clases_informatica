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
#%%
numbers= [0,1,2,3,4,5]
for number in numbers:
    print(number)
#%%
Notas = [8,7,9,10,6]
suma = 0
for nota in Notas:
    suma= suma + nota
promedio = suma / len(Notas)
print(promedio)
#%%
language = "Python"
for letter in language:
    print(letter)
#%%
palabra= input("Ingrese una palabra: ")
vocales = 0
consonantes = 0
for letra in palabra:
    if letra == "a" or letra == "e" or letra == "i" or letra == "o" or letra == "u":
            vocales= vocales + 1
    else:
        consonantes += 1

print(f"La palabra '{palabra}' tiene {vocales} vocales y {consonantes} consonantes, tiene {consonantes + vocales} caracteres en total")