class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i, value_i in enumerate(nums):
            for ii, value_ii in enumerate(nums):
                if i == ii:
                    continue
                if value_i + value_ii == target:
                    answer_i = i
                    answer_ii = ii
                    return [answer_i, answer_ii]
