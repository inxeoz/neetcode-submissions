class Solution:
    def isValid(self, s: str) -> bool:


        st = []

        for c in list(s):
        
            if c in [ '(',  '{',  '[' ]:
                st.append(c)

            else:
                if len(st) > 0 :
                    top = st[-1] + '' + c
                    if top in ['()', '[]', '{}']:
                        st.pop()
                    else:
                        return False
                        
                else:
                    st.append(c)


        return len(st)  == 0     

        