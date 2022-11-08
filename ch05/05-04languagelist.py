pl = ["C", "C++", "Python", "Java"] # 변수 pl에 문자열이 요소인 리스트 만들어 대입 

print(pl[0]) # 표준 출력 함수 print() 호출하여 리스트 pl의 인덱스 0번째 요소 출력
print(pl[2]) # 표준 출력 함수 print() 호출하여 리스트 pl의 인덱스 2번째 요소 출력
print() # 줄바꿈

for i in range(len(pl)): # 변수 i에 0부터 리스트의 길이 미만인 정수를 하나씩 순서대로 모두 할당될 동안 반복
    print(pl[i]) # 표준 출력 함수 print() 호출하여 리스트 pl의 인덱스 i번쨰 요소 출력
