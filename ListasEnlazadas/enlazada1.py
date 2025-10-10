class Nodo:
    def __init__(self,data,next):
        self.data=data
        self.next=next

n=Nodo(12345,None)
print(n)
print(n.data)
print(n.next)

n0=Nodo(None,None)
#n0=None
n1=Nodo("San Mateo",n0)
n2=Nodo("Terreros",n1)
n3=Nodo("Bosa",n2)
n4=Nodo("Venecia",n3)
n5=Nodo("Gral Santander",n4)

nodito=n5
while nodito.next != None:
    print(nodito.data)
    nodito=nodito.next
    