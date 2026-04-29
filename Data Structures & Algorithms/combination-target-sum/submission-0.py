class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort(reverse=True)

        return self.get_combs(nums, target)

    def get_combs(self, nums: List[int], target: int) -> List[List[int]]:
        print(nums, target)        

        if len(nums) == 0:
            return []
        if target <= 0:
            return []

        n = nums[0]
        
        max_rep = target // n
        res = []

        if target % n == 0:
            res.append([n for i in range(max_rep)])

        for i in range(max_rep+1):
            
            res1 = self.get_combs(nums[1:], target-(n*i))

            for r in res1:
                r.extend([n for j in range(i)])
            
            res.extend(res1)

        return res
