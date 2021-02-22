from typing import List


class Solution:
    def maxArea(self, height: List[int]) -> int:
        """
        :param height: list of height
        :return: maximum area of water
        """
        if not height:
            return 0
        max_water = 0
        left, right = 0, len(height)-1
        while left < right:
            cur_area = (right - left) * min(height[left], height[right])
            max_water = max(cur_area, max_water)
            if height[left] >= height[right]:
                right -= 1
            else:
                left += 1
        return max_water


