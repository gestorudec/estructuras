def promedio(n1,n2,n3):
    nota=(n1+n2+n3)/3
    #return nota
    print(nota)

def ciclo(ini,fin):
    suma=0
    for i in range(ini,fin,1):
        print(i)
        suma+=i        
    for i in range(ini,fin,-1):
        print(i)
        suma+=i
    return suma

print(ciclo(1,6))
    

# promedio(5,6,7)
# print()
# print("hola")