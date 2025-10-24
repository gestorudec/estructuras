class Nodo:
    def __init__(self, dato):
        self.dato=dato
        self.siguiente=None

class Circular:
    def __init__(self):
        self.primero=None
        self.cont=0
    
    def agregar(self,dato):
        nuevo=Nodo(dato)
        if not self.primero:
            self.primero=nuevo
            nuevo.siguiente=self.primero
        else:
            actual=self.primero
            while actual.siguiente !=self.primero:
               actual=actual.siguiente
               self.cont+=1
            actual.siguiente=nuevo
            nuevo.siguiente=self.primero
            self.cont+=1
               
    def mostrar(self):
        actual=self.primero
        #while actual and actual!=self.primero:
        i=0
        while actual and i< self.cont:
            print(actual.dato)
            actual=actual.siguiente
            i+=1
            
            
k=Circular()
k.agregar(12)
k.agregar(9)
k.agregar(88)
k.agregar(8800)
k.agregar(9988)
k.mostrar()