menu = ["COFFEE", "BEVERAGE", "ADE"] # 변수 menu에 종류를 요소로 하는 리스트 만들어 대입
coffee = ["에스프레소", "아메리카노", "카페라테", "카페모카"] # 변수 coffee에 커피 종류를 요소하는 리스트 만들어 대입

print("=" * 45) # 표준 출력 함수 print() 호출하여 문자열 "="을 문자열 반복 연산자 이용하여 45번 반복한 문자열 만들어 리턴한 문자열 출력
for category in menu: # 변수 category에 리스트 menu의 모든 요소가 순서대로 하나씩 할당될 동안 반복
    print("{:^15s}".format(category), end=" ") # 표준 출력 함수 print() 호출하여 변수 category를 폭 15, 중앙 정렬하여 출력, 기본매개변수 end의 인자가 " "이므로 한칸씩 띄어서 출력, 줄바꿈X
print() # 줄바꿈
print("=" * 45) # 표준 출력 함수 print() 호출하여 문자열 "="을 문자열 반복 연산자 * 이용하여 45번 반복한 문자열을 만들어 리턴한 문자열 출력

for ckind in coffee: # 변수 ckind에 리스트 coffee의 모든 요소가 순서대로 하나씩 할당될 동안 반복
    print("{:^10s}".format(ckind)) # 표준 출력 함수 print() 호출하여 변수 ckind를 폭10, 중앙정렬로 정렬하여 출력
                                   # 파이썬의 포맷팅 방식인 format() 메소드 호출하여 포맷팅