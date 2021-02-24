#16956 boj


R,C=map(int,input().split())
dx=[0,1,0,-1]
dy=[-1,0,1,0]
pasture=[list(input()) for _ in range(R)]
check=0
for i in range(R):
    for j in range(C):
        if pasture[i][j]=='.':
            pasture[i][j]='D'
        elif pasture[i][j]=='S':
            for k in range(4):
                new_i=i+dx[k]
                new_j=j+dy[k]
                if 0<=new_i<R and 0<=new_j<C:
                    if check==0 and pasture[new_i][new_j]=='W':
                        check=1
                        print(0)
        if check==1:
            break
    if check==1:
        break
if check==0:
    print(1)
    for i in pasture:
        print(''.join(i))


#https://www.acmicpc.net/problem/16956