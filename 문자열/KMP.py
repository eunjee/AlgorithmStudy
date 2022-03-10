#16916 부분 문자열 22-02-25
def get_pi(P):
    m = len(P)
    pi = [0 for i in range(m)]
    idx=0
    for i in range(1,m):
        while idx>0 and P[i]!=P[idx]:
            idx=pi[idx-1]
        if P[i]==P[idx]:
            idx+=1
            pi[i]=idx
    return pi
def kmp(S,P):
    n = len(S)
    m = len(P)
    pi = get_pi(P)
    print(pi)
    idx =0
    for i in range(n):
        while idx>0 and S[i]!=P[idx]:
            idx=pi[idx-1]
        if S[i]==P[idx]:
            if idx==m-1:
                return 1
            else:
                idx+=1
    return 0
if __name__=='__main__':
    S = input().strip()
    P = input().strip()
    print(kmp(S,P))