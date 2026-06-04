StringVariaslineas= """
Byron
Informatica ruta 3
"""
print(StringVariaslineas)
Colegio= "Ism"
longitud= len(Colegio)
print(longitud)
print(len)
print(len("San francisco de quito"))
Nombre= "Byron"
Apellido= "Chico"
Nombre_completo= Nombre+ "" +Apellido+ ""
print(Nombre_completo)
print("Mi nombre completo es",Nombre,Apellido)
print(Nombre_completo*5)
print("python\nchallenge")
print("Nombre\tsemana1\tsemana2\tsemana3")
print("simbolo(\\)")
print(f"Mi nombre es:{Nombre} y mi Apellido es {Apellido}")
Nombre= "python"
a,b,c,d,e,f = Nombre
print(a,b,c,d,e,f)
info= "python"
print(info[2])
print(info[::-2])
frase = "soy del ISM"
print(frase.capitalize())

#DEBER
#Nivel 1
texto = "Programación Para Todos"
#%%
print(texto)
print("Cantidad de caracteres:", len(texto))
#%%
#Nivel 2
print(texto.upper())
print(texto.lower())
print(texto.title())
print(texto.capitalize())
#%%
#Nivel 3
print(texto.startswith("Programación"))
print(texto.endswith("Todos"))
print(texto.find("Para"))
print("Python" in texto)
# %%
#Nivel 4
print(texto.replace("Programación", "Python"))

palabras = texto.split()
print(palabras)

print(" - ".join(palabras))
#%%
# Nivel 5
print(texto[0])
print(texto[-1])
print(texto[5])
#%%
#Nivel 6
nombre = "Byron"
apellido = "Chico"
print(f"Hola, mi nombre es {nombre} {apellido}")

# Acrónimo
print(nombre[0] + apellido[0])
