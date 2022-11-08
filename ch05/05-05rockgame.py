from random import choice # random 모듈의 choice() 함수 임포트

rsp = ["가위", "바위", "보"] # 변수 rsp에 문자열이 요소인 리스트 만들어 대입 
for i in range(len(rsp)): # 변수 i에 0부터 리스트 rsp의 길이 미만인 정수를 순서대로 하나씩 모두 할당될 동안 반복 
    print(rsp[i], end=" ") # 표준 출력 함수 print() 호출하여 리스트 rsp의 인덱스 i번째 요소 출력, 기본매개변수 end의 인자가 " "이므로 한 칸씩 띄어서 출력
print() # 줄바꿈

print("컴퓨터의 가위 바위 보 5개") # 표준 출력 함수 print() 호출하여 컴퓨터의 가위 바위 보 안내 메세지 출력
for i in range(5): # 변수 i에 0부터 5미만인 정수를 순서대로 하나씩 모두 할당될 동안 반복
    print(choice(rsp)) # 표준 출력 함수 print() 호출하고 choice() 함수 호출하여 리스트 rsp의 요소를 랜덤으로 출력
