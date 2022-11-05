from random import randint # random 모듈의 randint() 함수 임포트

number1 = randint(1,99) # randint() 함수 호출하여 1~99 중에서 난수 발생하여 변수 number1에 대입
number2 = randint(1,99) # randint() 함수 호출하여 1~99 중에서 난수 발생하여 변수 number2에 대입
number3 = randint(1,99)

max_number = max(number1, number2, number3) # max() 함수 호출하여 number1, number2, number3 중에서 최대값 리턴하여 변수 max_number에 대입

print("{} {} {} 중에서 최대: {}".format(number1, number2, number3, max_number)) # 표준 출력 함수 print() 호출하여 난수 3개와 최댓값 출력
                                                                                # 파이썬의 포맷팅 방식인 format() 메소드 호출하여 포맷팅