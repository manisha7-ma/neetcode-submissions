class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack=[]
        for token in tokens:
            if token=='+' :
                stack.append(stack.pop() + stack.pop())
            elif token=='-':
                a=stack.pop()
                b=stack.pop()
                stack.append(b - a)
            elif token=='/':
                a=stack.pop()
                b=stack.pop()
                stack.append(int(b/a))
            elif token=='*':
                stack.append(stack.pop() * stack.pop())
            else :
                stack.append(int(token))
        if len(stack)==1:
            return stack.pop()
        else :
            token=stack.pop()
            a=stack.pop()
            b=stack.pop()
            if token=='+':
                return a+b
            elif token=='-':
                return b-a
            elif token=='/':
                return int(b/a) 
            else:
                 return a*b

            




        