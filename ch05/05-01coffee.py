coffee = ["에스프레소", "아메리카노", "카페라테", "카페모카"] # 커피 메뉴를 담은 리스트 생성하여 변수 coffee에 대입
print(coffee) # 표준 출력 함수 print() 호출하여 리스트 coffee 출력
print(type(coffee)) # 표준 출력 함수 print() 호출하여 coffee의 자료형 출력

num = 0 # 변수 num에 0 대입
for s in coffee: # 변수 s에 coffee에 저장된 값 모두 순서대로 할당될 동안 반복
    num +=1 # num에 +1
    print("%d. %s" % (num, s)) # 표준 출력 함수 print() 호출하여 num, s 출력
                               # 커피 메뉴 번호와 함께 하나씩 출력
