season = {"봄":"spring", "여름":"summer", "가을":"autumn", "겨울":"winter"} # 중괄호 {} 안에 요소를 직접 넣어 딕셔너리를 만들어 변수 season에 대입
print(season.keys()) # 표준 출력 함수 print() 호출하고, 딕셔너리 season의 메소드 keys() 호출하여 키로만 이루어진 dict_keys 리스트 출력 
print(season.items()) # 표준 출력 함수 print() 호출하고, 딕셔너리 season의 메소드 values() 호출하여 값으로만 이루어진 dict_values 리스트 출력
print(season.values()) # 표준 출력 함수 print() 호출하고, 딕셔너리 season의 메소드 items() 호출하여 키와 값이 튜플로 묶어진 dict_items 리스트 출력

for key in season: # 변수 key에 딕셔너리 season의 키를 모두 순서대로 할당될 동안 반복
    print("%s %s " % (key, season[key])) # 표준 출력 함수 print() 호출하여 변수 key와 딕셔너리 season의 키가 key인 요소의 값 출력

for item in season.items(): # 변수 item에 딕셔너리 season의 dict_item 리스트의 요소를 모두 순서대로 할당될 동안 반복
    print("{} {} ".format(item[0], item[1]), end=" ") # 표준 출력 함수 pritn() 호출하여 변수 item의 인덱스 0번째 요소, 1번째 요소의 값 출력, 기본매개변수 end의 인자가 " "이므로 한 칸씩 띄어서 출력
print() # 줄바꿈

for item in season.items(): # 변수 item에 딕셔너리 season의 dict_item 리스트이 요소를 모두 순서대로 할당될 동안 반복
    print("{} {} ".format(*item), end=" ") # 표준 출력 함수 print() 호출하여 변수 item의 모든 요소를 출력, 기본매개변수 end의 인자가 " "이므로 한 칸씩 띄어서 출력
print() # 줄바꿈
