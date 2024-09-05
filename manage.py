print('a = ')
a=input()
print('b = ')
b = input()
if a > b:
    print('a больше чем b')
else:
    print('b больше a')

print('x = ')
x = int(input())
if x > 0 or x == 0:
    y = 2*x-1
elif x < 0:
    y=x**2
print('y = ', y)

