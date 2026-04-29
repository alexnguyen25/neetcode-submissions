class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heap = []
        for i in nums:
            heapq.heappush(heap, -i)
        if len(heap) > 1:
            for i in range (k - 1):
                heapq.heappop(heap)
        return -heap[0]


        