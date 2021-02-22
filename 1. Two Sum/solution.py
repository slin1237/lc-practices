from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        """
        :param nums: List of integers
        :param target: integer
        :return: list of index
        """
        if not nums or len(nums) < 2:
            return []
        res_map = {}
        for i in range(len(nums)):
            remainder = target - nums[i]
            if remainder in res_map:
                return [i, res_map[remainder]]
            else:
                res_map[nums[i]] = i
        return []
