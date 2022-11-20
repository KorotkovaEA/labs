n = int(input('Введите количество значений:'))
a = {}
b = [0] * 2 * n
for i in range(0,2 * n, 2):
    b[i] = input('Введите ключ:')
for i in range(1, 2 * n, 2):
    b[i] = input('Введите значение:')
for i in range(0, 2 * n, 2):
    a[b[i]] = b[i+1]
print(a)
h = input('Введите ключ, значение которого хотите получить:')
print(a[h])
