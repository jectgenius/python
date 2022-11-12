singer = ["BTS", "볼빨간사춘기", "BTS", "블랙핑크", "태연", "BTS"] # 변수 singer에 [] 대괄호 안에 직접 요소 넣어 리스트를 만들어 대입, 가수
song = ["작은 것들을 위한 시", "나만 봄", "소우주", "Kill This Love", "사계"] # 변수 song에 [] 대괄호 안에 직접 요소 넣어 리스트를 만들어 대입, 노래

kpop = list(zip(singer, song)) # zip() 함수 호출하여 각 요소를 튜플로 짝짓고, list() 함수 호출하여 리스트로 만들어 변수 kpop에 대입
print(kpop) # 표준 출력 함수 print() 호출하여 리스트 kpop 출력

kpchart = dict(enumerate(kpop, start = 1)) # enumerate() 함수 호출하여 리스트 kpop의 각 요소를 1부터 튜플로 짝짓고, dict() 함수 호출하여 딕셔너리로 만들어 변수 kpchart에 대입
print(kpchart) # 표준 출력 함수 print() 호출하여 딕셔너리 kpchart 출력
print() # 줄바꿈

import pprint # pprint 모듈 임포트
pprint.pprint(kpchart) # pprint 모듈의 pprint() 함수 호출하여 딕셔너리 kpchart 출력