def tribonacci(signature, n):
    #this is a fibonacci sequence that adds the last 3 sequences instead of the last two sequences. 
    trilist = []
    if n <= 0:
        return []
    elif n <= 3:
        for i in range(n):
            trilist.append(signature[i])
        return trilist
    else:
        for i in range(n-3):
            a = signature[-3]
            b = signature[-2]
            c = signature[-1]
            signature.append(a+b+c)
        return signature
