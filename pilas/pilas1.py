class Pila:
    def __init__(self):
        self. elementos=[]

    def poner_top(self,dato):
        self.elementos.append(dato)
        return None
    
    def quitar(self):
        if len(self.elementos)!=0:
            self.elementos.pop()
    
    def ver_tope(self):
        if len(self.elementos)!=0:
            return self.elementos[-1]
    
    def mostrar(self):
        print(self.elementos)

    def get_lista(self):
        return self.elementos
    
mipila=Pila()
mipila.poner_top(100)
mipila.poner_top(300)
mipila.poner_top(500)
mipila.poner_top(200)
mipila.poner_top(400)
mipila.mostrar()
print(mipila.ver_tope())
mipila.quitar()
mipila.mostrar()
print(mipila.ver_tope())

def tipo_dato_tope(pila):
    print(type(pila.ver_tope()))


tipo_dato_tope(mipila)