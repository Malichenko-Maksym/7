import stack
num=int(input('Natural number: '))
while num>0:
    stack.push(num%2)
    num=num//2
k=''
for i in reversed(stack.stack):
    k=k+str(i)
print('Binary number:',k)
    

