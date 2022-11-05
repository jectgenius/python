from random import randint

HOURLY_WAGE = 12000

wage = 0

for i in range(5):
    working_hours = randint(35, 50)

    if working_hours >= 40:
        wage = HOURLY_WAGE * 40 + HOURLY_WAGE * 1.5 * (working_hours - 40)
    else:
        wage = HOURLY_WAGE * working_hours
    
    print("근로시간 %d시간, 주급 %d" % (working_hours, wage))