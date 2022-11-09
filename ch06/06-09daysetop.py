daysA = {"월", "화", "수", "목"} # {} 중괄호 안에 요소 직접 넣어 집합 만들어 변수 daysA에 대입
daysB = set(["수", "목", "금", "토", "일"]) # set() 함수 호출하여 인자로 리스트 전달하여 집합 만들어 변수 daysB에 대입
weekends = set(("토", "일")) # set() 함수 호출하여 인자로 튜플 전달하여 집합 만들어 변수 weekends에 대입

alldays = daysA | daysB # 변수 alldays에 집합 daysA와 daysB의 합집합 만들어 리턴하여 대입
print(alldays) # 표준 출력 함수 print() 호출하여 집합 alldays 출력

workdays = alldays - weekends # 변수 workdays에 집합 alldays와 weekends의 차집합 만들어 리턴하여 대입
print(workdays) # 표준 출력 함수 print() 호출하여 집합 worddays 출력

print(daysA & daysB) # 표준 출력 함수 print() 호출하여 집합 daysA와 daysB의 교집합 만들어 리턴하여 출력
print(daysA.symmetric_difference(daysB)) # 표준 출력 함수 print() 호출하여 집합 daysA와 daysB의 여집합 만들어 리턴하여 출력