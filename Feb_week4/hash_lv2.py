def solution(phone_book):
    answer = True
    phone_book.sort()
    l=len(phone_book)
    for i in range(l):
        for j in range(i+1,l):
            if phone_book[i] in phone_book[j]:
                return False
    
            
        
    return answer
    
    
    
#https://programmers.co.kr/learn/courses/30/lessons/42577