# 169. Majority Element (n/ 2 times)

''' Given an array nums of size n, return the majority element.

The majority element is the element that appears more than ⌊n / 2⌋ times. You may assume that the majority element always exists in the array.

Example 1:
Input: nums = [3,2,3]
Output: 3

Example 2:
Input: nums = [2,2,1,1,1,2,2]
Output: 2'''

#First Approach 

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        n = len(nums)
        for i in range(len(nums)):
            count = 0
            for j in range(i,len(nums)):
                if nums[i] == nums[j]:
                    count += 1
            if count > len(nums) // 2:
                return nums[i]
        return -1
      
#Second Approach

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        dic1 = {}
        for i in nums:
            if i in dic1:
                dic1[i] += 1
            else:
                dic1[i] = 1
        for freq, item in dic1.items():
            if item > len(nums) // 2:
                return freq
