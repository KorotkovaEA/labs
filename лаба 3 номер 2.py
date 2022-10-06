n = int(input('Введите длину массива: '))
a = [0] * n
for i in range(0, n):
    a[i] = int(input())
k = a.count(0)
print(k)
