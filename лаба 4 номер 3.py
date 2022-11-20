n = int(input('Введите длину списка: '))
a = [0] * n
for i in range(0, n):
    a[i] = int(input())
print(a)
m = max(a)
n = min(a)
k = a.index(m)
l = a.index(n)
a[l] = a[k]
a[k] = n
print(a)
