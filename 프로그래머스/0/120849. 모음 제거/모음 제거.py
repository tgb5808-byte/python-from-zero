def solution(my_string):
    answer=""
    for num in my_string:
            if num not in "aeiou":
                answer+=num
    return answer