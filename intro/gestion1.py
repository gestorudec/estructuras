x=int(input('ingrese numero'))
if x>0:
    print('positivo')
elif x<0:
    print('negativo')
else:
    print('neutro')

estrato=6
match estrato:
    case 1:
        print("descuento 50%")    
    case 2:
        print("descuento 40%")    
    case 3:
        print("descuento 30%")    
    case _:
        print("opcion errada")
