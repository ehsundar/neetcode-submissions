class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        if len(nums) == 1:
            return nums[0]

        val_skip, val_adj = nums[0], nums[1]
        for i in range(2, len(nums)):
            new_adj = nums[i] + val_skip
            new_skip = max(val_skip, val_adj)

            val_adj = new_adj
            val_skip = new_skip

        return max(val_skip, val_adj)
