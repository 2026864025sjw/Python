height,weight=eval(input("체중과 키를 입력하시오:"))

stadard_weight=(height-100)*0.9

if weight>stadard_weight:
    print("과체중입니다.")
elif weight<stadard_weight:
    print("저체중입니다.")
else:
    print("표준 체중입니다.")