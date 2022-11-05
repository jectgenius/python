from random import randint # radom 모듈의 randint() 함수 임포트

while True: # 조건식이 True이면 반복, 조건식이 True 논리 리터럴이므로 무한 반복
    number1 = randint(1, 99) # randint() 함수 호출하여 1~99 중에서 난수 발생하여 변수 number1에 대입
    number2 = randint(1, 99) # randint() 함수 호출하여 1~99 중에서 난수 발생하여 변수 number2에 대입
    result = number1 * number2 # 변수 result에 number1과 number2의 곱하기 연산 결과 대입

    print("{} * {} = {}\n".format(number1, number2, result)) # 표준 출력 함수 print() 호출하여 number1과 2 그리고 곱하기 연산결과 출력
                                                             # 파이썬의 포맷팅 방식인 format() 메소드 호출하여 포맷팅
    response = input("계속 y / n ? ") # 표준 입력 함수 input() 호출하여 입력 안내 메세지 출력 동시에 사용자로부터 입력 받은 문자열을 변수 response에 대입
    if response == "n": # 만약 조건식이 True이면, 즉 response가 "n"이면, 사용자가 입력한 문자열이 "n"이면
        break # 반복문을 빠져나감, 즉 while문을 빠져나감

# while문을 빠져나가면 프로그램 종료