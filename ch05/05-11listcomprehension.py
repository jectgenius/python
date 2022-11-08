a = [] # 변수 a에 빈 리스트 만들어 대입
for i in range(10): # 변수 i에 0부터 10미만의 정수가 순서대로 모두 할당될 동안 반복
    a.append(i) # 리스트 a의 메소드 append() 호출하여 i를 추가
print(a) # 표준 출력 함수 print() 호출하여 리스트 a 출력

seq = [i for i in range(10)] # 변수 i에 0부터 10미만의 정수가 순서대로 모두 할당될 동안 반복하여 변수 i를 리스트에 추가하여 만들어진 리스트를 변수 seq에 대입
print(seq) # 표준 출력 함수 print() 호출하여 리스트 seq 출력

s = [] # 변수 s에 빈 리스트 만들어 대입
for i in range(10): # 변수 i에 0부터 10미만의 정수가 순서대로 모두 할당될 동안 반복
    if i%2 == 1: # 만약 i를 2로 나눈 나머지가 1이면
        s.append(i**2) # 리스트 s의 메소드 append() 호출하여 i의 2제곱 추가
print(s) # 표준 출력 함수 print() 호출하여 리스트 s 출력

squares = [i**2 for i in range(10) if i%2 == 1] # 변수 i에 0부터 10미만의 정수가 순서대로 모두 할당될 동안 반복, 변수 i를 2로 나눈 나머지가 1이면 i의 제곱을 리스트에 추가하여 만들어진 리스트를 변수 squares에 대입
print(squares) # 표준 출력 함수 print() 호출하여 리스트 squares 출력