import random

computer_choice=random.randint(1,3)
user_choice=int(input("어디를 수비하시겠어요?(왼쪽: 1,중앙: 2,오른쪽 3)"))
if user_choice<1 and user_choice<3:
    print("잘못 입력하셨습니다.")
if computer_choice==user_choice:
    print("수비를 성공하셨습니다.")
else:
    print("페날티킥이 성공하였습니다.")