# calculadora_gastos_v1.7.py
# Autor: Manuel A. García
# Descripción: Calculadora de gastos profesional (añadir, ver, editar, eliminar, etc.)

import json
import os

ARCHIVO = "gastos.json"  # Nombre del archivo para guardar los datos

# ───── FUNCIONES DE ARCHIVO ─────
def cargar_gastos():
    if not os.path.exists(ARCHIVO):
        return []
    try:
        with open(ARCHIVO, "r", encoding="utf-8") as f:
            return json.load(f)
    except (json.JSONDecodeError, FileNotFoundError):
        print("Aviso: no se pudo leer el archivo. Se iniciará vacío.")
        return []

def guardar_gastos(gastos):
    with open(ARCHIVO, "w", encoding="utf-8") as f:
        json.dump(gastos, f, ensure_ascii=False, indent=2)

# ───── FUNCIONES DE OPERACIONES ─────
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
            print(f"{i}. {gasto['categoria'].capitalize():12} {gasto['importe']:.2f} €")

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
        print("No hay gastos por categoría.")
        return
    print("\nGastos por categoría:")
    for cat, imp in tot_cat.items():
        print(f"- {cat.capitalize():12}: {imp:.2f} €")

# ───── FUNCIONES EXTRA ─────
def editar_gasto(gastos):
    mostrar_gastos(gastos)
    try:
        num = int(input("¿Qué gasto quieres editar? (Número): "))
        if 1 <= num <= len(gastos):
            nuevo = pedir_gasto()
            if nuevo:
                gastos[num - 1] = nuevo
                print("✏️ Gasto editado correctamente.")
        else:
            print("Número inválido.")
    except ValueError:
        print("Introduce un número válido.")

def eliminar_gasto(gastos):
    mostrar_gastos(gastos)
    try:
        num = int(input("¿Qué gasto quieres eliminar? (Número): "))
        if 1 <= num <= len(gastos):
            eliminado = gastos.pop(num - 1)
            print(f"🗑️ Gasto eliminado: {eliminado['categoria'].capitalize()} - {eliminado['importe']} €")
        else:
            print("Número inválido.")
    except ValueError:
        print("Introduce un número válido.")

# ───── MENÚ ─────
def mostrar_menu():
    print("\n==== CALCULADORA DE GASTOS v1.7 ====")
    print("1. Añadir gasto")
    print("2. Ver lista de gastos")
    print("3. Ver total gastado")
    print("4. Ver totales por categoría")
    print("5. Editar gasto")
    print("6. Eliminar gasto")
    print("7. Salir")

def main():
    gastos = cargar_gastos()

    while True:
        mostrar_menu()
        opcion = input("Elige una opción (1-7): ").strip()

        if opcion == "1":
            gasto = pedir_gasto()
            if gasto:
                gastos.append(gasto)
                print("✅ Gasto añadido.")
        elif opcion == "2":
            mostrar_gastos(gastos)
        elif opcion == "3":
            mostrar_totales(gastos)
        elif opcion == "4":
            mostrar_totales_por_categoria(gastos)
        elif opcion == "5":
            editar_gasto(gastos)
        elif opcion == "6":
            eliminar_gasto(gastos)
        elif opcion == "7":
            guardar_gastos(gastos)
            print("💾 Datos guardados. ¡Hasta pronto!")
            break
        else:
            print("Opción no válida. Elige del 1 al 7.")

if __name__ == "__main__":
    main()
