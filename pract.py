def nb_dig(n, d):
    num_list = []
    counter = 0
    for num in range(0, n+1): 
        num_list.append(str(num**2))
    for i in num_list:
        for j in i:
            if str(d) in j:
                counter += 1
    return counter

   

