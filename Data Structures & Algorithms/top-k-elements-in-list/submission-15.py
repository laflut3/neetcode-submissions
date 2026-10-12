class Solution:

    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        topTab = []
        count: Dict = {}

        for num in nums :
            count[num] = count.get(num, 0) +1
        
        for i in range(0, k):
            res = max(count, key=count.get)
            count.pop(res)
            topTab.append(res)

        return topTab