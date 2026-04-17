class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        cnt = len(nums)
        for num in nums:
            count = sum(1 for i in nums if i == num)
            if count > cnt // 2:
                return num