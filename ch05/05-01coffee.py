coffee = ["에스프레소", "아메리카노", "카페라테", "카페모카"] # 변수 coffee에 문자열을 요소로 하는 리스트를 직접 만들어 대입
print(coffee) # 표준 출력 함수 print() 호출하여 리스트 coffee 출력
print(type(coffee)) # 표준 출력 함수 print() 호출하고, type() 함수 호출하여 coffee의 자료형인 <class 'list'> 출력

num = 0 # 변수 num에 0 대입
for s in coffee: # 변수 s에 리스트 coffee의 모든 요소가 하나씩 순서대로 할당될 동안 반복
    num += 1 # 변수 num에 +1
    print("%d. %s" % (num, s)) # 표준 출력 함수 print() 호출하여 num, s 출력
                               # C언어의 포맷팅 방식인 형식지정자 사용하여 포맷팅