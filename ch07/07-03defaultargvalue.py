def hello(name = "여러분"): # hello() 함수 정의, 기본 매개변수 
    print("안녕, {}!".format(name)) # 표준 출력 함수 print() 호출하여 "안녕, {}!" 출력

hello() # hello() 함수 호출하여 "안녕, 여러분!" 출력
hello("현철") # hello() 함수 호출하여 "안녕, 현철!" 출력