korean = ("정렬", "초보자", "내포", "사전") # 변수 korean에 문자열이 요소인 튜플 만들어 대입
english = ("sorting", "novice", "comprehension", "dictionary") # 변수 english에 문자열이 요소인 튜플 만들어 대입

q = input("찾을 단어 입력 ? ") # 변수 q에 표준 입력 함수 input() 호출하여 입력 안내 메세지 출력 동시에 사용자로부터 입력 받은 문자열 리턴하여 대입
exist = False # 변수 exist에 False 대입

for i in range(len(korean)): # 변수 i에 0부터 튜플 korean의 요소의 개수 미만 정수가 하나씩 순서대로 할당될 동안 반복
    if q == korean[i]: # 만약 q가 튜플 korean의 i번째 인덱스의 요소와 같다면
        exist = True # exist에 True 대입
        print(english[i]) # 표준 출력 함수 print() 호출하여 튜플 english의 i번째 요소 출력

if exist == False: # 만약 exits가 False이면, 반복문 다 끝난 후
    print("그러한 단어는 사전에 없습니다.") # 표준 출력 함수 print() 호출하여 없습니다. 안내 메세지 출력
