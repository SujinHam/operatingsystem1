# 2개씩 그룹짓기

n=int(input())
arr=list(map(int,input().split()))
arr.sort()
groupmax=0
for i in range(n):
    groupsum=arr[i]+arr[2*n-1-i]
    if groupsum>groupmax:
        groupmax=groupsum
print(groupmax)
