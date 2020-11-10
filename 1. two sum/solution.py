from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        """
        :param nums: list of unique integers
        :param target: target sum
        :return: list of index
        """
        if not nums or len(nums) < 2:
            return []
        num_map = {}
        for i in range(len(nums)):
            remainder = target - nums[i]
            if remainder in num_map:
                return [i, num_map[remainder]]
            else:
                num_map[nums[i]] = i
        return []
