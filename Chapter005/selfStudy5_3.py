n = int(input("*** 숫자를 입력하세요 : "))
count = 0

for i in range(2,n):
    if(n % i == 0) : 
        count += 1

if(count==0):
    print("%d는 소수입니다." %n)
else :
    print("%d는 소수가 아닙니다." %n)