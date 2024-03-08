#Laboratorio 12 y 13
# ejercicio parte 01 - colas
# ejercicio 02

"""Diseño de un sistema de gestión de pedidos
2. Crea un sistema de gestión de pedidos que utilice una cola para procesar los pedidos en el orden en que
fueron recibidos. Implementa funciones para agregar pedidos, procesar pedidos y mostrar el estado
actual de la cola. """

class Cola:
    def __init__(self):
        self.pedidos = []

    def esta_vacia(self):
        return len(self.pedidos) == 0

    def agregar_pedido(self, pedido):
        self.pedidos.append(pedido)

    def procesar_pedido(self):
        if self.esta_vacia():
            print("No hay pedidos para procesar.")
        else:
            pedido = self.pedidos.pop(0)
            print("Procesando pedido:", pedido)

    def mostrar_estado(self):
        if self.esta_vacia():
            print("La cola de pedidos está vacía.")
        else:
            print("Pedidos en cola:", self.pedidos)

cola_pedidos = Cola()

cola_pedidos.agregar_pedido("Pedido 1")
cola_pedidos.agregar_pedido("Pedido 2")
cola_pedidos.agregar_pedido("Pedido 3")

cola_pedidos.mostrar_estado()

cola_pedidos.procesar_pedido()
cola_pedidos.procesar_pedido()

cola_pedidos.mostrar_estado()
