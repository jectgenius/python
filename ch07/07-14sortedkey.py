words = "The core of extensible programming is defining functions.".split() # 문자열을 split() 메소드 호출하여 공백을 구분자로 분리된 문자열을 담은 리스트를 리턴하여 변수 words에 대입

print(sorted(words, key = str.lower)) # 표준 출력 함수 print() 호출하고, sorted() 함수 호출하여 리스트 words를 소문자로 바꿔 정렬한 결과를 리스트로 리턴하여 출력
print(sorted(words, key = lambda word:word[1])) # 표준 출력 함수 print() 호출하고, sorted() 함수 호출하여 리스트 words를 문자열의 인덱스 1번째 문자를 기준으로 정렬한 결과를 리스트로 리턴하여 출력

groupnumber = [("잔나비", 5), ("트와이스", 9), ("블랙핑크", 4), ("방탄소년단", 7)] # [] 대괄호 안에 요소를 직접 넣어 리스트를 만들어 변수 groupnumber에 대입
print(sorted(groupnumber)) # 표준 출력 함수 print() 호출하고, sorted() 함수 호출하여 리스트 groupnumber를 정렬한 결과를 리스트를 출력
print(sorted(groupnumber, key = lambda singer: singer[1])) # 표준 출력 함수 print() 호출하고, sorted() 함수 호출하여 리스트 groupnumber를 groupnumber의 요소인 튜플의 인덱스 1번째 요소를 기준으로 정렬한 리스트를 리턴하여 출력