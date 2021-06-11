#冒泡排序
#进行排序,从小到大排列,进行的左右互换
#2021/6/11/17/16
numbers = [10,4,5,67,8,9,0,2,4,1,2,4,6,8,56,12,1,4,5,67,7,9,90,3,21,1]
def bubble_sort(nums):
    i = 0
    k = 0
    while k < len(nums):
        i = 0
        while i < len(nums) - 1:
            if nums[i] > nums[i + 1]:
                team = nums[i]
                nums[i] = nums[i + 1]
                nums[i + 1] = team

            i += 1
        k +=1
    return nums


print(bubble_sort(numbers))











