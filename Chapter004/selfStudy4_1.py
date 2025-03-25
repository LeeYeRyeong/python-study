## 변수 선언 부분 ##
money, p50000, p10000, p5000, p1000 = 0,0,0,0,0

## 메인 코드 부분 ##
money = int(input("교환할 돈은 얼마? "))

p50000 = money / 50000
money %= 50000

p10000 = money / 10000
money %= 10000

p5000 = money / 5000
money %= 5000

p1000 = money / 1000
money %= 1000

print("\n 50000원 ==> %d장" %p50000)
print("\n 10000원 ==> %d장" %p10000)
print("\n 5000원 ==> %d장" %p5000)
print("\n 1000원 ==> %d장" %p1000)
print("\n 바꾸지 못한 돈 ==> %d원" %money)