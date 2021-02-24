from itertools import permutations 

def solution(numbers):
    answer=''
    #n = sorted(list(map(str, numbers)), key=lambda x: x*5, reverse=True)
    #print(n)
    num=[]
    for i in numbers:
        num.append(str(i))
        
    num=sorted(num,key=lambda x : x* 5,reverse=True)
    #print(num)
    for i in num:
        answer+=i
    answer=str(int(answer))
    return answer

#https://programmers.co.kr/learn/courses/30/lessons/42746