a = int(input("시프트할 숫자는? "))
n = int(input("출력할 횟수는? "))
result = 0
i = 0

for i in range(1,n+1):
    result = a << i
    print("%d << %d = %d" %(a, i, result))\

for i in range(1,n+1):
    result = a >> i
    print("%d >> %d = %d" %(a, i, result))