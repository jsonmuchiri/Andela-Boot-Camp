def find_missing(first,second):
     #add the two lists

    add_list = first + second
    # checking whether the list contains only integers

    if all(isinstance(item, int) for item in add_list):    
        first_set=set(first)
        second_set=set(second)

        first_length = len(first_set - second_set)
        second_length = len(second_set - first_set)

        
        if (first_length)>1 or (second_length) > 1 or (second_length + first_length) > 1:
            print('The list should be different by only one extra number')
            
        else:
            if first_length > 0:
                print(list(first_set - second_set)[0])
                
            elif (first_length == 0) and (second_length == 0):
                print("0")
                
            else:
                print(list(second_set - first_set)[0])
                
    
    else:
        print('The arrays should only contain positive numbers')
       



