menu = """버거, 콤보 번호로 주문하세요!
0. 주문 종료
1. 올인원팩
2. 투게더팩
3. 트리오팩
4. 패밀리팩
    >> """

more = True

while more: # more == True 가 더 좋은 코드, 가독성있게 작성해야한다. 생각하게 만드는 코드는 안 좋은 코드이다.
    order = int(input(menu)) # 표준 입력 함수 input() 호출하여 입력 안내 메세지 변수 menu를 출력 동시에 사용자로부터 입력 받은 문자열을 리턴하여 int() 함수 호출하여 정수로 변환한 뒤 변수 order에 대입

    if order == 1:
        print("%s 주문" % "올인원팩") # \n을 같이 출력하여 줄바꿈 되어 보기 편해야 한다.
    elif order == 2:
        print("%s 주문" % "투게더팩")
    elif order == 3:
        print("%s 주문" % "트리오팩")
    elif order == 4:
        print("%s 주문" % "패밀리팩")
    elif order == 0:
        print("주문 종료".center(20, "*"))
        more = False # 변수 more에 저장된 값이 True에서 False로 바뀌어 조건식이 False가 되어 반복문이 종료됨
    else:
        print("모르겠어요.")

else: # 반복문이 끝나면 
    print("주문을 마치겠습니다.") 
    
