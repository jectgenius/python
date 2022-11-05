number = int(input("네 자릿수 정수 입력 >> ")) # 표준 입력 함수 input() 호출하여 입력 안내 메세지 출력 동시에 사용자로부터 입력 받은 문자열을 리턴하고, 함수 int() 호출하여 정수로 변환한 뒤 변수 number에 대입

number4 = number // 1000 # 4번째 자릿수 구하여 변수 number4에 대입
number = number % 1000
number3 = number // 100
number = number % 100
number2 = number // 10
number = number % 10
number1 = number

print(str(number1) + str(number2) + str(number3) + str(number4)) # 표준 출력 함수 print() 호출하여 출력, 문자열 연결 연산자 +를 사용하기위해 str() 함수 호출하여 문자열로 변환
