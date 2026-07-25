class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:

        n = len(names)

        mapp = {heights[i]:names[i] for i in range(len(names))}

        for i in range(n):

            for j in range(n - 1):
                if heights[j] < heights[j + 1]:
                    #heights[j],heights[j+1]=heights[j+1],heights[j]
                    #swap the hight
                    temp = heights[j]
                    heights[j]=heights[j+1]
                    heights[j+1]=temp


        

        sorted_name=[mapp[heights[i]] for i in range(n)]
        return sorted_name
