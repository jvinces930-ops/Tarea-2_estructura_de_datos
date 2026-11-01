from pasajero import Pasajero


class MiLista:
    """Lista construida a mano sobre un arreglo de tamaño fijo.
    datos     -> [p1, p2, p3, None, None, ...]
    capacidad -> total de cajones     cantidad -> cajones ocupados
    ⛔ Sin append, insert, pop, remove, sort, reverse, copy, len, in, slicing.
    """

    def __init__(self, capacidad=10):
        self.datos = [None] * capacidad
        self.capacidad = capacidad
        self.cantidad = 0

    def añadir(self, pasajero):                      # ✅ resuelto
        if self.cantidad == self.capacidad:
            print("  ⚠ La lista está llena")
            return False
        # Validación opcional para evitar números de pasajero duplicados
        if self.buscar(pasajero.numero) != -1:
            print("  ⚠ Ya existe un pasajero con este número.")
            return False
        self.datos[self.cantidad] = pasajero          # primer cajón libre
        self.cantidad = self.cantidad + 1
        return True

    def listar(self):                                 # ✅ resuelto
        if self.cantidad == 0:
            print("  (lista vacía)")
            return
        for i in range(self.cantidad):
            print(f"  [{i}] {self.datos[i]}")

    # ---------------- ✍ IMPLEMENTACIÓN DE MÉTODOS ----------------
    def insertar(self, posicion, pasajero):
        if posicion < 0 or posicion > self.cantidad:
            print("  ⚠ Posición inválida.")
            return False
        if self.cantidad == self.capacidad:
            print("  ⚠ La lista está llena.")
            return False
        if self.buscar(pasajero.numero) != -1:
            print("  ⚠ Ya existe un pasajero con este número.")
            return False
        
        # Desplazar elementos hacia la derecha de atrás hacia adelante
        i = self.cantidad
        while i > posicion:
            self.datos[i] = self.datos[i - 1]
            i = i - 1
            
        self.datos[posicion] = pasajero
        self.cantidad = self.cantidad + 1
        return True

    def buscar(self, numero):
        i = 0
        while i < self.cantidad:
            if self.datos[i].numero == numero:
                return i
            i = i + 1
        return -1

    def buscar_binaria(self, numero):
        izq = 0
        der = self.cantidad - 1
        while izq <= der:
            medio = (izq + der) // 2
            if self.datos[medio].numero == numero:
                return medio
            elif self.datos[medio].numero < numero:
                izq = medio + 1
            else:
                der = medio - 1
        return -1

    def modificar(self, numero, nuevo_destino, nuevo_asiento):
        pos = self.buscar(numero)
        if pos == -1:
            return False
        self.datos[pos].destino = nuevo_destino
        self.datos[pos].asiento = nuevo_asiento
        return True

    def eliminar_por_posicion(self, posicion):
        if posicion < 0 or posicion >= self.cantidad:
            return None
        
        pasajero_eliminado = self.datos[posicion]
        
        # Desplazar elementos a la izquierda
        i = posicion
        while i < self.cantidad - 1:
            self.datos[i] = self.datos[i + 1]
            i = i + 1
            
        self.datos[self.cantidad - 1] = None
        self.cantidad = self.cantidad - 1
        return pasajero_eliminado

    def eliminar_por_valor(self, numero):
        pos = self.buscar(numero)
        if pos == -1:
            return False
        eliminado = self.eliminar_por_posicion(pos)
        return eliminado is not None

    def ordenar_asc(self):
        # Algoritmo de burbuja
        i = 0
        while i < self.cantidad - 1:
            j = 0
            while j < self.cantidad - i - 1:
                if self.datos[j].numero > self.datos[j + 1].numero:
                    aux = self.datos[j]
                    self.datos[j] = self.datos[j + 1]
                    self.datos[j + 1] = aux
                j = j + 1
            i = i + 1

    def ordenar_desc(self):
        # Burbuja cambiando un solo símbolo (>) a (<)
        i = 0
        while i < self.cantidad - 1:
            j = 0
            while j < self.cantidad - i - 1:
                if self.datos[j].numero < self.datos[j + 1].numero:
                    aux = self.datos[j]
                    self.datos[j] = self.datos[j + 1]
                    self.datos[j + 1] = aux
                j = j + 1
            i = i + 1

    def reversar(self):
        izq = 0
        der = self.cantidad - 1
        while izq < der:
            aux = self.datos[izq]
            self.datos[izq] = self.datos[der]
            self.datos[der] = aux
            izq = izq + 1
            der = der - 1

    def copiar(self):
        nueva = MiLista(self.capacidad)
        i = 0
        while i < self.cantidad:
            # Creamos una copia superficial o el mismo objeto pasajero
            p = self.datos[i]
            copia_p = Pasajero(p.numero, p.nombre, p.cedula, p.edad, p.fecha_vuelo, p.destino, p.asiento)
            nueva.añadir(copia_p)
            i = i + 1
        return nueva

    def longitud(self):
        return self.cantidad
   

if __name__ == "__main__":
    print("--- PROBANDO MI_LISTA.PY ---")
    
    # 1. Creamos una lista manual con capacidad para 5 pasajeros
    mi_prueba = MiLista(5)
    
    # 2. Creamos un par de pasajeros de prueba
    p1 = Pasajero(1001, "Elena", "0901234567", 41, "2026-11-22", "Lima", "01A")
    p2 = Pasajero(1002, "Ana", "0912345678", 28, "2026-11-15", "Lima", "03C")
    
    # 3. Probamos el método añadir
    print("Añadiendo pasajeros...")
    mi_prueba.añadir(p1)
    mi_prueba.añadir(p2)
    
    # 4. Probamos el método listar
    print("\nEstado actual de la lista:")
    mi_prueba.listar()
    
    # 5. Probamos el método longitud
    print(f"\nLongitud de la lista: {mi_prueba.longitud()}")
    
    # 6. Probamos el método buscar
    pos = mi_prueba.buscar(1002)
    print(f"Buscando al pasajero 1002: Encontrado en la posición [{pos}]")