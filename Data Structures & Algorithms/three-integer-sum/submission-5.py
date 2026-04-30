class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        if len(nums) < 3:
            return []

        nums.sort()
        results = []
        last_seen = None
        for i, v in enumerate(nums):
            if v == last_seen:
                continue
            last_seen = v

            pairs = self.two_sum(nums, i + 1, -v)
            for p in pairs:
                results.append([v, p[0], p[1]])

        return list(results)

    def two_sum(self, nums, start, target):
        results = []
        if len(nums) - start < 2:
            return []

        l, r = start, len(nums) - 1

        while l < r:
            sm = nums[l] + nums[r]
            if sm == target:
                results.append((nums[l], nums[r]))
                l += 1
                r -= 1
                while l < r and nums[l-1] == nums[l]:
                    l += 1
                while l < r and nums[r+1] == nums[r]:
                    r -= 1
            elif sm < target:
                l += 1
            else:
                r -= 1

        return results
