def addone(): # 함수 addone() 정의
    """함수에서 대입에 사용되는 변수는 지역변수"""
    i = 30 # 지역변수 i에 30 대입
    i += 1 # 지역변수 i에 +1하여 대입, 즉 31
    print("\t지역변수 i:", i) # 표준 출력 함수 print() 호출하여 "\t지역변수 i: 31" 출력

i = 20 # 전역변수 i에 20 대입
print("i:", i) # 표준 출력 함수 print() 호출하여 전역변수 "i: 20" 출력
addone() # 함수 addone() 호출하여 "지역변수 i: 31" 출력
print("i:", i) # 표준 출력 함수 print() 호출하여 전역변수 "i: 20" 출력