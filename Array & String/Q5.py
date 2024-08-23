#485. Max Consecutive Ones

''' Given a binary array nums, return the maximum number of consecutive 1's in the array.

 

Example 1:

Input: nums = [1,1,0,1,1,1]
Output: 3
Explanation: The first two digits or the last three digits are consecutive 1s. The maximum number of consecutive 1s is 3.
Example 2:

Input: nums = [1,0,1,1,0,1]
Output: 2 '''

class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        curr_cons = 0
        max_cons = 0
        for i in range(len(nums)):
            if nums[i] == 1:
                curr_cons += 1
                if curr_cons > max_cons:
                    max_cons = curr_cons
            else:
                curr_cons = 0
        return max_cons
