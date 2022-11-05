strTime = input("시각 정보(16:30:15) 입력 >> ") # 표준 입력 함수 input() 호출하여 입력 안내 메세지 출력 동시에 사용자로부터 입력 받은 문자열을 리턴하여 변수 strTime에 대입
hours, mins, secs = strTime.split(":") # 입력 받은 strTime을 split() 메소드 호출하여 ":"을 기준으로 나누어진 문자열 요소를 담은 리스트를 리턴받아 변수 hours, mins, secs에 각각 대입

print("입력 시각 정보:", strTime) # 표준 출력 함수 print() 호출하여 사용자가 입력한 시각 정보 문자열 출력
print("{}시 {}분 {}초".format(hours, mins, secs)) # 표준 출력 함수 print() 호출하여 변수에 저장된 문자열 출력
                                                  # 파이썬의 포맷팅 방식인 format() 함수 호출하여 포맷팅
