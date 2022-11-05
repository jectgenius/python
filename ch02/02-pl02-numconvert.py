base = int(input("입력할 정수의 진수(base)는? ")) # 표준 입력 함수 input() 호출하여 입력 안내 메세지 출력 동시에 사용자로부터 입력 받은 문자열을 리턴하고, int() 함수 호출하여 정수로 변환한 뒤 리턴하여 변수 base에 대입
strNum = input(str(base) + "진수 정수 입력 >> ") # 변수 strNum에 사용자로부터 입력 받은 문자열 정수를 대입
data = int(strNum, base) # base진수 문자열을 10진수 정수로 변환

print("2진수:", bin(data)) # 표준 출력 함수 print() 호출하고 bin() 함수 호출하여 10진수 정수 data를 2진수 정수 출력
print("8진수:", oct(data))
print("10진수:", data)
print("16진수:", hex(data))
