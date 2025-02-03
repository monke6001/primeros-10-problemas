def generar_pares_impares(limite):
    # Listas para números pares e impares
    pares = []
    impares = []
    
    for numero in range(1, limite + 1):
        if numero % 2 == 0:
            pares.append(numero)
        else:
            impares.append(numero)
    
    return pares, impares

# input
limite = int(input("Ingresa el límite: "))
pares, impares = generar_pares_impares(limite)

print(f"Números pares hasta {limite}: {pares}")
print(f"Números impares hasta {limite}: {impares}")
