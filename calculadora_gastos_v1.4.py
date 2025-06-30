# calculadora_gastos_v1.3.py
# Autor: Manuel A. García
# Descripción: Calculadora de gastos mensuales en consola

import json
import os

ARCHIVO = "gastos.json" # Constante con el nombre del fichero

def cargar_gastos():
    """Devuelve la lista de gastos desde 'gastos.json' o lista vacía."""
    if not os.path.exists(ARCHIVO):
        return []
    try:
        with open(ARCHIVO, "r", encoding="utf-8") as f:
            return json.load(f)
    except (json.JSONDecodeError, FileNotFoundError):
        # Archivo vacío o corrupto
        print("Aviso: no se pudo leer el archivo de gastos, se iniciará vacío.")
        return []
    
def guardar_gastos(gastos):
    """Guarda la lista de gastos en 'gastos.json'."""
    with open(ARCHIVO, "w", encoding="utf-8") as f:
        json.dump(gastos, f, ensure_ascii=False, indent=2)

def pedir_gasto():
    categoria = input("Introduce la categoría: ").strip().lower()
    try:
        importe = float(input("Introduce el importe en euros: "))
        if importe <= 0:
            print("El importe debe ser mayor que 0.")
            return None
    except ValueError:
        print("Error: introduce un número válido.")
        return None
    return {"categoria": categoria, "importe": importe}

def mostrar_gastos(gastos):
    if not gastos:
        print("No hay gastos registrados todavía.")
    else:
        print("\nLista de gastos:")
        for i, gasto in enumerate(gastos, start=1):
            print(f"{i}. {gasto['categoria'].capitalize():12}  {gasto['importe']:.2f} €")

def calcular_total(gastos):
    return sum(gasto["importe"] for gasto in gastos)

def calcular_total_por_categoria(gastos):
    totales = {}
    for gasto in gastos:
        cat = gasto["categoria"]
        imp = gasto["importe"]
        totales[cat] = totales.get(cat, 0) + imp
    return totales

def mostrar_totales(gastos):
    total = calcular_total(gastos)
    print(f"\n💰 Total gastado: {total:.2f} €")
    if total > 1000:
        print("¡Cuidado! Has superado los 1000 €.")

def mostrar_totales_por_categoria(gastos):
    tot_cat = calcular_total_por_categoria(gastos)
    if not tot_cat:
        print("No hay gastos para mostrar por categoría.")
        return
    print("\nGastos por categoría:")
    for cat, imp in tot_cat.items():
        print(f"- {cat.capitalize():12}: {imp:.2f} €")

def mostrar_menu():
    print("\n==== CALCULADORA DE GASTOS ====")
    print("1. Añadir gasto")
    print("2. Ver lista de gastos")
    print("3. Ver total gastado")
    print("4. Ver totales por categoría")
    print("5. Salir")

def main():
    gastos = cargar_gastos() # Cargamos al arrancar

    while True:
        mostrar_menu()
        opcion = input("Elige una opción (1-5): ").strip()
        if opcion == "1":
            gasto = pedir_gasto()
            if gasto:
                gastos.append(gasto)
                guardar_gastos(gastos)
                print("✅ Gasto añadido.")
        elif opcion == "2":
            mostrar_gastos(gastos)
        elif opcion == "3":
            mostrar_totales(gastos)
        elif opcion == "4":
            mostrar_totales_por_categoria(gastos)
        elif opcion == "5":
            print("👋 ¡Hasta pronto!")
            break
        else:
            print("Opción no válida. Elige un número del 1 al 5.")

if __name__ == "__main__":
    main()



