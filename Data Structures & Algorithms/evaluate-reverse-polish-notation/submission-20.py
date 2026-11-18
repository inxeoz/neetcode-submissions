class Solution:
    def evalRPN(self, tokens: List[str]) -> int:

        st = []

        for t in tokens:
            if t in  ["+", "-", "*", "/"]:

                match t:
                    case "+":
                        st.append(st.pop() + st.pop())
                    case "-":
                         st.append( -1 * st.pop() + st.pop())
                    case "*":
                         st.append(st.pop() * st.pop() )
                    case "/":
                        import math
                        right  = st.pop()
                        st.append(math.trunc( st.pop()  / right) )
            else:

                n = int(t)
                st.append(n)

        return  st[-1]
                
        