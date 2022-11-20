n = int(input('Введите длину списка: '))
a = [0] * n
for i in range(0, n):
    a[i] = int(input())
l = len(a)
if l % 2 == 0:
    b = [0] * (l//2)
else:
    b = [0] * ((l//2)+1)
k = 0
for i in range(0, n):
    if i % 2 == 0:
        b[k] = a[i]
        k += 1
    else:
        continue
print(b)
        
