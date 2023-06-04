# 정렬된 숫자 위치 알아내기

class Number:
    def __init__(self, number, index):
        self.number, self.index=number, index
n=int(input())
arr=list(map(int,input().split()))
numbers=[]
numbers=[
    Number(num,i)
    for i, num in enumerate(arr)
]
answer=[
    0 for _ in range(n)
]
numbers.sort(key=lambda x: (x.number, x.index))
for i, number in enumerate(numbers):
    answer[number.index]=i+1
for i in range(n):
    print(answer[i], end=" ")
