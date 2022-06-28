


maximum_value = int(input("please enter maximum value"))
minumum_value = int(input("please enter minumum value"))


for num in range(minumum_value, maximum_value + 1) :
    if num > 1 :
        for i in range(2, num) :
            if (num%i)==0:
                break
        else:   
            print(num)
            
    
    










