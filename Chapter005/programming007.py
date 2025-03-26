import random

diceA1 = random.randrange(1,7)
diceA2 = random.randrange(1,7)
diceB1 = random.randrange(1,7)
diceB2 = random.randrange(1,7)

print("A의 주사위 숫자는 %d %d 입니다"%(diceA1, diceA2))
print("B의 주사위 숫자는 %d %d 입니다"%(diceB1, diceB2))

if(diceA1+diceA2 > diceB1+diceB2):
    print("A가 이겼네요")
elif(diceA1+diceA2 < diceB1+diceB2) :
    print("B가 이겼네요")
else :
    print("둘이 비겼네요.")