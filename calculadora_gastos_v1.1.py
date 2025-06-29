# calculadora_gastos_v1.1.py
# Autor: Manuel A. García
# Descripción: Calculadora de gastos mensuales en consola

def pedir_cantidad_gastos():
    return int(input("¿Cuántos gastos vas a introducir? "))

def pedir_gasto(i):
    categoria = input(f"Gasto {i} - Introduce la categoría: ").strip().lower()
    importe = float(input(f"Gasto {i} - Introduce el importe en euros: "))
    return {"categoria": categoria, "importe": importe}

def calcular_total(gastos):
    return sum(gasto["importe"] for gasto in gastos)

def calcular_total_por_categoria(gastos):
    totales = {}
    for gasto in gastos:
        categoria = gasto["categoria"]
        importe = gasto["importe"]
        if categoria in totales:
            totales[categoria] += importe
        else:
            totales[categoria] = importe
    return totales

def mostrar_resultado(total):
    print(f"\nHas gastado un total de {total:.2f} €")
    if total > 1000:
        print("¡Cuidado! Has superado los 1000 €.")

def mostrar_resultado_por_categoria(totales):
    print("\nGastos por categoría:")
    for categoria, total in totales.items():
        print(f"- {categoria.capitalize()}: {total:.2f} €")

def main():
    gastos = []
    cantidad = pedir_cantidad_gastos()

    for i in range(1, cantidad + 1):
        gasto = pedir_gasto(i)
        gastos.append(gasto)

    total = calcular_total(gastos)
    mostrar_resultado(total)

    totales_categoria = calcular_total_por_categoria(gastos)
    mostrar_resultado_por_categoria(totales_categoria)

if __name__ == "__main__":
    main()

