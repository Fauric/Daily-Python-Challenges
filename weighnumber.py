# weighs a number by the numbers within it. 
# example: 99 weighs 18 and 273 weighs 12.
def order_weight(strng):
    ref_list = []
    new_strng = ""
    strng2 = strng.split()
    strng2.sort()
    for i in strng2:
        num = 0
        for x in i:
            num += int(x)
        ref_list.append( (num , i) )
    ref_list.sort()
    for i in ref_list:
        new_strng += i[1] + " "
    return new_strng[:len(new_strng)-1]
