class Natural:
    """Implementacion del TAD Natural"""

    def sucesion(self, numero: float) -> float:
        """Devuelve el siguiente numero natural"""
        return numero + 0.1

    def suma(self, numero1: float, numero2: float) -> float:
        """Devuelve la suma de dos numeros naturales"""
        return numero1 + numero2

    def producto(self, numero1: float, numero2: float) -> float:
        """Devuelve el producto de dos numeros naturales"""
        return numero1 * numero2
    
    def comparacion(self, numero1: float, numero2: float) -> bool:
        """Devuelve True si el primer numero es igual al segundo, False en caso contrario"""
        return numero1 == numero2

if __name__ == "__main__":
    print("Proband el TAD natural")
    print("Valores: 0, 1, 2...")
    print("Operaciones: sucesion, suma, producto y comparacion")

    obj = Natural()
    opcion = -1 #Inicializamos la variable de control

    while opcion != 0:
        print("\nOperaciones:")
        print("1. Sucesion")
        print("2. Suma")
        print("3. Producto")
        print("4. Comparacion")
        print("0. Salir")

        try:
            opcion = int(input("\nIngresa una opcion: "))

            match opcion:
                case 1:
                    print("Ingresa un valor:")
                    n1 = float(input("Valor 1: "))
                    resultado = obj.sucesion(n1)
                    print(f"La sucesion de {n1} es {resultado}")

                case 2:
                    print("Ingresa dos valores:")
                    n1 = float(input("Valor 1: "))
                    n2 = float(input("Valor 2: "))
                    resultado = obj.suma(n1, n2)
                    print(f"La suma de {n1} y {n2} es {resultado}")

                case 3:
                    print("Ingresa dos valores:")
                    n1 = float(input("Valor 1: "))
                    n2 = float(input("Valor 2: "))
                    resultado = obj.producto(n1, n2)
                    print(f"El producto de {n1} y {n2} es {resultado}")

                case 4:
                    print("Ingresa dos valores:")
                    n1 = float(input("Valor 1: "))
                    n2 = float(input("Valor 2: "))
                    resultado = obj.comparacion(n1, n2)
                    print(f"La comparacion de {n1} y {n2} es {resultado}")

                case 0:
                    print("¡¡¡Adios!!!")

                case _: #Equivalente a default
                    print("Opcion no valida")
        except ValueError:
            print("Error: Por favor ingresa un numero entero valido")
        