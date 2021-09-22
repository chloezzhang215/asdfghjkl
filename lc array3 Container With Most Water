# Container With Most Water
# TIME LIMIT EXCEEDED    O(n^2)
class Solution:
    def maxArea(self, height: List[int]) -> int:
        area_array = []
        for i in range(0,len(height)):
            n = 0
            while n <= len(height)-i-2:
                area = min(height[i+n+1],height[i])*(n+1)
                area_array.append(area)
                n = n + 1
        return max(area_array)



class Solution:
    def maxArea(self, height: List[int]) -> int:
        MAX = 0 
        x = 0
        y = len(height) - 1
        while x != y:
            area = min(height[x],height[y]) * (y - x)
            MAX = max(MAX, area)
            
            if height[x]<height[y]:
                x += 1
            else :
                y -= 1
         
        return MAX
        
        
        
