a = [[1,2,3],
     [4,5,6]]
## one way to traverse a 2d list
#for i in range(len(a)):
#    for j in range(len(a[i])):
#        print(a[i][j],end=' ')
#    print()

##another way
#def print_2dlist(lst):
#for row in a:
#    for element in lst:
#        print(element,end=' ')
#    print()

#add all elements
#sum = 0
#for i in range(len(a)):
#    for j in range(len(a[i])):
#        sum += a[i][j]      
#print(sum)

#sum = 0
#for row in a:
#    for element in row:
#        sum += element
#print(sum)

#for i in range(len(a)):
#    for j in range(len(a[i])):
#        a[i][j] += 1
#print(a)



#x = [[0] * 5]*8 DOES NOT WORK!!!!
m = 5
n = 8
x = [[0]*n for i in range(m)]
x[0][0] = 100

print(x)







