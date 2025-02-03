def interes_compuesto(capital, tasa, tiempo):
    return capital * (1 + tasa / 100) ** tiempo

# Solicitar al usuario los valores
capital = float(input("Ingrese el capital inicial: "))
tasa = float(input("Ingrese la tasa de interés anual (%): "))
tiempo = int(input("Ingrese el tiempo en años: "))

monto_final = interes_compuesto(capital, tasa, tiempo)
print(f"El monto final después de {tiempo} años será: {monto_final:.2f}")
