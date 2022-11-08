day1 = ("monday", "tuesday", "wednesday") # 변수 day1에 문자열이 요소인 튜플 만들어 대입
day2 = ("thursday", "friday", "saturday") # 변수 day2에 문자열이 요소인 튜플 만들어 대입
day3 = ("sunday", ) # 변수 day3에 문자열이 요소인 튜플 만들어 대입, 요소가 1개인 튜플은 만들때 만드시 요소 뒤에 ,콤마를 써야한다.

day = day1 + day2 + day3 # 변수 day에 튜플 day1, day2, day3를 튜플 연결 연산자 +를 이용하여 새로 만들어진 튜플 대입
print(type(day)) # 표준 출력 함수 print() 호출하고 type() 함수 호출하여 튜플 day의 자료형 출력 
print(day) # 표준 출력 함수 pritn() 호출하여 튜플 day 출력

day = day1 + day2 + day3 * 3 # 변수 day에 튜플 day1, day2, day3를 튜플 연결 연산자와 반복 연산자 + *를 이용하여 새로 만들어진 튜플 대입
print(day) # 표준 출력 함수 print() 호출하여 튜플 day 출력
