class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        if len(nums) <= 1:
            return []

        ltr = [nums[0]] * len(nums)
        rtl = [nums[-1]] * len(nums)

        for i in range(1, len(nums)):
            ltr[i] = ltr[i - 1] * nums[i]
            rtl[len(nums) -1 - i] = rtl[len(nums) - i] * nums[len(nums) - i - 1]

        results = [0] * len(nums)
        results[0] = rtl[1]
        results[-1] = ltr[-2]

        for i in range(1, len(nums) - 1):
            results[i] = ltr[i - 1] * rtl[i + 1]

        return results
