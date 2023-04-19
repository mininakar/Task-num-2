#Пункт 7
print('Числa Фибоначчи')
n1=1
n2=1
print ('Введите число: ')
number = int(input())

i = 0
while i < (number-2):
    fib_num = n1+n2
    n1 = n2
    n2 = fib_num
    i = i+1

print('Номер ряда =',number,',его значение = ', fib_num)