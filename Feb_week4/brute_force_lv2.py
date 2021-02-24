
from itertools import permutations
def is_prime(num):
    for i in range(2,int(num**0.5)+1):
        if num%i==0:
            return False
    return True
def solution(numbers):
    answer = 0
    
#     num_list=list(numbers)
#     num_set=[]
#     for i in range(1,len(num_list)+1):
#         tmp=list(permutations(num_list,i))
#         k=[]
#         for j in tmp:
#             k.append(int(''.join(j)))
        
#         num_set+=k
#     num_set=set(num_set)
#     num_set=list(num_set)
#     cnt=0
    
#     for num in num_set:
#         if int(num) >1 and is_prime(int(num)):
#             cnt+=1
#     answer=cnt



    #에라토스 테네스의 체를 써보기 
    num_list=list(numbers)
    a=[]
    for i in range(1,len(num_list)+1):
        k=list(set(permutations(num_list,i)))
        for j in k:
            a.append(int(''.join(j)))
    a=list(set(a))  
    #print(a)
    m_prime=max(a)
    cnt=0
    is_prime=[False,False]+[True]*(m_prime-1)
    for i in range(2,m_prime+1):
    
        if is_prime[i] and i in a:
            #print(i)
            cnt+=1
            
        for j in range(i*2,m_prime+1,i):
            is_prime[j]=False
        
    answer=cnt
    return answer

# https://programmers.co.kr/learn/courses/30/lessons/42839