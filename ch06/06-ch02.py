# 중괄호 {} 안에 직접 요소를 넣어 딕셔너리를 만들어 변수 stock에 대입
stock = {"삼성에스디에스":242000, "삼성전자":47000, "엔씨소프트":52600, "핸디소프트":5120, "골프존":215000, "기아":56300}
print(stock) # 표준 출력 함수 print() 호출하여 딕셔너리 stock 출력
print() # 줄바꿈

while True: # 조건식이 True일 동안 반복, 즉 무한반복
    name = input("주식 이름 ? ") # 표준 입력 함수 input() 호출하여 입력 안내 메세지 출력 동시에 사용자로부터 입력 받은 문자열을 리턴하여 변수 name 에 대입
    if name in stock: # 만약 변수 name이 딕셔너리 stock의 키이면
        print("{}: {}".format(name, stock[name])) # 표준 출력 함수 print() 호출하여 변수 name과 딕셔너리 stock의 키가 name인 요소의 값 출력
        print() # 줄바꿈
    else: # 그렇지 않으면, 즉 name이 딕셔너리 stock의 키가 아니면
        print("주식 이름이 없습니다.") # 표준 출력 함수 print() 호출하여 주식 이름이 없습니다. 안내 메세지 출력
        break # 반복문을 빠져나감
