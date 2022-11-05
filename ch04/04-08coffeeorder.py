for i in range(3): # 변수 i에 정수 0~2가 할당될 동안 반복
    coffee = input("주문하세요! [아메리카노] [카페라테] [카푸치노] >> ") # 변수 coffee에 표준 입력 함수 input() 호출하여 입력 안내 메세지 출력 동시에 사용자로부터 입력 받은 문자열을 리턴하여 대입
    
    if coffee == "아메리카노": # 만약 조건식이 True이면, 변수 coffee에 저장된 문자열이 "아메리카노"이면, 즉 사용자가 주문한 메뉴가 아메리카노이면
        print("%s 주문" % (coffee)) # 표준 출력 함수 print() 호출하여 주문 메뉴 출력
    elif coffee == "카페라테":
        print("%s 주문" % (coffee))
    elif coffee == "카푸치노":
        print("%s 주문" % (coffee))
    else: # 그렇지 않으면, 즉 전 조건식이 모두 False이면, 즉 사용자가 주문한 메뉴가 아메리카노, 카페라테, 카푸치노가 아니면
        print("모르겠어요.") # 표준 출력 함수 print() 호출하여 모르겠어요. 출력

else: # 반복문이 다 끝나면
    print("주문을 마치겠습니다.") # 표준 출력 함수 print() 호출하여 주문을 마치겠습니다. 출력

# print()가 반복되고 있으므로 print()를 한 번만 사용하도록 수정하면
# if coffee == "아메리카노" or coffee == "카페라테" or coffee == "카푸치노":
#     print("%s 주문" % (coffee))
# else:
#     print("모르겠어요.")
