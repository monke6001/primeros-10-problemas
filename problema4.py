def fibonacci(n):
    a, b = 0, 1
    for _ in range(n):
        print(a, end=' ')
        a, b = b, a + b

# Solicitar al usuario el número de términos
t = int(input("Ingrese el número de términos: "))
fibonacci(t)
