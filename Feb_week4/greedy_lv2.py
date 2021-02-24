def solution(people, limit):
    answer = 0
    check=[0 for _ in people]

            
    people.sort(reverse=True)
    answer=len(people)
    start=0
    tmp=0
    end=len(people)-1
    while start<end:
        if people[start]+people[end]<=limit:
            start+=1
            end-=1
            tmp+=1
        else:
            start+=1
    return answer-tmp


#https://programmers.co.kr/learn/courses/30/lessons/42885