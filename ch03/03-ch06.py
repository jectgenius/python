number1, number2 = input("실수 두개 입력 >> ").split() # 표준 입력 함수 input() 호출하여 입력 안내 메세지 출력 동시에 사용자로부터 입력 받은 문자열을 split() 메소드 호출하여 공백을 구분자로하여 분리된 문자열을 담은 리스트를 리턴받아 변수 number1, 2에 각각 대입
number1, number2 = int(number1), int(number2) # int() 함수 호출하여 문자열 number1, 2를 정수로 변환한 뒤 변수 number1, 2에 각각 대입
print("{} > {} 결과: {}".format(number1, number2, number1 > number2)) # number1이 number2보다 크다.
print("{} >= {} 결과: {}".format(number1, number2, number1 >= number2)) # number1이 number2보다 크거나 같다.
print("{} < {} 결과: {}".format(number1, number2, number1 < number2)) # number1이 number2보다 작다.
print("{} <= {} 결과: {}".format(number1, number2, number1 <= number2)) # number1이 number2보다 작거나 같다.
print("{} == {} 결과: {}".format(number1, number2, number1 == number2)) # number1은 number2와 같다.
print("{} != {} 결과: {}".format(number1, number2, number1 != number2)) # number1은 number2와 다르다.
# 표준 출력 함수 print() 호출하여 number1, 2의 비교 연산 결과를 출력
# 파이썬의 포맷팅 스타일인 format() 메소드 호출하여 포맷팅
# 비교 연산자는 피연산자가 2개인 이항 연산자이다.
# 비교 연산의 결과는 논리값 True, False이다.
# 파이썬은 다른 프로그래밍 언어와 달리 논리값이 대문자로 시작한다.