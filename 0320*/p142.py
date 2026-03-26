import random

print("행운의 매직볼로 오늘의 운세를 출력합니다.")
answers=random.randint(1,8)
if answers==1:
    print("확실히 이루어집니다.")
elif answers==2:
    print("좋아 보이네요")
elif answers==3:
    print("믿으셔도 됩니다.")
elif answers==4:
    print("노력한 만큼 결과가 나와요.")
elif answers==5:
    print("휴식이 필요한 하루입니다.")
elif answers==6:
    print("새로운 도전을 해보세요.")
elif answers==7:
    print("행운이 찾아옵니다.")
else:
    print("조심하는 게 좋아요.")