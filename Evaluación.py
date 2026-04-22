# %%
#===== PARTE A =====
#=====Parte A. Análisis y comprensión aplicada
#=== Indica el tipo de dato de cada variable
#=Nombre es un string.
#=Edad es un int.
#=Promedio es un float.
#=Cursos es una list.
#===Escribe qué mostraría el programa en pantalla
#=Lucia
#=16
#=9.75
#=Python HTML CSS
#=Lucia
#===Explica qué hace len(nombre).
#Len(nombre) no hace mas que repetir el nombre.
#===¿Qué diferencia hay entre print() e input()?
#=print() Se usa para mostrar datos en la pantalla. input() Se usa para pedir datos al usuario a través del teclado.
#===¿Por qué un dato ingresado con input() puede dar error si se usa directamente en un cálculo?
#=Porque todo lo que escribes en un input() Python lo recibe como un texto (string). Si intentas sumar o multiplicar ese texto con un número, el programa fallará.
#===Explica la diferencia entre /, // y %
#=(/) Te da el resultado exacto con decimales. (//) Te da solo la parte entera del resultado, quitando los decimales. (%) Te da el residuo o lo que sobra de la división.
#===Escribe una instrucción que permita comprobar la versión de Python que se está usando.
#=print(sys.version)
#===Escribe una instrucción que permita consultar las palabras reservadas de Python.
#=print(keyword.kwlist)
# %%
#===== PARTE B =====
#===Parte B. Corrección y construcción de fragmentos
largo = float(input("Ingrese el largo del terreno:"))
precio = float(input("Ingrese el precio por metro cuadrado:"))
ancho = float(input("Ingrese el ancho del terreno:"))
area = ancho * largo
costo = area * precio
print("Área total: ", area)
print("Costo estimado: ",costo)
#===¿Cuáles eran los errores principales?
#=No habia una variable para "Ancho" y puse "+" en vez de ",".
#===¿Por qué tu corrección sí permite obtener resultados válidos?
#= Mi corrección si me permite obterner resultados válidos, debido a que le de un valor y hize una variablable de "ancho" tambien correji los "+".
#===Cree la variable frase con el texto "Tecnología para todos"
"Tecnologia para todos"