circle = [3, 5, 7, 10] # [] 대괄호 안에 직접 요소를 넣어 리스트를 만들어 변수 circle에 대입
area = list(map(lambda r: r*r*3.14, circle)) # map() 함수 호출하여 맵핑한 결과를 list() 함수 호출하여 리스트로 변환한 뒤 변수 area에 대입

for c, a in zip(circle, area): # 변수 c, a에 zip() 함수 호출하여 리스트 circle, area를 튜플로 묶은 시퀀스의 모든 요소가 순서대로 하나씩 할당될 동안 반복
    print("반지름 {} => 원면적 {}".format(c, a)) # 표준 출력 함수 print() 호출하여 변수 c, a 출력