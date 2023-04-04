# input two nested structures. if both structures have the same information, return TRUE. even if they are structured differently. 

def same_structure_as(original,other):
    if type(original) != type(other):
        return False
    if len(original) == 0:
        print(original, other)
        return False
    if len(original) != len(other):
        return False
    for a,b in enumerate(original):
        if type(b) == type(other[a]):
            if type(b) == list and type(other[a]) == list:
                if len(b) != len(other[a]):
                    return False
                for c,d in enumerate(b):
                    if type(d) != type(other[a][c]):
                        return False
            continue
        elif type(b) == int and type(other[a]) == str:
            continue
        elif type(b) == str and type(other[a]) == int:
            continue
        else:
            return False
    return True
