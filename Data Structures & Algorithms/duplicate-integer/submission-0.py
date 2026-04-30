class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        m = set()
        for v in nums:
            if v in m:
                return True
            m.add(v)
        return False
