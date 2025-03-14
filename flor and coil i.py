def a(arr,tar):
    low=0
    high=len(arr)-1
    while low<=high:
        mid=int((low+high)/2)
        if arr[mid]>=tar:
            ans=mid
            ans1=mid-1
            high=mid-1
        else:
            low=mid+1
    return arr[ans1],arr[ans]
arr=[3,4,4,7,8,10]    
tar=8
a1=a(arr,tar)
print(a1)
if tar not in arr:
  print(a1)
else:
    print(tar,tar)