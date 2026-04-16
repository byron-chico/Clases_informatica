# %%
edad = 16
estatura = 1.72
# %%
base = float(input("Ingrese la base del triangulo:")) 
altura = float(input("Ingrese la altura del triangulo:")) 
area = 0.5 * base * altura 
print("Área:", area) 
# %%
a = float(input("Ingrese lado a:")) 
b = float(input("Ingrese lado b:")) 
c = float(input("Ingrese lado c:")) 
perimetro = a + b + c 
print("Perímetro:", perimetro) 
# %%
longitud = float(input("Ingrese la longitud:")) 
ancho = float(input("Ingrese el ancho:")) 
area = longitud * ancho 
perimetro = 2 * (longitud + ancho) 
print("Área:", area) 
print("Perímetro:", perimetro) 
# %%
radio = float(input("Ingrese el radio:")) 
pi = 3.14 
area = pi * radio * radio 
circunferencia = 2 * pi * radio 
print("Área:", area) 
print("Circunferencia:", circunferencia) 
# %%
x1, y1 = 2, 2 
x2, y2 = 6, 10 
pendiente = (y2 - y1) / (x2 - x1) 
distancia = ((x2 - x1)**2 + (y2 - y1)**2) ** 0.5 
print("Pendiente:", pendiente) 
print("Distancia:", distancia) 
# %%
x = -3 
y = x**2 + 6*x + 9 
print("y:", y) 
# %%
print(len("python") == len("dragón"))
# %%
print("on" in "python" and "on" in "dragón")
# %%
oracion = "Espero que este curso no esté lleno de jerga" 
print("jerga" in oracion)
# %%
print("on" in "python" and "on" in "dragon")
#%%
valor = len("python")
print(str(float(valor)))
# %%
print(7 // 3 == int(2.7))
# %%
print(type("10") == type(10))
# %%
print(int(float("9.8")) == 10)
# %%
horas = float(input("Ingrese horas:"))
tarifa = float(input("Ingrese tarifa por hora:"))
pago = horas * tarifa 
print("Pago:", pago)
# %%
anios = int(input("Ingrese años:"))
segundos = anios * 365 * 24 * 60 * 60 
print("Segundos vividos:", segundos)
# %%
print("1 1 1 1 1") 
print("2 1 2 4 8")
print("3 1 3 9 27")
print("4 1 4 16 64")
print("5 1 5 25 125")
# %%