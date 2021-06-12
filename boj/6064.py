
# 6064번 

#  브루트 포스로 풀면 틀리는 문제 
# 규칙을 찾아야 한다 
T=int(input())
for _ in range(T):
    M,N,x,y=map(int,input().split())
    
    ans=x
    # 정답 k - x % M = 0 
    # 정답 k - y % N = 0 
    # 인 k 값을 찾는다 ?
    '''
    K 는 M의 배수  이므로 x에서 M 씩 더해나간다 

    
    '''
    check=1
    while ans<=M*N:
        if (ans-y)%N==0:
            print(ans)
            check=0
            break

        ans+=M
    if check:
        print(-1)
