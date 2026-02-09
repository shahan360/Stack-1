'''
503. Next Greater Element II
Problem Link: https://leetcode.com/problems/next-greater-element-ii/description/
'''

# Time Complexity : O(n) as each element is pushed and popped at most once
# Space Complexity : O(n) for the stack and result array
# Did this code successfully run on Leetcode : Yes and all test cases passed
# Any problem you faced while coding this : Yes, initially I was not handling the circular nature of the array correctly, but after realizing that we can loop through the array twice using modulo, I was able to solve it.

class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        n = len(nums)
        res = [-1] * n # default results
        stack = [] # stack for indices

        # Loop through the array twice to handle the circular part
        for i in range(2 * n):
            curr = nums[i % n] # Wrap around using modulo
            # Pop from stack while current number is greater than the stack's top index number
            while stack and curr > nums[stack[-1]]:
                prev_index = stack.pop()
                res[prev_index] = curr
            # Only push indices from the first pass
            if i < n:
                stack.append(i % n)
        return res