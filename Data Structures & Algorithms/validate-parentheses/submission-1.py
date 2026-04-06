class Solution:
    def isValid(self, s: str) -> bool:
        st = []
        for b in s:
            if b in ['}', ']', ')']:
                if len(st)>0:
                    if b == '}' and st[-1]=='{':                
                        st.pop()
                    elif b == ']' and st[-1]=='[':                
                        st.pop()
                    elif b == ')' and st[-1]=='(':                
                        st.pop()
                    else:
                        return False
                else:
                    return False

            else:
                st.append(b)
        if st == []:
            return True
        return False