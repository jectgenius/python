sports = ["축구", "야구", "농구", "배구"] # 변수 sports에 문자열이 요소인 리스트 만들어 대입
num = [11, 9, 5, 6] # 변수 num에 정수가 요소인 리스트 만들어 대입
print(sports) # 표준 출력 함수 print() 호출하여 리스트 sports 출력
print(num) # 표준 출력 함수 print() 호출하여 리스트 num 출력

for i in range(len(sports)): # 변수 i에 0부터 리스트 sports의 요소의 개수미만의 정수가 할당될 동안 반복
    print("%s: %d명 " % (sports[i], num[i]), end=" ") # 표준 출력 함수 print() 호출하여 리스트 sports, num의 인덱스 i번째 요소 출력, 기본매개변수 end의 인자가 " "이므로 한 칸씩 띄어서 출력
print() # 줄바꿈
print() # 줄바꿈

sponum = [sports, num] # 변수 sponum에 리스트 sports, num으로 이루어진 이중 중첩 리스트 만들어 대입
print(sponum) # 표준 출력 함수 print() 호출하여 리스트 sponum 출력

for i in range(len(sponum[0])): # 변수 i에 0부터 리스트 sponum의 0번째 인덱스의 요소의 개수 미만의 정수가 할당될 동안 반복
    print("%s: %d명 " % (sponum[0][i], sponum[1][1]), end=" ") # 표준 출력 함수 print() 호출하여 리스트 sponum의 0번째 리스트 sports의 i번째 요소, 1번째 리스트 num의 i번째 요소 출력, 기본 매개변수 end의 인자가 " "이므로 한 칸씩 띄어서 출력
print() # 줄바꿈
print() # 줄바꿈

psponum = [[sports[i], num[i]] for i in range(len(sports))] # 변수 i에 리스트 sports의 요소의 개수 미만의 정수가 할당될 동안 반복, 리스트 sports의 i번째 요소와 리스트 num의 i번째 요소가 짝지어진 리스트를 리스트의 요소로 추가하여 만들어진 리스트를 변수 psponum에 대입
print(psponum) # 표준 출력 함수 print() 호출하여 리스트 psponum 출력

for one in psponum: # 변수 one에 리스트 psponum의 모든 요소가 순서대로 하나씩 할당될 동안 반복
    print("%s: %d명 " % (one[0], one[1]), end=" ") # 표준 출력 함수 print() 호출하여 변수 one에 할당된 리스트의 인덱스 0번째, 1번째 요소 출력, 기본매개변수 end의 인자가 " "이므로 한 칸씩 띄어서 출력
print() # 줄바꿈
