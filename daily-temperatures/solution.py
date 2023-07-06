class Solution:
    def dailyTemperatures( temperatures ): 
        ans = []
        checked_temps=[]
        i = 0
        while len(temperatures) != 0:
            checked_temps.append(temperatures[i])
            i += 1
            if i == len(temperatures):
                while i > 0:
                    ans.append(0)
                    i -= 1
                return ans
            if temperatures[i] > checked_temps[0]:
                ans.append(len(checked_temps))
                temperatures.pop(0)
                checked_temps = []
                i = 0
                continue
            
        return ans

temperatures = [73,74,75,71,69,72,76,73]
Solution.dailyTemperatures(temperatures=temperatures)