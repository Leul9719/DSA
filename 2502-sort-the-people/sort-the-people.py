class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:

        n = len(names)

        mapp = {heights[i]:names[i] for i in range(len(names))}

        # worse case, I will have to do n passes
        for i in range(n):
            # bubble sort
            for j in range(n - 1):
                if heights[j] < heights[j + 1]:
                    #temp = arr[0]
                    #arr = [[1,8,7]]
                    #arr[0]=arr[1]
                    #arr[1]=arr[0]
                    #arr[0],arr[1]=arr[1],arr[0]
                    temp = heights[j]
                    heights[j]=heights[j+1]
                    heights[j+1]=temp
        

        sorted_name=[mapp[heights[i]] for i in range(n)]
        return sorted_name
