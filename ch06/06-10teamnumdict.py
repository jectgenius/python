sports = ["축구", "야구", "농구", "배구"] # 
num = [11, 9, 5, 6]

print(sports)
print(num)
print()

print("함수 zip():")
for s, i in zip(sports, num):
    print("%s: %d명" % (s, i), end=" ")
print()
for tp in zip(sports, num):
    print("{}: {}명".format(*tp), end=" ")
print()
print()

print("함수 dict(zip()):")
sportnum = dict(zip(sports, num))
print(sportnum)