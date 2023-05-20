class Solution:
	def productExceptSelf(self, nums: List[int]) -> List[int]:
		print("not done")
		res = [1] * len(nums)
		prefix = 1
		for i in range(len(nums)):
			res[i] = prefix
			prefix *= nums[i]
		postfix = 1
		for i in range(len(nums)-1, -1, -1): #Reverse for loop syntax do be kinda weird
			res[i] *= postfix
			postfix *= nums[i]	
		return res