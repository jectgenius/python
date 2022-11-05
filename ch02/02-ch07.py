number1 = float.fromhex(input("첫 번째 16진수 실수 입력 >> ")) # 표준 입력 함수 input() 호출하여 사용자로부터 입력 받은 문자열 리턴하고, float.fromhex() 함수 호출하여 16진수로 변환한 뒤 변수 number1에 대입
number2 = float.fromhex(input("두 번째 16진수 실수 입력 >> "))

add = number1 + number2 # 변수 add에 number1과 number2를 더하기 연산하여 대입
sub = number1 - number2 # 변수 sub에 number1과 number2를 빼기 연산하여 대입
mul = number1 * number2 # 변수 mul에 number1과 number2를 곱하기 연산하여 대입
div = number1 / number2 # 변수 div에 number1과 number2를 나누기 연산하여 대입

print("실수1:", number1, "실수2:", number2) # 표준 출력 함수 print() 호출하여 변수 number1, number2에 저장된 값 출력, 인자가 여러개인 경우 ,콤마로 구분하여 전달, 한 칸씩 띄어쓰기 되어 출력
print("합:", add) # 표준 출력 함수 print() 호출하여 변수 add에 저장된 더하기 연산 결과 출력
print("차:", sub)
print("곱하기:", mul)
print("나누기:", div)
