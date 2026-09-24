class Comprobar:
    """Implementacion del TAD Comprobar"""
    def menor_igual(self, numero1: int, numero2: int) -> bool:
        """Devuelve True si el primer numero es menor o igual al segundo, False en caso contrario"""
        return numero1 <= numero2

    def menor(self, numero1: int, numero2: int) -> bool:
        """Devuelve True si el primer numero es menor"""
        return numero1 < numero2

    def mayor_igual(self, numero1: int, numero2: int) -> bool:
        """Devuelve True si el primer numero es mayor o igual al segundo, False en caso contrario"""
        return numero1 >= numero2

    def mayor(self, numero1: int, numero2: int) -> bool:
        """Devuelve True si el primer numero es mayor"""
        return numero1 > numero2

if __name__ == "__main__":
        print("Probando el TAD Comprobar")
        print("Valores: 0, 1, 2...")
        print("Operaciones: menor_igual, menor, mayor_igual y mayor")

        obj = Comprobar()
        opcion = -1 #Inicializamos la variable de control

        while opcion != 0:
            print("\nOperaciones:")
            print("1. Menor o igual")
            print("2. Menor")
            print("3. Mayor o igual")
            print("4. Mayor")
            print("0. Salir")

            try:
                opcion = int(input("\nIngresa una opcion: "))

                match opcion:
                    case 1:
                        print("Ingresa dos valores:")
                        n1 = int(input("Valor 1: "))
                        n2 = int(input("Valor 2: "))
                        resultado = obj.menor_igual(n1, n2)
                        print(f"{n1} es menor o igual que {n2}: {resultado}")

                    case 2:
                        print("Ingresa dos valores:")
                        n1 = int(input("Valor 1: "))
                        n2 = int(input("Valor 2: "))
                        resultado = obj.menor(n1, n2)
                        print(f"{n1} es menor que {n2}: {resultado}")

                    case 3:
                        print("Ingresa dos valores:")
                        n1 = int(input("Valor 1: "))
                        n2 = int(input("Valor 2: "))
                        resultado = obj.mayor_igual(n1, n2)
                        print(f"{n1} es mayor o igual que {n2}: {resultado}")

                    case 4:
                        print("Ingresa dos valores:")
                        n1 = int(input("Valor 1: "))
                        n2 = int(input("Valor 2: "))
                        resultado = obj.mayor(n1, n2)
                        print(f"{n1} es mayor que {n2}: {resultado}")

                    case 0:
                        print("Saliendo del programa...")

                    case _:                        
                        print("Opción inválida")

            except ValueError:
                print("Error: Debe ingresar un número entero.")