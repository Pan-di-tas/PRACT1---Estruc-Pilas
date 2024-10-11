class PilaPrac:
    def __init__(self, tamaño):
        self.stack = [] 
        self.tamaño = tamaño_max 
        self.tope = 0 

    def esta_llena(self):
        if self.tope == self.tamaño:
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

pila.insertar("X") 
pila.insertar("Y") 
pila.eliminar()
pila.eliminar()    
pila.eliminar()  
pila.insertar("V")  
pila.insertar("W") 
pila.eliminar()    
pila.insertar("R") 
