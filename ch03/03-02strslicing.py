str = "Monty Python" # 변수 str에 문자열 대입
print(len(str)) # 표준 출력 함수 print() 호출하고, len() 함수 호출하여 문자열의 길이 출력
print(str[0:5], str[6:], str[6:12]) # 표준 출력 함수 print() 호출하여 문자열 슬라이싱하여 출력, start는 시작, end는 미만, step은 생략되면 1
print(str[-12:-7], str[-6:], str[-6:0]) # start, end 생략되면 처음부터 끝까지 포함
