class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        if len(nums) == 1:
            return nums[0]
        return max(self.rob_sub(nums, 0))

    # two resp, (i'm in), (i'm not in)
    def rob_sub(self, nums, start):
        if len(nums) - start == 2:
            return nums[start], nums[start + 1]

        next_in, next_not_in = self.rob_sub(nums, start + 1)

        im_in = nums[start] + next_not_in
        im_not_in = max(next_in, next_not_in)
        return im_in, im_not_in
