h, w = input("당신의 키(cm)와 몸무게(kg)는? >> ").split()
h = int(h)
w = int(w)

bmi = w / ((h / 100) ** 2)
e = ""

if 40 <= bmi:
    e = "고도 비만"
elif 35 <= bmi:
    e = "중등도 비만"
elif 30 <= bmi:
    e = "비만" 
elif 25 <= bmi:
    e = "과체중" 
elif 18.5 <= bmi:
    e = "정상" 
else:
    e = "저체중"

print("키: {}(cm), 몸무게: {}(km)".format(h, w)) 
print("BMI: {:.1f} {}".format(bmi, e)) 