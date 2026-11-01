from pasajero import Pasajero
from mi_lista import MiLista
from lista_python import ListaPython

lista1 = MiLista(10)
lista2 = ListaPython()


# ------------------------- funciones de apoyo ✅ -------------------------
def leer_entero(mensaje):
    while True:
        try:
            return int(input(mensaje))
        except ValueError:
            print("  Debe ser un número entero.")


def leer_pasajero():
    numero = leer_entero("  N.º de pasajero: ")
    nombre = input("  Nombre: ").strip()
    cedula = input("  Cédula: ").strip()
    edad = leer_entero("  Edad: ")
    fecha = input("  Fecha de vuelo (AAAA-MM-DD): ").strip()
    destino = input("  Destino: ").strip()
    asiento = input("  Asiento: ").strip().upper()
    return Pasajero(numero, nombre, cedula, edad, fecha, destino, asiento)



def mostrar_opciones(titulo, extras=False):
    print(f"\n========== {titulo} ==========")
    print(" 1. Añadir           2. Listar            3. Insertar en posición")
    print(" 4. Buscar (lineal)  5. Buscar (binaria)  6. Modificar")
    print(" 7. Eliminar por posición                 8. Eliminar por número")
    print(" 9. Ordenar asc     10. Ordenar desc     11. Reversar")
    print("12. Copiar          13. Longitud")
    if extras:
        print("14. Filtrar por destino                  15. Mayores de edad")
    print("0. Volver")


# ---------------------- MENÚ 1 · MiLista ----------------------
def menu_lista1():
    while True:
        mostrar_opciones("MENÚ 1 · MiLista")
        op = input("Opción: ").strip().upper()

        if op == "1":
            pasajero = leer_pasajero()
            if lista1.añadir(pasajero):
                print("  ✓ Pasajero añadido")
        elif op == "2":
            lista1.listar()
        elif op == "3":
            pos = leer_entero("  Posición donde insertar: ")
            p = leer_pasajero()
            if lista1.insertar(pos, p):
                print("  ✓ Pasajero insertado correctamente")
        elif op == "4":
            num = leer_entero("  N.º de pasajero a buscar: ")
            pos = lista1.buscar(num)
            if pos != -1:
                print(f"  ✓ Encontrado en [{pos}]: {lista1.datos[pos]}")
            else:
                print("  ❌ Pasajero no encontrado")
        elif op == "5":
            num = leer_entero("  N.º de pasajero a buscar (binaria): ")
            pos = lista1.buscar_binaria(num)
            if pos != -1:
                print(f"  ✓ Encontrado en [{pos}]: {lista1.datos[pos]}")
            else:
                print("  ❌ Pasajero no encontrado (recuerde ordenar la lista antes)")
        elif op == "6":
            num = leer_entero("  N.º de pasajero a modificar: ")
            dest = input("  Nuevo destino: ").strip()
            asiento = input("  Nuevo asiento: ").strip().upper()
            if lista1.modificar(num, dest, asiento):
                print("  ✓ Pasajero modificado con éxito")
            else:
                print("  ❌ No se encontró el pasajero")
        elif op == "7":
            pos = leer_entero("  Posición a eliminar: ")
            eliminado = lista1.eliminar_por_posicion(pos)
            if eliminado:
                print(f"  ✓ Eliminado correctamente: {eliminado}")
            else:
                print("  ❌ Posición inválida")
        elif op == "8":
            num = leer_entero("  N.º de pasajero a eliminar: ")
            if lista1.eliminar_por_valor(num):
                print("  ✓ Pasajero eliminado correctamente")
            else:
                print("  ❌ No se encontró el pasajero")
        elif op == "9":
            lista1.ordenar_asc()
            print("  ✓ Lista ordenada de forma ascendente")
        elif op == "10":
            lista1.ordenar_desc()
            print("  ✓ Lista ordenada de forma descendente")
        elif op == "11":
            lista1.reversar()
            print("  ✓ Lista invertida")
        elif op == "12":
            copia = lista1.copiar()
            print("  ✓ Copia de la lista creada con éxito. Contenido de la copia:")
            copia.listar()
        elif op == "13":
            print(f"  Longitud de la lista: {lista1.longitud()}")
        elif op == "0":
            break
        else:
            print("  Opción no válida")


