#Maximum Subarray Problem, Leetcode 53.
#Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.

#Time Complexity of the solution: O(n)

def maxSubArray(nums):
    currMax = globalMax = nums[0]
    for i in range(1,len(nums)):
        currMax = max(nums[i], nums[i] + currMax)
        if currMax > globalMax:
            globalMax = currMax
    return globalMax
            
        
