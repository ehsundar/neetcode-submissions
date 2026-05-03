class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # min heap
        h = []

        for i, num in enumerate(nums):
            if len(h) == k:
                heapq.heappushpop(h, (num, i))
            else:
                heapq.heappush(h, (num, i))

        return heapq.heappop(h)[0]