# ---------------------- MENÚ 2 · list de Python ----------------------
def menu_lista2():
    while True:
        mostrar_opciones("MENÚ 2 · list de Python", extras=True)
        op = input("Opción: ").strip().upper()

        if op == "1":
            pasajero = leer_pasajero()
            if lista2.añadir(pasajero):
                print("  ✓ Pasajero añadido")
        elif op == "2":
            lista2.listar()
        elif op == "3":
            pos = leer_entero("  Posición donde insertar: ")
            p = leer_pasajero()
            if lista2.insertar(pos, p):
                print("  ✓ Pasajero insertado correctamente")
        elif op == "4":
            num = leer_entero("  N.º de pasajero a buscar: ")
            pos = lista2.buscar(num)
            if pos != -1:
                print(f"  ✓ Encontrado en [{pos}]: {lista2.pasajeros[pos]}")
            else:
                print("  ❌ Pasajero no encontrado")
        elif op == "5":
            num = leer_entero("  N.º de pasajero a buscar (binaria): ")
            pos = lista2.buscar_binaria(num)
            if pos != -1:
                print(f"  ✓ Encontrado en [{pos}]: {lista2.pasajeros[pos]}")
            else:
                print("  ❌ Pasajero no encontrado (recuerde ordenar la lista antes)")
        elif op == "6":
            num = leer_entero("  N.º de pasajero a modificar: ")
            dest = input("  Nuevo destino: ").strip()
            asiento = input("  Nuevo asiento: ").strip().upper()
            if lista2.modificar(num, dest, asiento):
                print("  ✓ Pasajero modificado con éxito")
            else:
                print("  ❌ No se encontró el pasajero")
        elif op == "7":
            pos = leer_entero("  Posición a eliminar: ")
            eliminado = lista2.eliminar_por_posicion(pos)
            if eliminado:
                print(f"  ✓ Eliminado correctamente: {eliminado}")
            else:
                print("  ❌ Posición inválida")
        elif op == "8":
            num = leer_entero("  N.º de pasajero a eliminar: ")
            if lista2.eliminar_por_valor(num):
                print("  ✓ Pasajero eliminado correctamente")
            else:
                print("  ❌ No se encontró el pasajero")
        elif op == "9":
            lista2.ordenar_asc()
            print("  ✓ Lista ordenada de forma ascendente")
        elif op == "10":
            lista2.ordenar_desc()
            print("  ✓ Lista ordenada de forma descendente")
        elif op == "11":
            lista2.reversar()
            print("  ✓ Lista invertida")
        elif op == "12":
            copia = lista2.copiar()
            print("  ✓ Copia de la lista creada con éxito. Contenido de la copia:")
            copia.listar()
        elif op == "13":
            print(f"  Longitud de la lista: {lista2.longitud()}")
        elif op == "14":
            dest = input("  Ingrese destino a filtrar: ").strip()
            filtrados = lista2.filtrar_por_destino(dest)
            if filtrados:
                print(f"  --- Pasajeros con destino a {dest} ---")
                for p in filtrados:
                    print(f"  {p}")
            else:
                print("  No hay pasajeros para ese destino.")
        elif op == "15":
            mayores = lista2.mayores_de_edad()
            if mayores:
                print("  --- Pasajeros Mayores de Edad ---")
                for p in mayores:
                    print(f"  {p}")
            else:
                print("  No hay pasajeros mayores de edad.")
        elif op == "0":
            break
        else:
            print("  Opción no válida")


# ---------------------- MENÚ PRINCIPAL ✅ ----------------------
def main():
    while True:
        print("\n===== TAREA LISTAS · PASAJEROS ✈ =====")
        print("1. Menú 1 · MiLista")
        print("2. Menú 2 · list de Python")
        print("3. Salir")
        op = input("Opción: ").strip()
        if op == "1":
            menu_lista1()
        elif op == "2":
            menu_lista2()
        elif op == "3":
            print("¡Hasta pronto!")
            break
        else:
            print("Opción no válida")


if __name__ == "__main__":
    main()