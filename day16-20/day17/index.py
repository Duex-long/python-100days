
# 算法
# def select_sort(items, comp=lambda x, y: x < y):
#     """简单选择排序"""
#     items = items[:]
#     for i in range(len(items) - 1):
#         min_index = i
#         for j in range(i + 1, len(items)):
#             if comp(items[j], items[min_index]):
#                 min_index = j
#         items[i], items[min_index] = items[min_index], items[i]
#     return items

# def select_sort(items,comp=lambda x,y:x>y) {

# }



example = [5,4,3,2,1]


def select_sort(insert_list,comp= lambda x,y:x<y):
    cache_list = insert_list[:]
    cache_len = len(cache_list)
    # 选择排序的内容是当comp为false的时候换位置
    for i in range(cache_len):
        # 大指针
        min_i = i
        for j in range(i+1,cache_len):
            # 之后遍历的是i后的内容
            if not comp(cache_list[min_i] , cache_list[j]):
                min_i = j
        cache_list[i],cache_list[min_i] = cache_list[min_i],cache_list[i]
    return cache_list

print(select_sort([5,4,3,2,1]))
print(select_sort([5,4,3,1,2]),'select')

# 选择算法可以根据条件来选择排序方式
# 默认为 x < y的降序 
# 原理就是 使用双指针的形式，以当前值下表为开始，找到第一个不符合条件的值后指针继续与后找到一个极不符合条件的值
# 此时这个值就是整个list中的极端如果条件是升序，那这个值就是最小，同时换位置，指针后移


# 冒泡排序
# 冒泡排序在于当前值和后面所有值做比较，
def b_sort(items,comp= lambda x,y:x<y):
    cache_list = items[:]
    cache_len = len(cache_list)
    for i in range(cache_len):
        for j in range(cache_len - i - 1):
            current = cache_list[j]
            next_val = cache_list[j+1]
            if not comp(current,next_val):
                cache_list[j],cache_list[j+1] = cache_list[j+1],cache_list[j]
    return cache_list
print(b_sort([5,4,3,2,1]))
print(b_sort([5,4,3,1,2]),'bubble')

# 在冒泡排序中，每个值都会和相邻值做比较，如果不符合则做交换，如果符合则指针后移，此时指针移动过的地方都会是正确的顺序

# 合并有序list

# comp= lambda x,y:x<y 升序
def merge(items1,items2,comp= lambda x,y:x<y):
    index1,index2 = 0,0
    result = []
    while(index1 < len(items1) and index2 < len(items2)):
        # 思路就是判断大和小，同时移动指针
        if comp(items1[index1],items2[index2]):
            result.append(items1[index1])
            index1+=1
        else:
            result.append(items2[index2])
            index2+=1
    result += items1[index1:]
    result += items2[index2:]
    return result
  

print(merge([1,3,5,7,9],[2,4,6,8,9,10]))