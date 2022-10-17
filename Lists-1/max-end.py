# Given an array of ints length 3, figure out which is larger, the first or last element in the array, 
# and set all the other elements to be that value. Return the changed array.
def max_end3(nums):
  n = len(nums)
  if nums[0] >= nums[n - 1]:
    for i in range(n):
        nums[i] = nums[0]
  else:
    for i in range(n):
        nums[i]=nums[n-1]
  return nums

