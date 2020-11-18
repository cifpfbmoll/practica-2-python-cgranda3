# Practica 2: Diagrama que diga si un número es par o non
print("Verifica si un número es par o non")
num = int(input("Introduce el número: "))
if num == 0:
    print(num, "no es par ni impar")
else:
    if num % 2 == 0:
        print("El número", num, "es par")
    else:
        print("El número", num, "es impar")
