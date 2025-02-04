class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # MAX heap:
        heap = [-num for num in nums]

        heapq.heapify(heap)

        for _ in range(k-1):
            heapq.heappop(heap)

        return -heap[0]



# # MIN heap:
#         heap = []

#         for num in nums:
#             if len(heap) < k:
#                 heapq.heappush(heap, num)
#             else:
#                 if heap[0] < num:
#                     heapq.heappop(heap)
#                     heapq.heappush(heap, num)

#         return heap[0]
