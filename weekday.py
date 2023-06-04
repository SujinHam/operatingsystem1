# 요일 맞추기

m1,d1,m2,d2=map(int,input().split())
def function(m,d):
    days=[0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    total_days=0
    for i in range(1, m):
        total_days+=days[i]
    total_days+=d
    return total_days
diff=function(m2,d2)-function(m1,d1)
while diff<0:
    diff+=7
weekday=["Mon", "Tue", "Wed", "Thu", 'Fri', 'Sat', "Sun"]
print(weekday[diff%7])
