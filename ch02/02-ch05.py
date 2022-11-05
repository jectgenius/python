celsius = int(input("온도 입력 >> ")) # 표준 입력 함수 input() 호출하여 입력 안내 메세지 출력 동시에 사용자로부터 입력 받은 문자열을 리턴하여 정수로 변환하는 int() 함수 호출하여 인자로 전달하여 정수로 변환한 뒤 변수 celsius에 대입, 화씨 온도
precise_fahrenheit = celsius * 9/5 + 32 # 정확 계산 변수 precise_fahrenheit에 정확하게 연산하여 화씨로 변환된 온도 대입
informal_fahrenheit = celsius * 2 + 30 # 약식 계산 변수 informal_fahrenheit에 약식으로 연산하여 화씨로 변환된 온도 대입
difference = precise_fahrenheit - informal_fahrenheit # 정확과 약식 차이 변수 difference에 차이 연산하여 대입 

print("정확 계산: 섭씨:", celsius, ", 화씨:", precise_fahrenheit) # 표준 출력 함수 print() 호출하여 출력, 인자가 여러개인 경우 ,콤마로 구분하여 전달, 한칸씩 띄어쓰기 되어 출력
print("약식 계산: 섭씨:", celsius, ", 화씨:", informal_fahrenheit)
print("차이:", difference) # 표준 출력 함수 print() 호출하여 정확, 약식 계산 차이 출력, 인자가 여러개인 경우 ,콤마로 구분하여 전달, 한칸씩 띄어쓰기 되어 출력
