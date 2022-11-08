data = [[1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]] # 변수 data에 이중 리스트 만들어 대입

rsum = [0, 0, 0] # 변수 rsum에 각 행의 합을 저장할 리스트의 각 요소를 0으로 초기화하여 만들어 대입

for i in range(3): # 변수 i에 0부터 3미만의 정수 할당될 동안 반복
    sum  = 0 # 변수 sum에 0 대입하여 초기화
    for j in range(3): # 변수 j에 0부터 3미만의 정수 할당될 동안 반복
        sum += data[i][j] # 변수 sum에 리스트 data의 인덱스 i행j열 요소 합함, 행이 고정, 열이 변함
    rsum[i] = sum # 리스트 rsum의 i번째 요소에 sum 대입, 즉 각 행의 요소를 모두 더한 sum을 rsum의 인덱스 i번째 요소에 대입
print("각 행의 합:", rsum) # 표준 출력 함수 print() 호출하여 리스트 rsum 출력하여 각 행의 합 출력

csum = [0, 0, 0] # 변수 csum에 각 열의 합을 저장할 리스트의 각 요소를 0으로 초기화하여 만들어 대입

for i in range(3): # 변수 i에 0부터 0미만의 정수 할당될 동안 반복
    sum  = 0 # 변수 sum에 0 대입하여 초기화
    for j in range(3): # 변수 j에 0부터 3미만의 정수 할당될 동안 반복
        sum += data[j][i] # 변수 sum에 리스트 data의 인덱스 j행i열 요소 합함, 열이 고정, 행이 변함
    csum[i] = sum # 리스트 csum의 i번째 요소에 sum 대입, 즉 각 열의 요소를 모두 더한 sum을 csum의 인덱스 i번째 요소에 대입
print("각 열의 합:", csum) # 표준 출력 함수 print() 호출하여 리스트 csum 출력하여 각 열의 합 출력
