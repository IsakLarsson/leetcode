class Solution:
	def isValid(self, s:str) -> bool:
		stack = []
		pairs ={")":"(", "]": "[", "}":"{"}
		for c in s:
			if c not in pairs:
				stack.append(c)
				continue
			if not stack or stack[-1] != pairs[c]:
				return False
			stack.pop()
		return not stack


solution = Solution()
solution.isValid("()")