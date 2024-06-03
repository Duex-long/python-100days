# Python语言进阶

prices = {
    'AAPL': 191.88,
    'GOOG': 1186.96,
    'IBM': 149.24,
    'ORCL': 48.44,
    'ACN': 166.89,
    'FB': 208.09,
    'SYMC': 21.29
}
# 用价格大于100元的股票构造一个新的字典
# 推倒
price2 = {key:value  for key,value in prices.items() if value > 100 }
print(price2)


# 嵌套的列表的坑

names = ['关羽', '张飞', '赵云', '马超', '黄忠']
courses = ['语文', '数学', '英语']
# scores = [[None] * len(courses) for _ in range(len(names))]
scores = [[None] * len(courses) for _ in range(len(names))]
print(scores)

# 数组创建的合并
a = [None] * len(courses) # [None, None, None]
b = [i for i in range(len(names))]

print([a for _ in range(len(names))])

#堆栈
list1 = [34, 25, 12, 99, 87, 63, 58, 78, 88, 92]
list2 = [
    {'name': 'IBM', 'shares': 100, 'price': 91.1},
    {'name': 'AAPL', 'shares': 50, 'price': 543.22},
    {'name': 'FB', 'shares': 200, 'price': 21.09},
    {'name': 'HPQ', 'shares': 35, 'price': 31.75},
    {'name': 'YHOO', 'shares': 45, 'price': 16.35},
    {'name': 'ACME', 'shares': 75, 'price': 115.65}
]
import heapq

print(heapq.nlargest(3,list1)) # 从大到小三个
print(heapq.nsmallest(3,list1)) #从小到大3个

# 字典排序
print(heapq.nlargest(3,list2,key=lambda x:x['price'])) # 根据price 从大到小三个
print(heapq.nsmallest(3,list2,key=lambda x:x['shares'])) # 根据price 从大到小三个


#迭代工具
import itertools
print([x for x in itertools.permutations('ABCD')])
