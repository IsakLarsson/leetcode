class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        values = {}
        res=[]
        for num in nums:
            values[num] = values.get(num,0)+1 
        
        for i in range(k):
            max_value_key = max(values, key=values.get)
            values.pop(max_value_key)
            res.append(max_value_key)

        return res
