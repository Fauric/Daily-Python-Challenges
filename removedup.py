def array_diff(a, b): #takes the list a and removes all values existing in b
    answer = []
    for i in a:
        if i not in b:
            answer.append(i)
    return answer
