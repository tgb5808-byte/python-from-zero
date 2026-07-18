def solution(array):
    answer =0
    max_c=0
    same=0
    for num in set(array):
        count=array.count(num)
        if count>max_c:
            max_c=count
            answer=num
            same=1
        elif count==max_c:
            same+=1
    if same>1:
        return -1
    
    return answer