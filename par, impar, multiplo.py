def verificar_numero(numero, divisor):
    # Verificar si el número es par o impar
    if numero % 2 == 0:
        print(f"{numero} es un número par.")
    else:
        print(f"{numero} es un número impar.")
    
    # Verificar si el número es múltiplo de otro
    if numero % divisor == 0:
        print(f"{numero} es múltiplo de {divisor}.")
    else:
        print(f"{numero} no es múltiplo de {divisor}.")

#input
numero = int(input("Ingresa un número: "))
divisor = int(input("Ingresa el divisor para comprobar si es múltiplo: "))
verificar_numero(numero, divisor)
