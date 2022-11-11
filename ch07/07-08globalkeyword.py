def addone(): # 함수 addone() 정의
    """명시적으로 변수를 전역 변수로 지정"""
    global i # 전역 변수 i
    print("\t 전역 변수 i 읽기, i + 1:", i + 1) # 표준 출력 함수 print() 호출하여 전역 변수 i + 1 출력
    i += 1 # 전역 변수 i에 +1하여 대입

i = 20 # 전역 변수 i에 20 대입
print("i = ", i) # 표준 출력 함수 print() 호출하여 전역변수 i 출력
addone() # addone() 함수 호출하여 전역변수 i + 1 출력
print("i = ", i) # 표준 출력 함수 print() 호출하여 전역변수 i 출력