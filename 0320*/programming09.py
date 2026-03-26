import random

num1=random.randint(1,10)
num2=random.randint(1,10)

op=random.randint(0,3)

if op==0:
    answer=num1+num2
    user_answer=float(input(f"{num1}+{num2}의 값은?"))
elif op==1:
    answer=num1-num2
    user_answer=float(input(f"{num1}-{num2}의 값은?"))
elif op==2:
    answer=num1*num2
    user_answer=float(input(f"{num1}*{num2}의 값은?"))
else:
    answer=num1/num2
    user_answer=float(input(f"{num1}/{num2}의 값은?"))
    
if user_answer==answer:
    print("맞았습니다.")
else:
    print(f"틀렸습니다. 정답은{answer}입니다.")