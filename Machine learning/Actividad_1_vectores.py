
#Integrantes
"""
-	CRISTIAN CAMILO VEGA MORALES
-	DIDIER DAVID SANTAMARIA BENITEZ
-	DUMAR SULVARAN JIMENEZ
-	ALEX FERNEY RONDON CALDERON
-	WILVER JULIAN MARTIN JIMENEZ.

"""

# Declarar vector
can, ref, total = [], [], []
T = 5  # Días de la semana (lunes a viernes)

def inicializar():
    for i in range(T):
        can.append([0] * T)  # Cambio en la inicialización de "can" para almacenar las ventas por referencia y día
        ref.append(0)
        total.append(0)
    print("El vector de cantidades:", can)
    print("El vector de referencia:", ref)
    print("El vector total:", total)

def captura():
    for i in range(T):
        for j in range(T):
            can[i][j] = int(input(f"Digite la cantidad de ventas de la referencia {i+1} en el dia {j+1}: "))
    return can

def referencias():
    for i in range(T):
        ref[i] = int(input(f"Digite el valor de ventas de la referencia {i+1} de papa frita: "))
    return ref

def costos(can, ref):
    for i in range(T):
        total[i] = sum(can[i]) * ref[i]  # Cambio en el cálculo del total para tener en cuenta las ventas por referencia y día
    return total

def mostrar(can, ref, total):
    tgc = 0
    tgv = 0
    print("Ventas por referencia y dia:")
    for i in range(T):
        for j in range(T):
            print(f"Referencia {i+1}, Dia {j+1}: {can[i][j]}")
    print("Ventas totales por referencia:")
    for i in range(T):
        print(f"Referencia {i+1}: {sum(can[i])}")
    print("Ventas totales en dinero de papas fritas por referencia:")
    for i in range(T):
        print(f"Referencia {i+1}: {total[i]}")
        tgc += sum(can[i])
        tgv += total[i]
    print("Las ventas totales en unidades de papas fritas es de", tgc)
    print("Las ventas totales en dinero de papas fritas es de", tgv)

def titulo():
    print("Empresa Margarita")

def salir():
    print("CHAO")

def main():
    titulo()
    inicializar()
    can = captura()
    ref = referencias()
    total = costos(can, ref)
    mostrar(can, ref, total)
    max_venta = max(total)
    min_venta = min(total)
    ref_max = total.index(max_venta) + 1
    ref_min = total.index(min_venta) + 1
    print("La venta mayor fue de la referencia", ref_max, "por un valor de", max_venta)
    print("La venta menor fue de la referencia", ref_min, "por un valor de", min_venta)
    salir()

# Bloque principal
main()
