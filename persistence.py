def persistence(n):
    #function used to to find out how many times a number can be multiplied into itself. 
    #example: 27  2*7=14  1*4=4  answer: 2
    if n < 10:
        return 0
    why = True
    num = list(str(n))
    value = 1
    final_num = 0
    while why == True:
        for i in num:
            value = value*int(i)
        if value < 10:
            final_num += 1
            why = False
            return final_num
        else:
            final_num += 1
            num = list(str(value))
            value = 1
