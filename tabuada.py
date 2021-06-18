a = int(input())
b = int(input())

if a > b:
    print ('Nenhuma tabuada no intervalo!')
else:    
    for num in range (a, b+1):
        for numero in range(1,11):
            print(f'{num} x {numero} = {num*numero}')
        print('-'*10)   

#correção

a = int(input())
b = int(input())

if a <= b:
    for multiplicando in range(a,b+1):
        for multiplicador in range(1,11):
            produto = multiplicando*multiplicador
            print(f'{multiplicando} x {multiplicador} = {produto}')
        print(10* '-') 
else:   
    print ('Nenhuma tabuada no intervalo!')        

#correção2
a = int(input())
b = int(input())

if a <= b:
    for multiplicando in range(a,b+1):
        for multiplicador in range(1,11):
            produto = multiplicando*multiplicador
            print(f'{multiplicando} x {multiplicador} = {produto}')
        print(10* '-') 
else:   
    print ('Nenhuma tabuada no intervalo!')     




