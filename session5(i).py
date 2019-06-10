# Pass by reference

def squareOfNumbers(nums):
    for i in range(0,len(nums)):
        nums[i] = nums[i] * nums[i]

numbers = [1,2,3,4,5]
squareOfNumbers(numbers)
print(numbers)

def fun(a, b, c):
    pass

fun(a=10, c=20, b=30)


