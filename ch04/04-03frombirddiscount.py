from time import localtime # time 모듈의 localtime() 함수를 import
hour = localtime().tm_hour # localtime() 함수 호출하여 현재 시간을 변수 hour에 대입
mnt = localtime().tm_min # localtime() 함수 호출하여 현재 분을 변수 mnt에 대입

if hour < 10: # 만약 조건식이 True이면, 즉 10 이하 이면, 즉 오전 10시 이전이면
    print("지금 시각: %d시 %d분, 조조 할인 된다. " % (hour, mnt)) # 표준 출력 함수 print() 호출하여 조조 할인 가능 메세지 출력
else: # 그렇지 않으면, 즉 조건식이 False이면, 즉 오전 10시 이후이면
    print("지금 시각: %d시 %d분, 조조 할인 안 된다. " % (hour, mnt)) # 표준 출력 함수 print() 호출하여 조조 할인 불가능 메세지 출력

# C언어의 포맷팅 방식인 형식 지정자 사용하여 포맷팅
