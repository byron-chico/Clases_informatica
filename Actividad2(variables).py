
# %%
# Escribe un comentario de múltiples líneas con: nombre, fecha y título.
"""Nombre = Byron
Fecha = 15/4/26
 Titulo = Actividad2"""
# %%
nombre= "Byron"
apellido= "Chico"
nombreCompleto= "Byron Chico"
pais= "Ecuador"
ciudad= "Calderon"
edad= "16"
anio= "2026"
estaCasado= "No"
esVerdadero= "Si"
luzEncendida= "Si"
hobby,deporte,cumpleanos= "Leer","Futbol","31 de Diciembre 2009"
# %%
nombre= "Byron"
apellido= "Chico"
nombreCompleto= "Byron Chico"
print(type(nombre))
print(type(apellido))
print(type(nombreCompleto))
# %%

# Usando la función integrada len(), encuentra la longitud de tu variable nombre.  
print(len(nombre))
# Compara la longitud de tu nombre con la longitud de tu apellido.
print(len(nombre) > len(apellido))
print(len(nombre) < len(apellido))
print(len(nombre) == len(apellido))
# %%
# Declarar 5 como numeroUno y 4 como numeroDos.  
numeroUno = 5
numeroDos = 4
# %%
# Sumar numeroUno y numeroDos y asignar el resultado a una variable llamada total.  
total= numeroUno + numeroDos
print(total)
# %%
# Restar numeroDos de numeroUno y asignar el resultado a una variable llamada diferencia.
resta= numeroDos - numeroUno
print(resta)
# %%
# Multiplicar numeroUno por numeroDos y asignar el resultado a una variable llamada producto.  
multiplicacion= numeroDos * numeroUno
print(multiplicacion)
# %%
# Dividir numeroUno entre numeroDos y asignar el resultado a una variable llamada division.
division= numeroUno / numeroDos
print(division)
# %%
# Encontrar el módulo de numeroDos dividido por numeroUno y asignar el resultado a una variable llamada modulo.
modulo= numeroDos % numeroUno
print(modulo)
# %%
# Encontrar la potencia de numeroUno elevado a numeroDos y asignar el resultado a una variable llamada potencia.
potencia= numeroUno ** numeroDos
print(potencia)
# %%
# Encontrar la división entera de numeroUno entre numeroDos y asignar el resultado a una variable llamada divisionEntera.
divisionEntera= numeroUno // numeroDos
print(divisionEntera)
# %%
# El radio de un círculo es de 30 metros.  
radioEnMetros = 30
# %%
#Calcular el área de un círculo y asignar el valor a una variable llamada areaCirculo.  
areaDelCirculo = 3.14 * radioEnMetros ** 2
print(areaDelCirculo)
# %%
#Calcular la circunferencia de un círculo y asignar el valor a una variable llamada circunferenciaCirculo.  
circunferenciaDelCirculo = 2 * 3.14 * radioEnMetros
print(circunferenciaDelCirculo)
# %%
#Toma el valor del radio como entrada del usuario y calcula el área.  
radio=float(input("Ingrese el radio del círculo en metros: "))
areaDelCirculo = 3.14 * radio ** 2
print("El área del círculo es:", areaDelCirculo)
# %%
#Utiliza la función input() para obtener el nombre, apellido, país y edad de un usuario y almacena cada valor en su variable correspondiente.  
nombre = str(input("Ingrese su nombre: "))
apellido = str(input("Ingrese su apellido: "))
pais = str(input("Ingrese su país: "))
edad = int(input("Ingrese su edad: "))
# %%
#Ejecuta help('keywords') en la consola de Python o en tu archivo para comprobar las palabras reservadas de Python. 
help('keywords')
