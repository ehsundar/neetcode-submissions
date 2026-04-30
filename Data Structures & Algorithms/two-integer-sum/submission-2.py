class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        orig_nums = deepcopy(nums)
        nums.sort()

        res = []
        for i, v in enumerate(nums):
            index_2 = self.bin_search(nums, target-v, i+1, len(nums))
            if index_2 is not None:
                res = [i, index_2]
                break
        
        if nums[res[0]] == nums[res[1]]:
            ix1 = orig_nums.index(nums[res[0]])
            ix2 = orig_nums[ix1+1:].index(nums[res[1]]) + ix1 + 1
        else:
            ix1 = orig_nums.index(nums[res[0]])
            ix2 = orig_nums.index(nums[res[1]])

        resp = [ix1, ix2]
        resp.sort()
        return resp

    def bin_search(self, nums, target, l, r):
        if l >= r:
            if nums[l%len(nums)] == target:
                return l
            return None

        mid = (l + r) // 2
        if nums[mid] == target:
            return mid
        if nums[mid] < target:
            return self.bin_search(nums, target, mid + 1, r)
        if nums[mid] > target:
            return self.bin_search(nums, target, l, mid - 1)
