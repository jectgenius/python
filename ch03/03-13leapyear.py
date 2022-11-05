year = int(input("윤년을 검사할 연도 입력 >> ")) # 표준 입력 함수 input() 호출하여 입력 안내 메세지 출력 동시에 사용자로부터 입력 받은 문자열을 리턴하여 int() 함수 호출하여 정수로 변환한 뒤 변수 year에 대입
print("입력한 연도: %d" % year) # 표준 출력 함수 print() 호출하여 입력한 연도 출력, C언어의 포맷팅 방식인 형식 지정자 사용
cond1 = year % 4 == 0 # 변수 cond1에 조건 1 연산 결과 대입
cond2 = year % 100 != 0 # 변수 cond2에 조건 2 연산 결과 대입
cond3 = year % 400 == 0 # 변수 cond3에 조건 3 연산 결과 대입
result1 = cond1 and cond2 or cond3 # 변수 result1에 윤년 개별 검사 결과 대입, 논리 연산자의 우선 순위는 and가 or보다 높기 때문에 괄호를 생략해도 된다.
print("개별 검사 {} and {} or {} : {}".format(cond1, cond2, cond3, result1)) # 표준 출력 함수 print() 호출하여 개별 검사 결과 출력, 파이썬의 포맷팅 방식인 format() 메소드 호출하여 포맷팅
result2 = year % 4 == 0 and year % 100 != 0 or year % 400 == 0 # 변수 result2에 통합 검사 결과 대입, 연산자 우선 순위 때문에 괄호 생략해도 된다.
print("통합 검사: %s" % result2) # 표준 출력 함수 print() 호출하여 통합 검사 결과 출력, C언어의 포맷팅 스타일인 형식 지정자 사용하여 