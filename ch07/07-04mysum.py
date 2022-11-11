def mysum(x, y = 0): # 함수 mysum() 정의, 기본 매개변수
    """두 수의 합 반환 함수""" # 함수 문서
    return x + y # x + y 연산하여 리턴

hap = mysum(5) # 변수 hap에 mysum() 함수 호출하여 5 + 0 을 연산한 5 리턴받아 대입
print(hap) # 표준 출력 함수 print() 호출하여 변수 hap 출력

hap = mysum(5, 10) # 변수 hap에 mysum() 함수 호출하여 5 + 10 을 연산한 15 리턴받아 대입
print(hap) # 표준 출력 함수 print() 호출하여 변수 hap 출력