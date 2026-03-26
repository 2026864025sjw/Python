unit=input("섭씨는 C, 화씨는 F를 입력하시오:")
temp=float(input("온도를 입력하시오:"))

if unit=="F":
    temp=(temp-32)*5/9
    
if temp<=0:
    print("물의 상태는 얼음입니다.")
elif temp>0 and temp<100:
    print("물의 상태는 액체입니다.")
else:
    print("물의 상태는 기체입니다.")