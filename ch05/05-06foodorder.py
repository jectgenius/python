food = ["짜장면", "짬뽕", "우동", "울면"] # 변수 food에 문자열을 요소로 하는 리스트 만들어 대입
print(food) # 표준 출력 함수 print() 호출하여 리스트 food 출력

food.append("탕수육") # 리스트 food의 메소드 append() 호출하여 맨 뒤에 "탕수육" 요소로 추가
print(food) # 표준 출력 함수 print() 호출하여 리스트 food 출력

food[1] = "굴짬뽕" # 리스트 food의 인덱스 1번째 요소를 "굴짬뽕" 으로 변경
print(food) # 표준 출력 함수 print() 호출하여 리스트 food 출력

food[food.index("우동")] = "물만두" # 리스트 food의 메소드 index() 호출하여 "우동"의 인덱스 리턴하여 "우동"을 "물만두"로 변경
print(food) # 표준 출력 함수 print() 호출하여 리스트 food 출력