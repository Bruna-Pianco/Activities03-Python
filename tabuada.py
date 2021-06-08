# a = int(input('digite:'))
# b = int(input('digite:'))
# x = 1
# y = 1

# if a < b :
#       print('Nenhuma tabuada no intervalo!') 
# while x <= 10:
#     print(f'''{a} x {x} = {a*x}''')
#     x = x + 1
# print('----------')
# while y <= 10:
#     print(f'''{b} x {y} = {b*y}''')
#     y = y + 1
# print('----------')



# a = int(input())
# b = int(input())
# x = 0

# for num in range(1,11):
#     if a > b :
#         print('Nenhuma tabuada no intervalo!') 
#     elif a == b:     
#         print(f'{a} x {num} = {a*num}')
#     else:
#         print(f'{b} x {num} = {b*num}')
#     print('----------') 
# for num in range(1+1,11):
#     print(f'{b} x {num} = {b*num}')
# print('----------')  

a = int(input())
b = int(input())

if a > b:
    print ('Nenhuma tabuada no intervalo!')
else:    
    for num in range (a, b+1):
        for numero in range(1,11):
            print(f'{num} x {numero} = {num*numero}')
        print('-'*10)   

   






