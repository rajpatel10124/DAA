def superReducedString(s):
    stack = []
    
    for char in s:
        if stack and stack[-1] == char:
            stack.pop()  
        else:
            stack.append(char)
    
    result = ''.join(stack)
    return result if result else "Empty String"

 
s = input()
print(superReducedString(s))
