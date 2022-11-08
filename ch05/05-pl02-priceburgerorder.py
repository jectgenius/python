menu = ("주문 종료", "올인원팩", "투게더팩", "트리오팩", "패밀리팩") # 변수 menu에 문자열이 요소인 튜플 만들어 대입
price = (0, 6000, 7000, 8000, 10000) # 변수 price에 정수가 요소인 튜플 만들어 대입

# 주문에 필요한 메세지 문자열 만들기
msg = "주문할 콤보 번호와 수량을 계속 입력하세요!" # 변수 msg에 문자열 대입
for i in range(len(menu)): # 변수 i에 0부터 튜플 menu의 요소의 개수 미만인 정수가 순서대로 하나씩 모두 할당될 동안 반복
    msg += "\n\t %d %s" % (i, menu[i]) # 문자열 msg에 문자열 연결 연산자 이용하여 튜플 menu의 인덱스 i번째 요소 문자열 만들어 대입
    if i != 0: # 만약 i가 0이 아니면, 즉 "주문 종료"가 아니면
        msg += " %5d 원" % (price[i]) # 문자열 msg에 문자열 연결 연산자 이용하여 튜플 price의 인덱스 i번째 요소 문자열 만들어 대입
msg += "\n >> " # 반복문이 다 끝나면 문자열 msg에 문자열 연결 연산자 이용하여 ">>" 대입

# 주문에 필요한 변수 초기화
more = True # 변수 more에 True 대입
total = 0 # 변수 total에 0 대입

while more: # 변수 more이 True이면 반복
    instr = input(msg) # 변수 instr에 표준 입력 함수 input() 호출하여 입력 안내 메세지 msg 출력 동시에 사용자로부터 입력받은 문자열 리턴하여 대입
    if instr.count(" ") > 0: # 만약 문자열 instr이 " "가 0보다 크면, 즉 사용자가 입력한 정수가 2개이면
        order, cnt = instr.split() # 문자열 instr의 메소드 split() 호출하여 공백을 구분자로 하여 분리된 문자열 리스트를 변수 order, cnt에 각각 대입
        cnt = int(cnt) # 변수 cnt에 int() 함수 호출하여 문자열을 정수로 변환한 뒤 대입
    else: # 그렇지 않으면, 즉 사용자가 입력한 정수가 1개이면
        order = instr # 변수 order에 사용자가 입력한 문자열인 instr 대입
    
    order = int(order) # 변수 order에 int() 함수 호출하여 문자열을 정수로 변환한 뒤 대입
    if order == 0: # 만약 order가 0이면
        print() # 줄바꿈
        print(" 주문 종료 ".center(20, "*")) # 표준 출력 함수 print() 호출하여 "주문종료" 출력, center() 메소드 호출하여 폭 20, 채울문자 "*"인 문자열 만들어 리턴
        more = False # 변수 more에 True 대입
    elif 1 <= order <=4: # 그렇지 않고 변수 order가 1이상 4이하 이면
        print("%s, %d개 주문" % (menu[order], cnt)) # 튜플 menu의 인덱스 order번째 요소와 사용자가 주문한 개수 cnt를 출력
        sub = price[order] * cnt # 튜플 price의 order번째 요소, 즉 가격과 주문한 개수를 연산하여 변수 sub에 대입
        total += sub # 변수 total에 변수 sub 합함
        print("%s 주문 가격 %d, 총 가격 %d" % (menu[order], sub, total)) # 표준 출력 함수 print() 호출하여 현재 주문한 가격인 sub와 총 주문 가격인 total 출력
    else: # 그렇지 않으면
        print("모르겠어요. 다시 주문하세요!") # 표준 출력 함수 print() 호출하여 모르겠어요. 출력

else: # while문 다 끝나면
    print("총 주문 가격 %d 원" % total) # 표준 출력 함수 print() 호출하여 총 주문 가격 출력
    print("주문을 마치겠습니다.") # 표준 출력 함수 print() 호출하여 주문을 마치겠습니다. 출력
    print(" 안녕! ".center(20, "=")) # 표준 출력 함수 print() 호출하여 안녕 출력, center() 메소드 호출하여 폭 20 채울문자 "=" 로 만들어진 문자열 리턴
