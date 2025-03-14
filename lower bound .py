def a(arr,tar):
    low=0
    high=len(arr)-1
    ans=len(arr)
    while low<=high:
      mid=(low+high)//2
      if arr[mid]>=tar:
        ans=mid
        high=mid-1
      else:
        low=mid+1
    return ans
arr=[3,5,8,15,19]
tar=9
f=a(arr,tar)
print(f)
         
