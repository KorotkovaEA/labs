a = int(input())
b = int(input())
c = int(input())
if a == b and b == c:
    print('0')
elif a == b or b == c or a == c:
    print('1')
else:
    print('3')
