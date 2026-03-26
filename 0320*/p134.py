import random

print("주사위 던지기 게임을 시작합니다.")
dice=random.randrange(6)

if dice==0:
    print("1")
elif dice==1:
    print("2")
elif dice==2:
    print("3")
elif dice==3:
    print("4")
elif dice==4:
    print("5")
else:
    print("6")
print("게임이 종료되었습니다.")