def ingresar_datos():
    nombre = input("Ingrese el nombre: ")
    apellido = input("Ingrese el apellido: ")
    nota1 = float(input("Ingrese la nota 1: "))
    nota2 = float(input("Ingrese la nota 2: "))
    nota3 = float(input("Ingrese la nota 3: "))
    return nombre, apellido, nota1, nota2, nota3
 
def calcular_promedio(n1, n2, n3):
    return (n1 + n2 + n3) / 3
nom, ape, n1, n2, n3 = ingresar_datos()
promedio = calcular_promedio(n1, n2, n3)
print("\n--- DATOS DEL ESTUDIANTE ---")
print(f"Nombre: {nom}")
print(f"Apellido: {ape}")
print(f"Nota 1: {n1}")
print(f"Nota 2: {n2}")
print(f"Nota 3: {n3}")
print(f"Promedio: {promedio}")








def obtener_mensaje():
    mensaje = "Bienvenido al sistema"
    return mensaje
    
def nombre_completo():
    nombre = input ("Ingrese su nombre: ")
    apellido = input("Ingrese su apellido: ")
    espacio = " "
    nombre_completo= nombre + espacio + apellido
    return nombre_completo
    
print(obtener_mensaje())
print(nombre_completo())

def centimetros(metros):
    centimetros = metros*100
    return centimetros
def milimetros(metros):
    milimetros = metros*1000
    return milimetros
def kilometros(metros):
    kilometros = metros/1000
    return kilometros
def pulgadas(metros):
    pulgadas = metros*39.37
    return pulgadas
    
def centimetros(metros):
    centimetros = metros*100
    return centimetros
def milimetros(metros):
    milimetros = metros*1000
    return milimetros
def kilometros(metros):
    kilometros = metros/1000
    return kilometros
def pulgadas(metros):
    pulgadas = metros*39.37
    return pulgadas
    
metros = float(input("Ingrese una cantidad de metros: "))
print("====MENU====")
print ("1.centimentros")
print("2.milimetros")
print("3.kilometros")
print("4.pulgadas")
numero = int(input ("ingrese una de las opciones: "))
while True:
    if numero ==1:
        print (f"La cantidad de centimetros es: {centimetros(metros)}")
        break
    elif numero ==2:
        print (f"La cantidad de milimetros es: {milimetros(metros)}")
        break
    elif numero ==3:
         print (f"La cantidad de kilometros es: {kilometros(metros)}")
         break
    elif numero ==4:
         print (f"La cantidad de pulgadas es: {pulgadas(metros)}")
         break
    elif numero >=5:
        print("Numero no valido")
        break
#%%

def calcular_promedio(n1, n2, n3):
    return (n1 + n2 + n3) / 3
def obtener_mayor(n1, n2, n3):
    return max(n1, n2, n3)
def obtener_menor(n1, n2, n3):
    return min(n1, n2, n3)
def determinar_estado(promedio):
    if promedio >= 7: 
        return "Aprobado"
    else:
        return "Reprobado"
nota1 = float(input("Introduce la primera calificación: "))
nota2 = float(input("Introduce la segunda calificación: "))
nota3 = float(input("Introduce la tercera calificación: "))
while True:
    print("--- MENÚ DE CALIFICACIONES ---")
    print("1. Calcular el promedio")
    print("2. Mostrar la nota mayor")
    print("3. Mostrar la nota menor")
    print("4. Determinar si aprueba o reprueba")
    print("5. Salir del programa")
    opcion = input("Selecciona una opción (del 1 al 5): ")
    if opcion == "1":
        prom = calcular_promedio(nota1, nota2, nota3)
        print(f"El promedio de las calificaciones es: {prom}")
    elif opcion == "2":
        mayor = obtener_mayor(nota1, nota2, nota3)
        print(f"La calificación más alta es: {mayor}")
    elif opcion == "3":
        menor = obtener_menor(nota1, nota2, nota3)
        print(f"La calificación más baja es: {menor}")
    elif opcion == "4":
        prom = calcular_promedio(nota1, nota2, nota3)
        estado = determinar_estado(prom)
        print(f"El estado del estudiante es: {estado}")
    elif opcion == "5":
        print("Ha salido del programa")
        break
    else:
        print("Opción no válida. Por favor, intente de nuevo.")
         nota1 = float(input("Introduce la primera calificación: "))
        nota2 = float(input("Introduce la segunda calificación: "))
        nota3 = float(input("Introduce la tercera calificación: "))
        
