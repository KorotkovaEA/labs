n = int(input())
k = str(1)
for i in range(1, n+1):
    print(k)
    a = int(k)%10
    k = str(k) + str(a+1)
    

