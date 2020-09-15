def lin_search(num, lst):
    n = 0
    for i in lst:
        n = n + 1
        if i == num:
            print(f'Found at position {n}')
            break
    else:
        print("Not Found")



