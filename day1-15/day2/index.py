# 华氏温度转换为摄氏温度。

f = float(input('请输入华氏温度: '))
c = (f - 32) / 1.8
print('%.1f华氏度 = %.1f摄氏度' % (f, c))

# 练习2：输入圆的半径计算计算周长和面积。


radius = float(input('请输入圆的半径: '))


pi = 3.14

perimeter = 2 * pi * radius

area = pi * radius * radius

# 练习3：输入年份判断是不是闰年。

year = int(input('请输入年份：'))

is_leap = not bool(year % 4)


# day2 主要介绍了部分变量的定义和类型