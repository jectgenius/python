print((lambda x: x ** 3)(3)) # 표준 출력 함수 print() 호출하여 람다 함수 리턴값 출력, 일반 매개 변수 x를 세제곱 하여 리턴
print((lambda a, b: a % b)(10, 3)) # 표준 출력 함수 print() 호출하여 람다 함수 리턴값 출력, 일반 매개 변수 a, b를 a를 b로 나눈 나머지 리턴

div = lambda a, b: a / b # 람다 함수 정의하여 변수 div에 대입, 일반 매개변수 a, b를 a를 b로 나누기 연산한 결과를 리턴
print(div(10, 2)) # 표준 출력 함수 print() 호출하고, div() 함수 호출하여 리턴 값 출력