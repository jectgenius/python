color = dict(검은색="black", 흰색="white", 녹색="green", 파란색="blue") # 함수 dict() 호출하여 기본매개변수 인자 전달 방식으로 딕셔너리를 만들어 변수 color에 대입
print(color) # 표준 출력 함수 print() 호출하여 딕셔너리 color 출력

# 항목 조회
print(color.get("녹색")) # 표준 출력 함수 print() 호출하여 딕셔너리 color의 get() 메소드 호출하여 키가 "녹색"인 요소의 값 리턴하여 출력
print(color.get("노란색")) # 표준 출력 함수 print() 호출하여 딕셔너리 color의 get() 메소드 호출하여 키가 "노란색"인 요소의 값 리턴하여 출력, 없을때 반환할 값 인자 전달하지 않았으므로 None 리턴
print() # 줄바꿈 

color["노란색"] = "yellow" # 딕셔너리 color의 키가 "노란색"이고 값이 "yellow"인 요소 추가
print(color) # 표준 출력 함수 print() 호출하여 딕셔너리 color 출력
print() # 줄바꿈 

# 항목 삭제
c = "흰색" # 변수 c에 문자열 대입
print("삭제: %s %s" % (c, color.pop("흰색"))) # 표준 출력 함수 print() 호출하고, 딕셔너리 color의 pop() 메소드 호출하여 키가 "흰색"인 요소의 값 리턴하며 삭제하여 출력
print(color) # 표준 출력 함수 print() 호출하여 딕셔너리 color 출력
c = "빨간색" # 변수 c에 문자열 대입
print("삭제: %s %s" % (c, color.pop(c, "없어요"))) # 표준 출력 함수 print() 호출하고, 딕셔너리 color의 pop() 메소드 호출하여 키가 "빨간색"인 요소의 값 리턴하며 삭제하여 출력, 키가 없을 때 반환 값 인자 지정하여 없으면 "없어요" 출력

print("임의 삭제: {} ".format(color.popitem())) # 표준 출력 함수 print() 호출하고, 딕셔너리 color의 popitem() 메소드 호출하여 임의의 항목 리턴하며 삭제하여 출력 
print("임의 삭제 후: {}".format(color)) # 표준 출력 함수 print() 호출하여 딕셔너리 color 출력
                                       # 파이썬의 포맷팅 방식인 format() 메소드 호출하여 포맷팅
c = "검은색" # 변수 c에 문자열 대입
del color[c] # del 키워드 사용하여 딕셔너리 color의 키가 "검은색"인 요소 삭제
print("{} 삭제 후: {}".format(c, color)) # 표준 출력 함수 print() 호출하여 딕셔너리 color 출력

# 모든 항목 삭제
color.clear() # 딕셔너리 color의 메소드 clear() 호출하여 모든 요소 삭제
print(color) # 표준 출력 함수 print() 호출하여 딕셔너리 color 출력