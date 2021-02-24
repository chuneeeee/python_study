import sys
input=sys.stdin.readline
N,M = map(int,input().split())
tree=list(map(int,input().split()))
start=0
end=max(tree)

# 완전탐색 문제 
def func(start,end):
  ans=0
  while start<=end:
    middle=(start+end)//2
    cur=0
    for i in tree:
      if i>middle:
        cur+=i-middle
  # 현재 높이로 나무를 잘랐을 때 나오는 값 계산 
    
    if cur>=M:
      ans=middle
      start=middle+1
  # 나무길이가  목표보다 길다면 최적의 값을 위해 값을 위해
    elif cur<M:
      end=middle-1
  # 나무길이가  목표보다 짧다면 정답을 위해
  return ans
print(func(start,end))

# https://www.acmicpc.net/problem/2805