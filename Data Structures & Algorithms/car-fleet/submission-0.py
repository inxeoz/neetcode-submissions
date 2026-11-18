class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        time_list = []

        for i, p in enumerate(position):
            tt =  ( target - p ) / speed[i]

            if tt == 0.0 :
                continue
            
            time_list.append((p, tt))
            # print(f"{target} - {p} / {speed[i]} ")
            # print(time_list)

        time_list.sort(key=lambda x : -x[0])
        # print(time_list)

        out = 0
        pt = 0.0
        for i, t in  enumerate ( time_list ):

            if pt < t[1]:
                out +=1
                pt = t[1]

            # print(pt, t[1], end="\n")
        
        return out