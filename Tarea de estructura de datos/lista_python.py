from bisect import bisect_left
from pasajero import Pasajero


class ListaPython:
    """Las mismas operaciones usando los métodos del list de Python."""

    def __init__(self):
        self.pasajeros = []

    def añadir(self, pasajero):                      # ✅ resuelto
        if any(p.numero == pasajero.numero for p in self.pasajeros):
            print("  ⚠ Ya existe un pasajero con este número.")
            return False
        self.pasajeros.append(pasajero)
        return True

    def listar(self):                                 # ✅ resuelto
        if not self.pasajeros:
            print("  (lista vacía)")
            return
        for i, p in enumerate(self.pasajeros):
            print(f"  [{i}] {p}")

    # Implementacion de Funciones

    def insertar(self, posicion, pasajero):
        if posicion < 0 or posicion > len(self.pasajeros):
            print("  ⚠ Posición inválida.")
            return False
        if any(p.numero == pasajero.numero for p in self.pasajeros):
            print("  ⚠ Ya existe un pasajero con este número.")
            return False
        self.pasajeros.insert(posicion, pasajero)
        return True

    def buscar(self, numero):
        indices = [i for i, p in enumerate(self.pasajeros) if p.numero == numero]
        return indices[0] if indices else -1

    def buscar_binaria(self, numero):
        # Requiere lista ordenada por número previamente
        numeros = [p.numero for p in self.pasajeros]
        idx = bisect_left(numeros, numero)
        if idx < len(numeros) and numeros[idx] == numero:
            return idx
        return -1

    def modificar(self, numero, nuevo_destino, nuevo_asiento):
        pos = self.buscar(numero)
        if pos == -1:
            return False
        self.pasajeros[pos].destino = nuevo_destino
        self.pasajeros[pos].asiento = nuevo_asiento
        return True

    def eliminar_por_posicion(self, posicion):
        if posicion < 0 or posicion >= len(self.pasajeros):
            return None
        return self.pasajeros.pop(posicion)

    def eliminar_por_valor(self, numero):
        pos = self.buscar(numero)
        if pos == -1:
            return False
        self.pasajeros = [p for p in self.pasajeros if p.numero != numero]
        return True

    def ordenar_asc(self):
        self.pasajeros.sort(key=lambda p: p.numero, reverse=False)

    def ordenar_desc(self):
        self.pasajeros.sort(key=lambda p: p.numero, reverse=True)

    def reversar(self):
        self.pasajeros.reverse()

    def copiar(self):
        nueva = ListaPython()
        nueva.pasajeros = self.pasajeros.copy()
        return nueva

    def longitud(self):
        return len(self.pasajeros)

    def filtrar_por_destino(self, destino):           # solo Lista 2
        return [p for p in self.pasajeros if p.destino.lower() == destino.lower()]

    def mayores_de_edad(self):                        # solo Lista 2
        return [p for p in self.pasajeros if p.es_mayor_de_edad()]