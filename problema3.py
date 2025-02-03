import math

num = int(input("Número para calcular el factorial: "))
print("Factorial:", math.factorial(num) if num >= 0 else "No se puede calcular el factorial de un número negativo")
