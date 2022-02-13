#스위치 켜고 끄기 22-02-13
from collections import deque
import sys
input = sys.stdin.readline

def male_switch(num):
    for i in range(num,n+1,num):
        if switch[i]==0:
            switch[i]=1
        else:
            switch[i]=0

def female_switch(num):
    count = min(num,n-num+1)
    for i in range(0,count):
        if switch[num-i]==switch[num+i]:
            if switch[num-i]==0:
                switch[num-i]=switch[num+i]=1
            else:
                switch[num-i]=switch[num+i]=0
        else:
            break


n = int(input())
switch=[0]+list(map(int,input().split()))
student=deque()
m= int(input())
for _ in range(m):
    sex,num = map(int,input().split())
    student.append((sex,num))

while student:
    sex,num = student.popleft()
    if sex==1:
        male_switch(num)
    else:
        female_switch(num)

if n>20:
    for i in range(1,n+1,20):
        if n+1-i<=20:
            print(*switch[i:])
        else:
            print(*switch[i:i+20])
else:
    print(*switch[1:])