for i in range(20, 42, 3): # 변수 i에 정수 20이상 41미만 3간격이 하나씩 순서대로 할당될 동안 반복
    celsius = i # 변수 celsius에 i 대입, 섭씨
    formal_fahrenheit = celsius * (9/5) + 32 # 화씨 정식 계산하여 변수 formal_fahrenheit에 대입
    informal_fahrenheit = celsius * 2 + 30 # 화씨 약식 계산하여 변수 informal_fahrenheit에 대입
    difference = abs(informal_fahrenheit - formal_fahrenheit) # 변수 difference에 abs() 함수 호출하여 화씨 정식과 약식 계산의 차 절댓값 대입
    
    print("섭씨: {} 화씨: {:.1f} 화씨(약식): {:d} 차이: {:.2f}".format(celsius, formal_fahrenheit, informal_fahrenheit, difference)) # 표준 출력 함수 print() 호출하여 출력

