km = float(input("차의 속도를 입력(km) >> ")) # 표준 입력 함수 input() 호출하여 입력 안내 메세지 출력 동시에 사용자로부터 입력 받은 문자열을 리턴하고 float() 함수 호출하여 실수로 변환하여 변수 km에 대입
mile = km / 1.61 # 킬로미터 단위의 거리를 마일 단위의 거리로 변환하는 연산을 하여 변수 mile에 대입, 파이썬에서 / 나누기 연산 결과는 항상 실수
print(str(km) + "(km)은 " + str(mile) + " 마일(miles)이다.") # 표준 출력 함수 print() 호출하여 출력, 문자열 연결 연산자 +로 연결 하기위해 str() 함수 호출하여 문자열로 변환
