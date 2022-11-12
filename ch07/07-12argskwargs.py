def sumvalue(*values, **kwargs): # 함수 sumvalue() 정의, 가변 매개변수, 키워드 가변 매개변수 
    hap = 0 # 지역 변수 hap에 0 대입
    for v in values: # 변수 v에 튜플 values의 모든 요소가 순서대로 하나씩 할당될 동안 반복
        hap += v # 변수 hap에 +v
    
    for key in kwargs: # 변수 key에 딕셔너리 kwargs의 모든 요소의 키가 순서대로 하나씩 할당될 동안 반복
        hap += kwargs[key] # 변수 hap에 딕셔너리 kwargs의 키가 key인 요소의 값을 합함 
    
    return hap # 변수 hap 리턴

coffeeprice = {"value":2000, "에스프레소":2000, "아메리카노":2800, "카페라테":3200} # {} 중괄호 안에 요소 직접 넣어 딕셔너리 만들어 변수 coffeeprice에 대입
print(sumvalue(1, 2, 3, **coffeeprice)) # 표준 출력 함수 print() 호출하고 sumvalue() 호출하여 출력
print(sumvalue(*[2, 3, 4], **coffeeprice))