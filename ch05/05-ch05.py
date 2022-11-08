sports = ["축구", "야구", "농구", "배구"] # 변수 sports에 문자열을 요소로 하는 리스트 만들어 대입
num = [11, 9, 5, 6] # 변수 num에 정수를 요소로 하는 리스트 만들어 대입

sports.insert(1, 11) # 리스트 sports의 메소드 insert() 호출하여 인덱스 1번째에 요소 11 삽입
sports.insert(3, 9) # 리스트 sports의 메소드 insert() 호출하여 인덱스 3번째에 요소 9 삽입
sports.insert(5, 5) # 리스트 sports의 메소드 insert() 호출하여 인덱스 5번째에 요소 5 삽입
sports.insert(7, 6) # 리스트 sports의 메소드 insert() 호출하여 인덱스 9번째에 요소 6 삽입
print("메소드 insert()로 팀원 수 삽입")
print(sports)

sports = ["축구", "야구", "농구", "배구"] # 변수 sports에 문자열을 요소로 하는 리스트 만들어 대입, 초기화
for i in range(1, 8, 2): # 변수 i에 1부터 8미만, 간격이 2인 정수가 모두 순서대로 할당될 동안 반복
    sports.insert(i, "") # 리스트 sports의 메소드 insert() 호출하여 인덱스 i번째에 "" 삽입
print("메소드 insert()로 "" 삽입")
print(sports)

sports[1::2] = num # 리스트 sports에 인덱스 1번째 부터 끝까지 간격 2만큼 슬라이싱한 요소에 리스트 num 대입
print("슬라이스 sports[1::2]에 num을 대입")
print(sports)