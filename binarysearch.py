In a nutshell, this search algorithm takes advantage of a collection of elements that is already sorted by ignoring half of the elements after just one comparison. 

Compare x with the middle element.
If x matches with the middle element, we return the mid index.
Else if x is greater than the mid element, then x can only lie in the right (greater) half subarray after the mid element. Then we apply the algorithm again for the right half.
Else if x is smaller, the target x must lie in the left (lower) half. So we apply the algorithm for the left half.


a=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16]
lower=0
element=int(input())
end=len(a)-1
found=-1
while(lower<=end):
    mid=(lower+end)//2
    if a[mid]==element:
        found=mid
        break
    if a[mid]<element:
        lower=mid+1
    else:
        end=mid-1
if found==-1:
    print("ELEMENT NOT FOUND")
else:
    print("ELEMENT FOUND AT",found)
    
