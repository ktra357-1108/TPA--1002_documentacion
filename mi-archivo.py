def saludar(nombre):
    print(f"Hola", {nombre}, ", bienvenido al ejercicio de github.")

def sumar(a, b):
    resultado = a + b
    print(f"el resultado de la suma de {a} + {b} es igual: {resultado}")

def main():
    print("Hola mundo desde Python")
    saludar("nombre")
    sumar(5, 3)

if __name__ == "__main__":
    main()
