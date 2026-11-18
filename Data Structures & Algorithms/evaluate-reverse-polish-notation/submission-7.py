class Solution:
    def evalRPN(self, tokens: List[str]) -> int:

        st = []

        for t in tokens:
            if t in  ["+", "-", "*", "/"]:
                right = st.pop()
                left = st.pop()

                match t:
                    case "+":
                        st.append(left + right )
                    case "-":
                        st.append(left - right)
                    case "*":
                        st.append( left * right)
                    case "/":
                        import math
                        st.append(math.trunc( left / right) )
            else:

                n = int(t)
                st.append(n)

        return  st[-1]  
                
        