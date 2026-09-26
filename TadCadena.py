class Cadena:
    """Implentacion del TAD Cadena (String)"""

    def concatenar(self, cadena1: str, cadena2: str) -> str:
        """Devuelve la concatenacion de dos cadenas"""
        return cadena1 + cadena2

    def Longitud(self, cadena: str) -> int:
        """Devuelve la longitud de una cadena"""
        return len(cadena)

    def es_vacia(self, cadena: str) -> bool:
        """Devuelve True si la cadena es vacia, False en caso contrario"""
        return len(cadena) == 0

    def son_iguales(self, cadena1: str, cadena2: str) -> bool:
        """Devuelve True si las cadenas son iguales, False en caso contrario"""
        return cadena1 == cadena2

if __name__ == "__main__":
    cadena = Cadena()
    print(cadena.concatenar("Holo", " Mundo"))
    print(cadena.Longitud("Hola Mundo"))
    print(cadena.es_vacia(""))
    print(cadena.son_iguales("Hola", "Hola"))

    obj = Cadena()
    opcion = -1
    while opcion != 0:
        print("1. Concatenar")
        print("2. Longitud")
        print("3. Es vacia")
        print("4. Son iguales")
        print("0. Salir")
        try:
            opcion = int(input("Ingrese una opcion: "))
            match opcion:
                case 1:
                    cadena1 = input("Ingrese la primera cadena: ")
                    cadena2 = input("Ingrese la segunda cadena: ")
                    print("Resultado:", obj.concatenar(cadena1, cadena2))
                case 2:
                    cadena = input("Ingrese una cadena: ")
                    print("Longitud:", obj.Longitud(cadena))
                case 3:
                    cadena = input("Ingrese una cadena: ")
                    print("Es vacía:", obj.es_vacia(cadena))
                case 4:
                    cadena1 = input("Ingrese la primera cadena: ")
                    cadena2 = input("Ingrese la segunda cadena: ")
                    print("Son iguales:", obj.son_iguales(cadena1, cadena2))
                case 0:
                    print("Saliendo del programa...")
                case _:
                    print("Opción inválida")
        except ValueError:
            print("Error: Debe ingresar un número entero.")
            