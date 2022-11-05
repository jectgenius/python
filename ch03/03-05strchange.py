str = input("2개의 단어를 빈 공간으로 구분해 입력하세요. >> ") # 표준 입력 함수 input() 호출하여 입력 안내 메세지 출력 동시에 사용자로부터 입력 받은 문자열을 변수 str에 대입
pos = str.find(" ") # find() 메소드 호출하여 " "공백의 인덱스 리턴하여 변수 pos에 대입 
pre_word = str[:pos] # 변수 pre_word에 인덱스 0부터 pos미만의 문자열 슬라이싱하여 대입 
post_word = str[pos+1:] # 변수 post_word에 인덱스 pos+1부터 끝까지의 문자열 슬라이싱하여 대입
print(pre_word, post_word) # 표준 출력 함수 print() 호출하여 변수에 저장된 문자열 출력, 인자가 여러개인 경우 , 콤마로 구분하여 출력, 이때 한 칸씩 띄어쓰기 되어 출력
print(pre_word[::-1], post_word[::-1]) # 표준 출력 함수 print() 호출하여 변수에 저장된 문자열 출력, start, end는 생략되어 있으므로 전체 문자열을 의미하고 step이 -1이므로 전체 문자열을 역순으로 슬라이싱
