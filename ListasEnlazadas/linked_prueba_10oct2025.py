class Node:
    def __init__(self,value):
        self.value=value
        self.next=None
    def __str__(self):
        return str(self.value)

class LinkedList:
    def __init__(self):
        self.first=None
        self.size=0
        
    def append(self, value):        
        nuevo_nodo=Node(value)        
        if self.size==0:
            self.first=nuevo_nodo    
        else:
            actual=self.first                            
            while actual.next !=None:               
                actual=actual.next                               
            actual.next=nuevo_nodo            
        self.size+=1        
        return nuevo_nodo
    
    def get_first(self):
        return self.first
    
    
    def remove(self, value):
        if self.size==0:
           return False
        else:
            actual=self.first
            try:
                while actual.next.value != value:
                    actual=actual.next
                
                nodo_saliente=actual.next                
                actual.next=nodo_saliente.next
            except AttributeError:
                return False
            self.size-=1
            return nodo_saliente
        
    def __len__(self):
        return self.size
    
    def __str__(self):
        String="["
        actual=self.first
        while actual!=None:
            String+=str(actual)
            String+=str(",")
            actual=actual.next
        String+="]"
        return String

Mylist=LinkedList()
Mylist.append(100)
Mylist.append("z")
Mylist.append("tres")
Mylist.append(250)
Mylist.append("hola")
print(Mylist)
                         
                                    
# Mylist=LinkedList()
# Mylist.append(1)
# Mylist.append(2)
# Mylist.append(3)
# Mylist.append(4)
# Mylist.append(5)
# print(Mylist)
# Mylist.remove(3)
# print(Mylist)
            
        