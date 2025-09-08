#in range
for i in range(100,-1,-5):
    #print(f"{i*i}")
    print(i)
suma=0
for i in range(1,21):
    suma+=i

print(f"total={suma}")

num=0
cont=0
while num!=0:
    num=int(input('ingrese numero'))
    cont+=1
else:
    print("fin del programa")
print(f"ingreso {cont} cantidad de numeros")


for i in range(1,10,1):
    print(i,end=', ')
    
c=0
while True:    
    if c<5:
        c+=1
        
    else:
        break
    print(c) 