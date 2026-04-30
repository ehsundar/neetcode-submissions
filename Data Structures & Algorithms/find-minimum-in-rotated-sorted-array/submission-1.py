class Solution:
    def findMin(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]

        l = 0
        r = len(nums) - 1
        lowest = nums[0]

        while l < r:
            mid = (l + r) // 2
            print(mid)
            lowest = min(lowest, nums[mid])
            if nums[l] > nums[mid]:
                r = mid - 1
                lowest = min(lowest, nums[r])
            elif nums[mid] > nums[r]:
                l = mid + 1
                lowest = min(lowest, nums[l])
            else:
                r -= 1
        
        return lowest
        