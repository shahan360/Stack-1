'''
739. Daily Temperatures
Problem Link: https://leetcode.com/problems/daily-temperatures/description/
'''

# Time Complexity : O(n), where n is the number of days in the input list. Each day is processed at most twice (once when it's added to the stack and once when it's removed).
# Space Complexity : O(n), in the worst case, if the temperatures are in decreasing order, all indices will be stored in the stack.
# Did this code successfully run on Leetcode : Yes and it passed all test cases.
# Any problem you faced while coding this : Yes, to find the correct indices and calculate the number of days waited, I had to ensure that I was correctly popping from the stack and updating the result array.

class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # Initialize the result array with zeros
        res = [0] * len(temperatures) 

        # Stack to keep indices of days waiting for a warmer temperatur
        stack = []

        # Loop through each day's temperature
        for i, temp in enumerate(temperatures):
            # Check if the current temperature is warmer than the last stacked day
            while stack and temp > temperatures[stack[-1]]:
                prev_index = stack.pop()
                # Calculate the number of days waited
                res[prev_index] = i - prev_index
            # Push the current day's index onto the stack
            stack.append(i)
        
        # Return the filled result array
        return res