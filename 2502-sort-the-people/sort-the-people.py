class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:

        """min_index = 0

        n = len(names)
        while min_index < n:
            curr_max = min_index
            for i in range(min_index,n):
                if heights[i] > heights[curr_max]:
                    curr_index = i
            heights[min_index], heights[curr_max] = heights[curr_max],heights[min_index]

            names[min_index], names[curr_max] = names[curr_max],names[min_index]

            min_index += 1
        return names"""

        """n = len(names)

        for i in range(1,n):
            index = i

            while index > 0 and heights[index] < heights[index - 1]:

                heights[index],heights[index - 1] = heights[index - 1],heights[index]
                names[index],names[index - 1] = names[index - 1],names[index]

                index -= 1

        return names"""

        """n = len(names)

        for i in range(1,n):
            index = i

            while index > 0 and heights[index] < heights[index - 1]:

                heights[index],heights[index - 1] = heights[index - 1],heights[index]
                names[index],names[index - 1] = names[index - 1],names[index]

                index -= 1

        return names[::-1]"""

       

        """for i in range(1,n):
            index = i

            while index > 0 and heights[index] > heights[index - 1]:

                heights[index],heights[index - 1] = heights[index - 1],heights[index]
                names[index],names[index - 1] = names[index - 1],names[index]

                index -= 1

        return names"""

        n = len(names)

        count = [0 for i in range(10**5 + 1)]

        for h in heights:
            count[h] += 1

        mapp = {heights[i]: names[i] for i in range(n)}
        result = []

        for i in range(10**5 + 1):
            if count[i] == 1:
                result.append(mapp[i])

        return result[::-1]

