number1 = int(input("Enter First number: ")) # 표준 입력 함수 input() 호출하여 입력 안내 메세지 출력 동시에 사용자로부터 입력 받은 문자열을 리턴하고, int() 함수 호출하여 정수로 변환한 뒤 변수 number1에 대입
number2 = int(input("Enter Second number: "))
div = number1 / number2 # 변수 div에 나누기 연산 결과 대입
remainder = number1 % number2 # 변수 remainder에 나머지 연산 결과 대입
mod = number1 // number2 # 변수 mod에 몫 연산 결과 대입
power = number1 ** number2 # 변수 power에 거듭제곱 연산 결과 대입

print(number1, "/", number2, "==>", div) # 표준 출력 함수 print() 호출하여 출력, 인자가 여러개인 경우 ,콤마로 구분하여 전달, 한칸씩 띄어쓰기 되어 출력
print(number1, "%", number2, "==>", remainder)
print(number1, "//", number2, "==>", mod)
print(number1, "**", number2, "==>", power)

