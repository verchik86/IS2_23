x = int(input('Введите трёхзначное число: '))
s = sum(int(digit) for digit in str(x))
k = s ** 0.5
print(s)
print(k)