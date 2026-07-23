class Solution:
    def isCovered(self, ranges: List[List[int]], left: int, right: int) -> bool:

        for num in range(left, right + 1):
            is_covered = False
            
            for interval in ranges:
                start = interval[0]
                end = interval[1]
                
                if start <= num <= end:
                    is_covered = True
                    break  
            
            if not is_covered:
                return False
        
        return True
        