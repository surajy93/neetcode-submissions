class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        result = [0] * n  # Initialize result array with 0s
    
        for i in range(n):
            for j in range(i + 1, n):
                if temperatures[j] > temperatures[i]:  # Find a warmer day
                    result[i] = j - i
                    break  # Stop once we find the next warmer day
        return result