class Solution:
	def evalRPN(self, tokens: list[str]):
		stack = []
		operands=set({ "+","-","/","*" })
		for token in tokens:
			if token in operands:
				val1 = stack.pop()
				val2 = stack.pop()
				res = int(eval("%s %s %s"%(val2,token, val1))	)
				stack.append(res)
			else:
				stack.append(token)
		return stack[0]


input = ["10","6","9","3","+","-11","*","/","*","17","+","5","+"]
solution = Solution()
solution.evalRPN(input)