import random

x=random.randint(1,100)
y=random.randint(1,100)

op=random.randint(0,1)

if op==0:
    answer=int(input(f"{x}+{y}="))
    flag=(answer==(x+y))
    print(flag)
else:
    answer=int(input(f"{x}-{y}="))
    flag=(answer==(x-y))
    print(flag) 