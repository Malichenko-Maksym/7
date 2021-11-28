import stack

com=input('RPN: ')
for i in com:
    if i=='=': print(stack.pop())
    elif i==' ': continue
    elif i=='+': stack.push(int(stack.pop())+int(stack.pop()))
    elif i=='-': stack.push(-1*int(stack.pop())+int(stack.pop()))
    elif i=='/': stack.push(1/int(stack.pop())*int(stack.pop()))
    elif i=='*': stack.push(int(stack.pop())*int(stack.pop()))
    else: stack.push(i)