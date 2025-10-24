class Nodo():
    def __init__(self,dato):
        self.dato=dato
        self.siguiente=None


class Lista:
    #El constructor genera un atributo que representa el
    #primer nodo de la lista
    #Siempre se recorre desde el primer nodo
    #Cada vez que se agrega un nodo nuevo
    def __init__(self):
        self.primero=None
        
    def agregar(self,dato):
#Se instancia un nuevo nodo         
        nuevo=Nodo(dato)
        #
        if not self.primero:
            self.primero=nuevo
        else:
            actual=self.primero            
            while actual.siguiente:
                actual=actual.siguiente
            actual.siguiente=nuevo            
        return 1 
    
    def eliminar(self,dato):
        actual=self.primero
        anterior=None
        while actual and actual.dato!=dato:
            anterior=actual
            actual=actual.siguiente
        if not actual:
            return
        if not anterior:
            self.primero=actual.siguiente
        else:
            anterior.siguiente=actual.siguiente 
            
    
    def imprimir(self):
        actual=self.primero
        while actual:
            print(actual.dato)
            actual=actual.siguiente

lili=Lista()
#print(type(lili))
lili.agregar('k')
lili.agregar(999)
lili.agregar(1000)

# l1.agregar(111)
# l1.eliminar(1112)
# l1.imprimir()
# l1.agregar(111)
# l1.agregar(333)
# l1.agregar(444)
# l1.imprimir()
# print("="*50)
# l1.eliminar(111)
# l1.imprimir()

                               
        


# a=Nodo(1)
# a=None
# if a:
#     print('hay nodo')
# else:

#     print('no nodo')
#class ListaEnlazada:
    
#lista=[1,2,3,2,5]
# print(lista)
# lista.remove(12)
# print(lista)
    