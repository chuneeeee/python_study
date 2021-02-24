def solution(array, commands):
    answer=[]
    for t in commands:
        #print(t)
        tmp=array[t[0]-1:t[1]]
        tmp.sort()
        answer.append(tmp[t[2]-1])
        
    return answer


    # https://programmers.co.kr/learn/courses/30/lessons/42748