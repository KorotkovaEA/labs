n = int(input('Введите длину списка: '))
a = [0] * n
for i in range(0, n):
    a[i] = int(input())
k = 0
for i in range(1, n):
    if a[i] > a[i-1]:
        k += 1
    else:
        continue
b = [0] * k
m = 0
for i in range(1, n):
    if a[i] > a[i-1]:
        b[m] = a[i]
        m += 1
print(b)
