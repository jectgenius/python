number = int(input("소수(prime number)인지를 판별한 2 이상의 정수 입력 >> "))

for i in range(2, number): # 1과 자기 자신을 제외한 정수로 만든 시퀀스의 요소를 하나씩 변수 i에 할당할 동안 반복 
    if number % i == 0: # 만약 number의 약수가 그 중에서 하나라도 있다면
        print("정수 {}는 소수가 아니다.".format(number)) # 소수가 아니다.
        break # 반복문을 빠져나감
else: # break문으로 반복문을 빠져나가면 이 문장은 실행되지 않는다. 그 중에서 number의 약수가 하나도 없다면 
    print("정수 {}는 소수이다.".format(number)) # 소수이다. 