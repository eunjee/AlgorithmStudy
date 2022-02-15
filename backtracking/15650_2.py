# 순열 직접 구현

def permutaions(n,m):
    if len(result)==m:
        print(' '.join(map(str,result)))
        return
    for i in range(1,n+1):
        if i not in result:
            result.append(i)
            permutaions(n,m)
            result.pop()

def combinations(n,m,curr):
    if len(result)==m:
        print(' '.join(map(str,result)))
    for i in range(curr,n+1):
        if i not in result:
            result.append(i)
            combinations(n,m,i)
            result.pop()

if __name__=='__main__':
    n,m = map(int,input().split())
    result=[]
    #permutaions(n,m)
    combinations(n,m,1)