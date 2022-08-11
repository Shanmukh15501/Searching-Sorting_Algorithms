a=[4,3,2,1]
for i in range(len(a)-1):
    swapped=False
    for j in range(len(a)-i-1):
        if a[j]>a[j+1]:
            temp=a[j]
            a[j]=a[j+1]
            a[j+1]=temp
            swapped=True
    if swapped==False:
        break
print(a)

Output=[1,2,3,4]

For better explination watch 
CODE BASICS YOUTUBE CHANNEL 

DATA STRUCTURES WITH PYTHON PLAYLIST

Time Complexity:  O(n2).

Auxiliary Space: O(1).
