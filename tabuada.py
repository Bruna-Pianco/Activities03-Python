a = int(input())
b = int(input())

if a > b:
    print ('Nenhuma tabuada no intervalo!')
else:    
    for num in range (a, b+1):
        for numero in range(1,11):
            print(f'{num} x {numero} = {num*numero}')
        print('-'*10)   

   






