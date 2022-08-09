a=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16]
element=int(input())
ans=-1
for i in range(len(a)):
    if a[i]==element:
        ans=i
        break
if ans!=-1:
    
    print("ELEMENT FOOUND at {} position".format(ans))
else:
    print("Element not found")

The time complexity of the above algorithm is O(n). 
Auxiliary Space: O(1) for iterative and O(n) for recursive.
