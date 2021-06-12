# 백준 2847번
N=int(input())
game=[int(input()) for _ in range(N)]

ans=0

# 그리디 문제, 뒤에서 부터 앞으로 가야한다.
for i in range(N-1,0,-1):
    if game[i-1]<game[i]: 
        continue
    ans+=game[i-1]-(game[i]-1)
    game[i-1]=game[i]-1

print(ans)    
