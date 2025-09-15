import random
cantidad=random.randint(5, 15)
print(f'cantidad={cantidad}')
vector=[]
for i in range(cantidad):
    vector.append(random.randint(1, 100))    
print(vector)

#posiciones_pares=[i+1 for i num in enumerate(vector) if num==]

sumapares=0
for num in vector:
    if num%2==0:
        sumapares+=num
print(sumapares)        