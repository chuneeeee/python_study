# 9184 
# dp 

w=[[[0 for _ in range(101)] for _ in range(101)] for _ in range(101)]
for i in range(101):
        for j in range(101):
            for k in range(101):
                if i<=50 or j<=50 or k<=50:
                    w[i][j][k]=1
                elif i>70 or j>70 or k>70:
                    # w[20][20][20] 하면 틀림 ㅋㅋㅋ 
                    # 꼼수로 하드코딩 해버렸다!
                    w[i][j][k]=1048576
                elif i<j and j<k:
                    w[i][j][k]=w[i][j][k-1]+w[i][j-1][k-1]-w[i][j-1][k]
                else:    
                    w[i][j][k]=w[i-1][j][k]+w[i-1][j-1][k]+w[i-1][j][k-1]-w[i-1][j-1][k-1]



while 1:
    a,b,c=map(int,input().split())
    if a==-1 and b==-1 and c==-1 :
        break
    a+=50
    b+=50
    c+=50
    print(f"w({a-50}, {b-50}, {c-50}) = {w[a][b][c]}")
