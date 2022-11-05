s1 = "Beautiful is better than ugly." # 변수 s1에 문자열 대입
print(s1) # 표준 출력 함수 print() 호출하여 변수 s1에 저장된 문자열 출력
print("위의 철학을 메소드 replace()를 사용해 다음 철학으로 다시 저장") # 표준 출력 함수 print() 호춯하여 문자열 출력
s2 = s1.replace("Beautiful", "Explicit") # replace() 메소드 호출하여 old를 new로 교체하여 생성된 새로운 문자열 리턴하여 변수 s2에 대입
s2 = s2.replace("ugly", "implicit") # replace() 메소드 호출하여 old를 new로 교체하여 생성된 새로운 문자열 리턴하여 변수 s2에 대입
print(s2) # 표준 출력 함수 print() 호출하여 변수 s2에 저장된 문자열 출력