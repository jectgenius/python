menu = ["COFFEE", "BEVERAGE", "ADE"] # 리스트를 만들어 변수 menu에 대입
coffee = ["에스프레소", "아메리카노", "카페라테", "카페모카"] # 리스트를 만들어 변수 coffee에 대입

print("=" * 45) # 표준 출력 함수 print() 호출하여 문자열=를 45번 반복한 문자열 출력
for category in menu: # 변수 category에 리스트 menu의 모든 요소들이 하나씩 순서대로 할당될 동안 반복
    print("{:^15s}".format(category), end=" ") # 표준 출력 함수 print() 호출하여 category 출력, 문자열을 폭 15 중앙정렬하고, end에 공백
print() # 줄바꿈
print("=" * 45) # 표준 출력 함수 print() 호출하여 문자열=를 45번 반복한 문자열 출력

for ckind in coffee: # 변수 ckind에 리스트 coffee의 모든 요소들이 하나씩 순서대로 할당될 동안 반복
    print("{:^10s}".format(ckind)) # 표준 출력 함수 print() 호출하여 ckind 출력, 문자열을 폭 10 중앙정렬하여 출력
                                   # 파이썬의 포맷팅 스타일인 format() 메소드 호
