def hello(): # hello() 함수 정의
    print("\tHello, Python!") # 표준 출력 함수 print() 호출하여 "\tHello, Python!" 출력

def helloint(): # helloint() 함수 정의
    print("\t", 77) # 표준 출력 함수 print() 호출하여 "t", 77 출력

print("처음 하는 함수 호출 hello()") # 표준 출력 함수 print() 호출하여 문자열 출력
hello() # hello() 함수 호출하여 "\tHello, Python!" 출력
print("함수 호출 hello() 이후") # 표준 출력 함수 print() 호출하여 문자열 출력

print(1) # 표준 출력 함수 print() 호출하여 1 출력
print(helloint) # 표준 출력 함수 print() 호출하여 함수 helloint()가 저장된 메모리 주소 출력
helloint() # hello() 함수 호출하여 "\t", 77 출력
print(3) # 표준 출력 함수 print() 호출하여 3 출력