class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count = {}
        n = len(nums)
        for i in nums:
            count[i] = count.get(i, 0) + 1
        for i, j in count.items():
            if j > n // 2:
                return i