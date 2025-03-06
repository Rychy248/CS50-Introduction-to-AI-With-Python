import sys

class Node():
    def __init__(self, estado, padre, accion):
        self.estado = estado
        self.padre = padre
        self.accion = accion

class PilaFrontera():
    def __init__(self):
        self.frontera = []  # Corregido: inicializar la frontera como una lista vacía.
        
    def add(self, nodo):
        self.frontera.append(nodo)
    
    def comprobar_estado(self, estado):
        return any(nodo.estado == estado for nodo in self.frontera)
    
    def empty(self):
        return len(self.frontera) == 0
    
    def removerFrontera(self):
        if self.empty():
            raise Exception("Empty frontera")
        else:
            nodo = self.frontera[-1]
            self.frontera = self.frontera[:-1]
            return nodo

class QFrontera(PilaFrontera):
    def remover(self):
        if self.empty():
            raise Exception("Empty QFrontera")
        else:
            nodo = self.frontera[0]
            self.frontera = self.frontera[1:]
            return nodo

# Ejemplo de uso
if __name__ == "__main__":
    # Crear nodos
    nodo1 = Node("estado1", None, "acción1")
    nodo2 = Node("estado2", nodo1, "acción2")
    
    # Usar PilaFrontera
    pila = PilaFrontera()
    pila.add(nodo1)
    pila.add(nodo2)
    
    print("Estado del último nodo en la pila:", pila.removerFrontera().estado)
    
    # Usar QFrontera
    cola = QFrontera()
    cola.add(nodo1)
    cola.add(nodo2)
    
    print("Estado del primer nodo en la cola:", cola.remover().estado)