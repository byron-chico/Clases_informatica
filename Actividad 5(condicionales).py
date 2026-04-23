A = 3
if A>0:
    print(f"{A} es positivo")
else:
    print(f"{A} es negativo")
print("Gracias por usar el programa")
#%%
#=Ejercicio
nota=int(input("Ingrese su calificación "))
if nota >= 90:
    print("A")
else:
    if nota >=80:
        print("B")
    else:
        if nota >= 70:
            print("C")
        else:
            if nota < 70:
                print("D")
