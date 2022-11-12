def sumvalue(value, **kwargs): # 함수 sumvalue() 정의
    hap = value # 지역변수 hap에 일반 매개 변수 value 대입
    for key in kwargs: # 변수 key에 딕셔너리 kwargs의 모든 요소의 키가 순서대로 하나씩 할당될 동안 반복
        hap += kwargs[key] # 딕셔너리 kwargs의 키가 key인 요소의 값이 변수 hap에 합함
    return hap # 지역변수 hap 리턴

coffeeprice = {"에스프레소":2000, "아메리카노":2800, "카페라테":3200} # {} 중괄호 안에 직접 요소를 넣어 딕셔너리 만들어 변수 coffeeprice에 대입
print(sumvalue(100, **coffeeprice)) # 표준 출력 함수 print() 호출하고, sumvalue() 함수 호출하여 리턴값 출력, 일반 매개변수 value에 2000, 가변 키워드 매개변수 kwargs에 딕셔너리 coffeeprice 전달
print(sumvalue(value = 2000, **coffeeprice))
print(sumvalue(**coffeeprice, value = 2000))
