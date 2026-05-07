class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        while len(stones)>1:
            stones.sort()
            st = stones.pop()-stones.pop()
            if st :
                stones.append(st)
        return stones[0] if stones else 0        