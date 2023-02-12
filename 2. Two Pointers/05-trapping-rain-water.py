# Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it can trap after raining.

class Solution:
    def trap(self, height: List[int]) -> int:
        ans = 0
        size = len(height)
        for i in range(1, size - 1):
            left_max, right_max = 0, 0
            for j in range(i, -1, -1):
                left_max = max(left_max, height[j])
            for j in range(i, size):
                right_max = max(right_max, height[j])
            ans += min(left_max, right_max) - height[i]
        return ans