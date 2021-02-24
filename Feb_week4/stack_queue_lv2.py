def solution(priorities, location):
    answer=0
    while 1:
        m=max(priorities)
        while m!=priorities[0]:
            priorities.append(priorities[0])
            del priorities[0]
            location-=1
            if location<0:
                location=len(priorities)-1
        
        if location==0:
            return answer+1
        else:
            answer+=1
            del priorities[0]
            location-=1
            if location<0:
                location=len(priorities)-1
            
    return answer



#https://programmers.co.kr/learn/courses/30/lessons/42587