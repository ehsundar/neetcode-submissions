class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        m = {}
        for i, v in enumerate(nums):
            m[v] = i
        
        for i, v in enumerate(nums):
            if (target-v) in m and m[target-v] != i:
                return [i, m[target-v]]
        
        return []
        