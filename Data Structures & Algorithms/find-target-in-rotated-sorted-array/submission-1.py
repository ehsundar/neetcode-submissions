class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l = 0
        r = len(nums) - 1

        while l <= r:
            mid = (l + r) // 2
            if target == nums[mid]:
                return mid

            if nums[mid] > nums[r]:
                # break right side
                if nums[l] <= target < nums[mid]:
                    r = mid - 1
                else:
                    l = mid + 1
                continue
            else:
                # break left side
                if nums[r] >= target > nums[mid]:
                    l = mid + 1
                else:
                    r = mid - 1
                continue

        return -1
