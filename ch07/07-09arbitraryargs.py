def hello(*names): # 함수 hello() 정의
    """가변 인자 name 활용""" # 함수 문서 문자열
    for each in names: # 가변인자 names의 모든 요소를 순서대로 하나씩 변수 each에 할당될 동안 반복
        print("안녕, {}!".format(each)) # 표준 출력 함수 print() 호출하여 "안녕, {}!" 출력

hello("나타샤") # hello() 함수 호출하여 "안녕, 나타샤!" 출력
hello("수빈", "현수", "지효") # hello() 함수 호출하여 "안녕, {}!" 출력
hello(*["방탄소년단", "여자친구"]) # hello() 함수 호출하여 리스트를 가변인자로 변환하여 전달하여 "안녕, {}!" 출력