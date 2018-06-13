Factorial = 1

for i in range(1, 101):
    Factorial *= i

print(Factorial)

Sum = sum(list(map(int, str(Factorial))))

print(Sum)
