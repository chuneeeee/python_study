N=int(input())
game=[int(input()) for _ in range(N)]

ans=0
for i in range(N-1,0,-1):
    if game[i-1]<game[i]: 
        continue
    ans+=game[i-1]-(game[i]-1)
    game[i-1]=game[i]-1

print(ans)    
