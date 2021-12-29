class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        nums3 = nums1 + nums2
        nums3.sort()
        if len(nums3)%2 == 0:
            result_1 = len(nums3)/2 - 1
            result_2 = len(nums3)/2
            answer = (nums3[int(result_1)]+nums3[int(result_2)])/2
        else:
            result = len(nums3)/2 - 0.5
            answer = nums3[int(result)]
        return answer
