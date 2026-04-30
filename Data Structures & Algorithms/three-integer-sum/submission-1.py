class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        results = set()
        for i, v in enumerate(nums):
            two_sums = self.two_sum(nums, -v, i + 1)
            for ts in two_sums:
                ts.append(v)
                ts.sort()
                results.add(tuple(ts))
        
        return list(results)

    def two_sum(self, nums, target, start=0) -> List[List[int]]:
        m = {}
        for i in range(start, len(nums)):
            m[nums[i]] = target - nums[i]
        
        results = []
        for k, v in m.items():
            if v in m and k != v:
                results.append([k, v])
        
        return results
    