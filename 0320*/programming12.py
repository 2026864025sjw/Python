year=int(input("연도를 입력하시오:"))
result=year%12

if result==0:
    print("원숭이띠입니다.")
elif result==1:
    print("닭띠입니다.")
elif result==2:
    print("개띠입니다.")
elif result==3:
    print("돼지띠입니다.")
elif result==4:
    print("쥐띠입니다.")
elif result==5:
    print("소띠입니다.")
elif result==6:
    print("범띠입니다.")
elif result==7:
    print("토끼띠입니다.")
elif result==8:
    print("용띠입니다.")
elif result==9:
    print("뱀띠입니다.")
elif result==10:
    print("말띠입니다.")
else:
    print("양띠입니다.")