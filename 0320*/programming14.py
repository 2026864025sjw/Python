import math

a=float(input("a를 입력하시오:"))
b=float(input("b를 입력하시오:"))
c=float(input("c를 입력하시오:"))

r=b**2-4*a*c

if r>0:
    root1=(-b+math.sqrt(r))/(2*a)
    root2=(-b-math.sqrt(r))/(2*a)
    print(f"실근은{root1}과{root2}입니다.")
elif r==0:
    root=-b/(2*a)
    print(f"중근은{root}입니다.")
else:
    print("실근이 존재하지 않습니다.")