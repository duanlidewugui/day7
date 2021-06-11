#选择排序
#这个应该是选择排序，将最小的列表数字一个个放在最左边
#2021/6/11/17/13
numbers = [10,4,5,67,8,9,0,2,4,1,2,4,6,8,56,12,1,4,5,67,7,9,90,3,21,1]
def select_sort(numbers):
    i = 0
    k = 0
    while k < len(numbers):
        i = 0
        q = -1
        while i < len(numbers) - 1 - k:
            if i == 0:
                team = numbers[k]
                q = k
            if team > numbers[k + i + 1]:
                team = numbers[k + i + 1]
                q = k + i + 1
            i += 1
        t = numbers[k]
        numbers[k] = numbers[q]
        numbers[q] = t
        k += 1
    return numbers

print(select_sort(numbers))












