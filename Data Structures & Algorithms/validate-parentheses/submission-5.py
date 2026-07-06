class Solution:
    def isValid(self, s: str) -> bool:
        st=[]
        for ch in s:
            if ch=='(' or ch=='[' or ch=='{':
                st.append(ch)
            elif (len(st)==0 and (ch=='}' or ch==']' or ch==')')):
                return False
            elif (ch==')' and st[-1]=='(') or (ch=='}' and st[-1]=='{') or (ch==']' and st[-1]=='['):
                st.pop()
            else :
                return False
            
            #print(st)

        if len(st)==0:
             return True
        else:
            return False 
            s="[(])"
            
        