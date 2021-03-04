"""
Single Number III

Given an integer array nums, in which exactly two elements appear only once and all the other elements appear exactly twice. Find the two elements that appear only once. You can return the answer in any order.
Follow up: Your algorithm should run in linear runtime complexity. Could you implement it using only constant space complexity?

Example 1:

Input: nums = [1,2,1,3,2,5]
Output: [3,5]
Explanation:  [5, 3] is also a valid answer.

Example 2:

Input: nums = [-1,0]
Output: [-1,0]

Example 3:

Input: nums = [0,1]
Output: [1,0]
 
Constraints:

2 <= nums.length <= 3 * 10^4
-231 <= nums[i] <= 2^31 - 1
Each integer in nums will appear twice, only two integers will appear once.
"""

class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        nums.sort()
        res = []
        i = 0
        while(i < len(nums)):
            if i == len(nums) - 1 or not nums[i] == nums[i+1]:
                res.append(nums[i])
                i += 1
            else:
                i += 2
        return res