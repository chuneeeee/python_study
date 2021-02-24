import heapq
# heapq 를 사용하여 힙구현 
def solution(scoville, K):
    answer=0
    heap=[]
    for i in scoville:
        heapq.heappush(heap,i)
    while heap[0]<K :
        
        if len(heap)>=2:
            a=heapq.heappop(heap)
            b=heapq.heappop(heap)
        
            heapq.heappush(heap,a+(b*2))
            answer+=1
        else:
            return -1
    
    return answer



#https://programmers.co.kr/learn/courses/30/lessons/42626