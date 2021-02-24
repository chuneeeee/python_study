#2805 boj

N,M = map(int,input().split())
tree=list(map(int,input().split()))
start=0
end=max(tree)
ans=0
while start<=end:
  middle=(start+end)//2
  #print(f"{middle}:middle")
  cur=0
  for i in tree:
    cur+=max(i-middle,0)
  #print(middle, cur)
  if cur>=M:
    ans=max(ans,middle)
    start=middle+1
    #print("here")

  elif cur<M:
    end=middle-1


print(ans)

# https://www.acmicpc.net/problem/2805