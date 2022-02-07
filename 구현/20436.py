#ZOAC3 22-02-07
import sys
input = sys.stdin.readline
keyboard = ['qwertyuiop', 'asdfghjkl', 'zxcvbnm']
mo = 'yuiophjklbnm'

left, right = input().rstrip().split()
strings = list(input().rstrip())

xl,yl,xr,yr=0,0,0,0
#시작 위치 구하기
for i in range(len(keyboard)):
    if left in keyboard[i]:
        xl = i
        yl = keyboard[i].index(left)

    if right in keyboard[i]:
        xr = i
        yr = keyboard[i].index(right)


time=0
#문자열 입력하는데 걸리는 시간 구하기
for string in strings:
    time+=1
    if string in mo: #모음이면 -> 오른손
        for i in range(len(keyboard)):
            if string in keyboard[i]:
                nx=i
                ny=keyboard[i].index(string)

                time+=abs(xr-nx)+abs(yr-ny)
                xr = nx
                yr= ny
                break
    else:
        for i in range(len(keyboard)):
            if string in keyboard[i]:
                nx=i
                ny=keyboard[i].index(string)
                time+=abs(xl-nx)+abs(yl-ny)
                xl = nx
                yl= ny
                break

print(time)