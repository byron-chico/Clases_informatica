#%%
# Tarea
notas = [8.5, 6.0, 9.0, 7.0, 5.5]
suma= 0
for nota in notas:
    suma= suma + nota
Total= suma + len(notas)
print("El total de notas es: ")
print(Total)
promedio = suma / len(notas)
print("El promedio de la clase es: ") 
print(promedio)