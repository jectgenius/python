goods = [] # 변수 goods에 빈 리스트 만들어 대입

for i in range(3): # 변수 i에 0부터 3미만의 정수 순서대로 할당될 동안 반복
    item = input("구입할 품목은 ? ") # 변수 item에 표준 입력 함수 input() 호출하여 입력 안내 메세지 출력 동시에 사용자로부터 입력 받은 문자열을 리턴하여 대입
    goods.append(item) # 리스트 goods 맨뒤에 메소드 append() 호출하여 변수 item에 저장된 문자열 추가
    print(goods) # 표준 출력 함수 print() 호출하여 리스트 goods 출력

print("길이: %d" % len(goods)) # 표준 출력 함수 print() 호출하고 함수 len() 호출하여 리스트 goods의 길이 출력
                               # C언어의 포맷팅 방식인 형식 지정자 사용하여 포맷팅