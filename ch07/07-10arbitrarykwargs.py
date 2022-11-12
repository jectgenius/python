def mykeyprint(**kwargs): # 함수 mykeyprint() 정의, 가변 키워드 매개변수는 딕셔너리
    for key in kwargs: # 가변 키워드 매개변수 kwargs의 모든 키를 순서대로 하나씩 변수 key에 할당될 동안 반복
        print("{}: {} ".format(key, kwargs[key]), end = " ") # 표준 출력 함수 print() 호출하여 {}: {} 출력
    print()

mykeyprint(여자친구=6, 마마무=4) # mykeyprint() 함수 호출하여 가변 키워드 매개변수 전달
mykeyprint(엑소=9, 트와이스=9, 블랙핑크=4, 방탄소년단=7)

coffeeprice = {"에스프레소":2500, "아메리카노":2800, "카페라테":3200} # 변수 coffeeprice에 중괄호 {} 안에 요소를 직접 넣어 딕셔너리를 만들어서 대입
mycar = {"brand":"현대", "model":"제네시스", "year": 2016}
mykeyprint(**coffeeprice) # 딕셔너리를 가변 키워드 매개변수로 전달하고자 할때는 ** 사용
mykeyprint(**mycar)