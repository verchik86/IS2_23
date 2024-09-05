x = int(input("Введите число: "))
p = int(input("Введите число: "))
y = int(input())
i = 0

while x < y:
    x *= 1 + p / 100
    x = int(100 * x) / 100
    i += 1

print(i)