
def a(arr ,target):
 low=0
 high=len(arr)-1
 while low<=high:
    mid=int((low+high)/2)
    if arr[mid]==target:
       return mid
    elif target>mid:
        low=mid+1
    elif target<mid:
        high=mid-1
 return -1
arr=[2,3,4,5]
target=10
f=a(arr,target)
if f!=-1:
   print(f)
else:
   print("not")
