str = "일요일 기러기" # 변수 str에 문자열 대입
print(str[:3], str[4:]) # 표준 출력 함수 print() 호출하여 문자열 슬라이싱한 결과를 출력, start, end 생략되면 처음부터 끝까지 포함, step 생략되면 1
print(str[:-4], str[-3:])
print(str[:], str[::], str[::1]) # 문자열 전체 슬라이싱
print(str[::2]) # step이 2, 즉 인덱스에 +2
print(str[::3]) # step이 3, 즉 인덱스에 +3
print(str[::-2]) # step이 -2, 즉 인덱스에 -2
print(str[::-1]) # step이 -1, 즉 인덱스에 -1, 문자열 전체 역순으로 슬라이싱
