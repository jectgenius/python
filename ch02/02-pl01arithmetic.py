number1 = float(input("첫 번째 수 입력 >> ")) # 표준 입력 함수 input() 호출하여 입력 안내 메세지 출력 동시에 사용자로부터 입력 받은 문자열을 리턴하여 float() 함수 호출하여 실수로 변환한 뒤 변수 number1에 대입 
number2 = float(input("두 번째 수 입력 >> ")) # 표준 입력 함수 input() 호출하여 입력 안내 메세지 출력 동시에 사용자로부터 입력 받은 문자열을 리턴하여 float() 함수 호출하여 실수로 변환한 뒤 변수 number2에 대입

add = number1 + number2 # 변수 add에 number1 + number2 연산 결과 대입
sub = number1 - number2
mul = number1 * number2
div = number1 / number2

print("합:", add) # 표준 출력 함수 print() 호출하여 합 연산 결과 출력, 인자가 여러개인 경우 ,콤마로 구분하여 전달, 한칸씩 띄어쓰기 되어 출력
print("차:", sub)
print("곱하기:", mul)
print("나누기:", div)

str1 = input("연산식 입력 >> ") # 표준 입력 함수 input() 호출하여 입력 안내 메세지 출력 동시에 사용자로부터 입력 받은 문자열을 리턴하여 변수 str1에 대입
print("연산식:", str1, "결과:", str(eval(str1))) # eval() 함수 호출하여 문자열 표현식 연산 결과 리턴하고, str() 함수 호출하여 문자열로 변환한 뒤 리턴하여 출력
