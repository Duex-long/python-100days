# 英制单位英寸与公制单位厘米互换。

value = float(input("输入长度："))
unit = input("输入单位")

def unitTransform(value,unit):
    if unit == 'in' or unit == '英寸':
        print('%f英寸 = %f厘米' % (value, value * 2.54))
    elif unit == 'cm' or unit == '厘米':
        print('%f厘米 = %f英寸' % (value, value / 2.54))
    else:
        print('请输入有效的单位')

# 百分制成绩转换为等级制成绩。
score = float(input('请输入成绩: '))
if score >= 90:
    grade = 'A'
elif score >= 80:
    grade = 'B'
elif score >= 70:
    grade = 'C'
elif score >= 60:
    grade = 'D'
else:
    grade = 'E'

# 输入三条边长，如果能构成三角形就计算周长和面积。

def checkIsTriangle(a1,a2,a3):
    if a1 + a2 > a3 and a1 + a3 > a2 and a2 + a3 > a1:
        return True
    else:
        return False
def computedArea(a1,a2,a3):
    print("周长：%f" %(a1+a2+a3))
    p = (a1 + a2 + a3) / 2
    area = (p * (p - a1) * (p - a2) * (p - a3) ) ** .5
    print('面积: %f' % (area))

if checkIsTriangle(2,2,1):
    computedArea(2,2,1)
else:
    print('不能构成三角形')