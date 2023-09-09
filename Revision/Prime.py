for i in range(2,1001):
    for j in range (i-1,2,-1):
        if i%j == 0 :
            break
    print(i)
        
        