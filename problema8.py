import math

def calcular_area_y_circunferencia(radio):
    # Calcular área
    area = math.pi * radio**2
    
    # Calcular circunferencia
    circunferencia = 2 * math.pi * radio
    
    return area, circunferencia

# input
radio = float(input("Ingresa el radio del círculo: "))
area, circunferencia = calcular_area_y_circunferencia(radio)

print(f"Área del círculo: {area:.2f}")
print(f"Circunferencia del círculo: {circunferencia:.2f}")
