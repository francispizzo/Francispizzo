def findSum(x):
    sum = 0
    for i in range(x):
     sum=(i+sum+1)
    return(sum)
print(findSum(20))
