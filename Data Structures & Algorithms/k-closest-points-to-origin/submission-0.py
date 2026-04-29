class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        ans = []
        distances = []
        hashMap = {}
        for i in points:
            x = i[0]
            y = i[1]
            e_distance = math.sqrt((x*x) + (y*y))
            hashMap[e_distance] = [x, y]
            heapq.heappush(distances, (-e_distance, [x, y]))
            if len(distances) > k:
                heapq.heappop(distances)
        for i in distances:
            ans.append(i[1])
        return ans
        