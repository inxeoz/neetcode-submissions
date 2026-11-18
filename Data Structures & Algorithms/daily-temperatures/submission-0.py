class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:

        res = [0] * len(temperatures)
        st = []

        for i in range(len(temperatures)):

            while st and temperatures[i] > temperatures[ st[-1] ]:
                last_lower_index = st.pop()
                dif = i - last_lower_index
                res[last_lower_index] = dif
            
            st.append(i)
        return res



        