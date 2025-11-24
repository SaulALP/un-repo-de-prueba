#!/usr/bin/env python3
"""
Calculadora Simple
Una calculadora básica que puede realizar operaciones aritméticas fundamentales.
"""

def sumar(a, b):
    """Suma dos números."""
    return a + b

def restar(a, b):
    """Resta dos números."""
    return a - b

def multiplicar(a, b):
    """Multiplica dos números."""
    return a * b

def dividir(a, b):
    """Divide dos números."""
    if b == 0:
        raise ValueError("No se puede dividir por cero")
    return a / b

def potencia(a, b):
    """Calcula a elevado a la potencia b."""
    return a ** b

def raiz_cuadrada(a):
    """Calcula la raíz cuadrada de un número."""
    if a < 0:
        raise ValueError("No se puede calcular la raíz cuadrada de un número negativo")
    return a ** 0.5

def mostrar_menu():
    """Muestra el menú de opciones."""
    print("\n=== CALCULADORA SIMPLE ===")
    print("1. Sumar")
    print("2. Restar")
    print("3. Multiplicar")
    print("4. Dividir")
    print("5. Potencia")
    print("6. Raíz cuadrada")
    print("7. Salir")
    print("=" * 26)

def obtener_numero(mensaje):
    """Obtiene un número del usuario con validación."""
    while True:
        try:
            return float(input(mensaje))
        except ValueError:
            print("Error: Por favor ingrese un número válido.")

def calculadora():
    """Función principal de la calculadora."""
    print("¡Bienvenido a la Calculadora Simple!")
    
    while True:
        mostrar_menu()
        
        try:
            opcion = input("Seleccione una opción (1-7): ")
            
            if opcion == "7":
                print("¡Gracias por usar la calculadora!")
                break
            
            if opcion in ["1", "2", "3", "4", "5"]:
                num1 = obtener_numero("Ingrese el primer número: ")
                num2 = obtener_numero("Ingrese el segundo número: ")
                
                if opcion == "1":
                    resultado = sumar(num1, num2)
                    print(f"Resultado: {num1} + {num2} = {resultado}")
                elif opcion == "2":
                    resultado = restar(num1, num2)
                    print(f"Resultado: {num1} - {num2} = {resultado}")
                elif opcion == "3":
                    resultado = multiplicar(num1, num2)
                    print(f"Resultado: {num1} × {num2} = {resultado}")
                elif opcion == "4":
                    try:
                        resultado = dividir(num1, num2)
                        print(f"Resultado: {num1} ÷ {num2} = {resultado}")
                    except ValueError as e:
                        print(f"Error: {e}")
                elif opcion == "5":
                    resultado = potencia(num1, num2)
                    print(f"Resultado: {num1} ^ {num2} = {resultado}")
            
            elif opcion == "6":
                num = obtener_numero("Ingrese el número: ")
                try:
                    resultado = raiz_cuadrada(num)
                    print(f"Resultado: √{num} = {resultado}")
                except ValueError as e:
                    print(f"Error: {e}")
            
            else:
                print("Opción no válida. Por favor seleccione una opción del 1 al 7.")
        
        except KeyboardInterrupt:
            print("\n\n¡Programa interrumpido por el usuario!")
            break
        except Exception as e:
            print(f"Error inesperado: {e}")

if __name__ == "__main__":
    calculadora()