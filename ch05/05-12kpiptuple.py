singer = ("BTS", "볼빨간사춘기", "BTS", "블랙핑크", "태연") # 변수 singer에 문자열이 요소인 튜플 만들어 대입
song = ("작은 것들을 위한 시", "나만, 봄", "소우주", "Kill This Love", "사계") # 변수 song에 문자열이 요소인 튜플 만들어 대입
print(singer) # 표준 출력 함수 print() 호출하여 튜플 singer 출력
print(song) # 표준 출력 함수 print() 호출하여 튜플 song 출력

print(singer.count("BTS")) # 표준 출력 함수 print() 호출하고, 튜플 singer의 메소드 count() 호출하여 "BTS"의 개수 출력
print(singer.index("볼빨간사춘기")) # 표준 출력 함수 print() 호출하고, 튜플 singer의 메소드 index() 호출하여 "볼빨간사춘기"의 인덱스 출력
print(singer.index("BTS")) # 표준 출력 함수 print() 호출하고, 튜플 singer의 메소드 index() 호출하여 "BTS"의 인덱스 출력
print() # 줄바꿈

for _ in range(len(singer)): # 변수 _에 0부터 튜플 singer의 요소의 개수 미만까지 할당될 동안 반복 
    print("%s: %s" % (singer[_], song[_])) # 표준 출력 함수 print() 호출하여 튜플 singer와 song의 인덱스 _번째 요소 출력
                                           # C언어의 포맷팅 방식인 형식 지정자 사용하여 포맷팅