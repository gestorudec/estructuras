class Nodo:
    def __init__(self, dato):
        self.dato=dato
        self.siguiente=None
    # def __str__(self):
    #     pass
        
a1=Nodo('a')
b1=Nodo('b')
if not a1:
    print("existe")
a1=None
if a1:
    print("existe")
else:
    print("NO ...existe")