class PilaPrac:
    def __init__(self, max_size):
        self.stack = [] 
        self.max_size = max_size 
        self.tope = 0 

    def esta_llena(self):
        if self.tope == self.max_size:
            return True
        else:
            return False

    def esta_vacia(self):
        if self.tope == 0:
            return True
        else:
            return False

    def insertar(self, elemento):
        if self.esta_llena():
            print(f"No se puede insertar {elemento}: Pila llena.")
        else:
            self.stack.append(elemento) 
            self.tope += 1  
            print(f"Insertado: {elemento}. Pila ahora: {self.stack}")

    def eliminar(self):
        if self.esta_vacia():
            print("No se puede eliminar: La pila ya está vacía.")
        else:
            elemento = self.stack.pop()        
            self.tope -= 1
            print(f"Eliminado: {elemento}. Pila ahora: {self.stack}")

pila = PilaPrac(8)

pila.insertar("X")  # Inserta X
pila.insertar("Y")  # Inserta Y
pila.eliminar()     # Elimina el último (Y)
pila.eliminar()     # Elimina el último (X)
pila.eliminar()     # Error, la pila está vacía (subdesbordamiento)
pila.insertar("V")  # Inserta V
pila.insertar("W")  # Inserta W
pila.eliminar()     # Elimina el último (W)
pila.insertar("R")  # Inserta R

# Al final, la pila debe contener "V" y "R"