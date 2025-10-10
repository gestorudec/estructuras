class Persona:
    def __init__(self, nombre, doc):
        self.nombre=nombre
        self.doc=doc
    def __str__(self):
        return self.nombre

objeto=Persona('Maria',123)
print(objeto)

lista=[]
print(type(lista))
lista.append(123)
lista.append('rrrr')
lista.append([])
print(lista)
lista.remove(12)
print(lista)