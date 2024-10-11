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
            print(f"No se puede Insertar {elemento}: Pila llena.")
        else:
            self.Pila.append(elemento) 
            self.tope += 1  
            print(f"Insertando: {elemento}. Pila actual: {self.Pila}")

    def Eliminar(self):
        if self.Pila_Vacia():
            print("No se puede Eliminar: La pila ya está vacía.")
        else:
            elemento = self.Pila.pop()        
            self.tope -= 1
            print(f"Eliminando: {elemento}. Pila actual: {self.Pila}")

pila = PilaPrac(8)

pila.Insertar("X") 
pila.Insertar("Y") 
pila.Eliminar()
pila.Eliminar()    
pila.Eliminar()  
pila.Insertar("V")  
pila.Insertar("W") 
pila.Eliminar()    
pila.Insertar("R") 
