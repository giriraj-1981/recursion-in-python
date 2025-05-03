n1=0
n2=1
print("Fibonacci sequence:")
for x in range(10):
       print(n1)
       x = n1 + n2
       # update values
       n1 = n2
       n2 = x
       
