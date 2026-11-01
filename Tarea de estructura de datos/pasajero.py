class Pasajero:
    """Representa a un pasajero de la aerolínea."""

    def __init__(self, numero, nombre, cedula, edad, fecha_vuelo, destino, asiento):
        self.numero = numero              # int -> 1002  (clave única)
        self.nombre = nombre              # str -> "Ana"
        self.cedula = cedula              # str -> "0912345678"
        self.edad = edad                  # int -> 28
        self.fecha_vuelo = fecha_vuelo    # str -> "2026-11-15"
        self.destino = destino            # str -> "Lima"
        self.asiento = asiento            # str -> "03C"

    def es_mayor_de_edad(self):
        return self.edad >= 18

    def __str__(self):
        return (f"#{self.numero} | {self.nombre:<8} | {self.cedula} | {self.edad:>2} años | "
                f"{self.fecha_vuelo} | {self.destino:<7} | asiento {self.asiento}")

# --- CÓDIGO DE PRUEBA INDEPENDIENTE ---
if __name__ == "__main__":
    print("--- PROBANDO EL ARCHIVO PASAJERO.PY ---")
    
    # Creamos un pasajero de prueba
    p1 = Pasajero(1001, "Josue", "0901234567", 21, "2026-11-22", "Lima", "01A")
    
    # Probamos el método __str__ (impresión)
    print("Objeto creado:")
    print(p1)
    
    # Probamos el método es_mayor_de_edad()
    print("¿Es mayor de edad?", p1.es_mayor_de_edad())