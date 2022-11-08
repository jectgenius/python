animal = [["사자", "코끼리", "호랑이"], "조류", "어류"] # 변수 animal에 리스트를 만들어 대입
print(animal) # 표준 출력 함수 print() 호출하여 리스트 animal 출력

for s in animal: # 변수 s에 리스트 animal의 모든 요소 순서대로 하나씩 할당될 동안 반복
    print(s) # 표준 출력 함수 print() 호출하여 변수 s 출력
print() # 줄바꿈

bird = ["독수리", "참새", "까치"] # 변수 bird에 리스트 만들어 대입
fish = ["갈치", "붕어", "고등어"] # 변수 fish에 리스트 만들어 대입
animal[1:] = [bird, fish] # 변수 animal을 인덱스 1번째 요소부터 끝까지 슬라이싱하여 리스트 [bird, fish]를 대입
print(animal) # 표준 출력 함수 print() 호출하여 리스트 animal 출력

for lst in animal: # 변수 lst에 리스트 animal의 모든 요소를 순서대로 하나씩 할당될 동안 반복
    for item in lst: # 변수 item에 변수 lst에 저장된 리스트의 모든 요소를 순서대로 하나씩 할당될 동안 반복
        print(item, end=" ") # 표준 출력 함수 print() 호출하여 변수 item에 저장된 값 출력, 기본매개변수 end의 인자가 " "이므로 한 칸씩 띄어서 출력
    print() # 줄바꿈
print() # 줄바꿈