class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        results = set()
        for i, v in enumerate(nums):
            pairs = self.two_sum(nums, i+1, -v)
            for p in pairs:
                results.add((v, *p))
        
        return list(results)
    
    def two_sum(self, nums, start, target):
        results = []
        if len(nums) - start < 2:
            return []

        m = {}
        for i in range(start, len(nums)):
            m[nums[i]] = i

        for i in range(start, len(nums)):
            to_find = target - nums[i]
            idx = m.get(to_find, -1)
            if idx <= i:
                continue

            results.append((nums[i], nums[idx]))            

        return results
