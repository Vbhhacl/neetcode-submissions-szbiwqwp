class Solution:
    def check(self, nums: List[int]) -> bool:
        count = 0
        n = len(nums)
        
        for i in range(n):
            # Compare current element with the next element
            # (i + 1) % n handles the wrap-around from the last element to the first
            if nums[i] > nums[(i + 1) % n]:
                count += 1
                
            # If we find more than 1 drop, it's invalid
            if count > 1:
                return False
                
        return True