import random

class Nodo:
    def __init__(self,data,next):
        self.data=data
        self.next=next

tam=random.randint(5, 10)
head=Nodo(None,None)
for i in range(tam):
    data=random.randint(0,100)
    head=Nodo(data,head)

while head.next!=None:
    print(head.data)
    head=head.next