class PilaPrac:
    def __init__(self, tamaño_max):
        self.Pila = [] 
        self.tamaño = tamaño_max 
        self.tope = 0 

    def Pila_Llena(self):
        if self.tope == self.tamaño:
            return True
        else:
            return False

    def Pila_Vacia(self):
        if self.tope == 0:
            return True
        else:
            return False

    def Insertar(self, elemento):
        if self.Pila_Llena():
            print(f"No se puede insertar {elemento}: Pila llena.")
        else:
            self.Pila.append(elemento) 
            self.tope += 1  
            print(f"Insertado: {elemento}. Pila ahora: {self.Pila}")

    def Eliminar(self):
        if self.Pila_Vacia():
            print("No se puede eliminar: La pila ya está vacía.")
        else:
            elemento = self.Pila.pop()        
            self.tope -= 1
            print(f"Eliminado: {elemento}. Pila ahora: {self.Pila}")

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
