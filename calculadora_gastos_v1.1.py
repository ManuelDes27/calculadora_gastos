# calculadora_gastos_v1.1.py
# Autor: Manuel A. García
# Descripción: Calculadora de gastos mensuales en consola

def pedir_cantidad_gastos(): # Función para pedir al usuario la cantidad de gastos que va a introducir
    return int(input("¿Cuántos gastos vas a introducir? "))

def pedir_gasto(i): # Función para pedir al usuario que introduzca los gastos
    return float(input(f"Introduce el gasto número {i}: "))

def calcular_total(lista_gastos): # Función para sumar todos los gastos
    return sum(lista_gastos)

def mostrar_resultado(total): # Función para mostrar el total
    print(f"\nHas gastado un total de {total:.2f} €")
    if total > 1000: # Si los gastos superan los 1000 € se muestra mensaje de advertencia
        print("¡Cuidado! Has superado los 1000 €.")

def main():  # Esta es la función principal, la que dirige todo
    gastos = []  # Creamos una lista vacía para los gastos
    cantidad = pedir_cantidad_gastos()  # Llamamos a la función que pide cuántos gastos vas a meter

    for i in range(1, cantidad + 1):  # Bucle para pedir cada gasto uno por uno
        gasto = pedir_gasto(i)
        gastos.append(gasto)

    total = calcular_total(gastos)  # Sumamos todos los gastos
    mostrar_resultado(total)  # Mostramos el resultado por pantalla


# Si este archivo es el que se está ejecutando, entonces se ejecuta la función main
if __name__ == "__main__":
    main()
