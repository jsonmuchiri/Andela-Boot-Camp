def find_min_max(a_list):
    """
    # make it a set to avoid duplication
    # Turn it back to a list for sort operation
    # sort the new list and assign min to [0] and max[-1]
    """
    make_set = set(a_list)
    new_list = list(make_set)

    sort_list = sorted(new_list)
    mini = sort_list[0]
    maxi = sort_list[-1]

    if mini == maxi:
        # if a list contains the same number,return number of items in it
        return [len(a_list)]
    else:
        min_and_max = [mini, maxi]
        print(min_and_max)


est = find_min_max([7, 70, 7, 7])
print(est)
