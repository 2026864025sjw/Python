number=int(input("정수="))

digit1=number%10
number=number//10

digit2=number%10
number=number//10

digit3=number%10
number=number//10

digit4=number%10

total=digit1+digit2+digit3+digit4
print(total)