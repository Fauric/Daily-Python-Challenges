# adds a number to the end of the string
# if number already at end of string, increase number by 1
def increment_string(strng):
    digit = ['0','1','2','3','4','5','6','7','8','9']
    last_num = ''
    if len(strng) == 0 or strng[-1] not in digit:
        return strng + '1'
    for i in strng[::-1]:
        if i in digit:
            last_num = i + last_num
            strng = strng[:-1]
        else:
            break
    new_num = (int(last_num) + 1)
    return strng + (str(new_num)).zfill(len(last_num))
