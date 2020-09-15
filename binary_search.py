def bin_search(number, list):
    list = sorted(list)
    l = 0
    u = len(list) - 1
    while l < u:
        mid = (l + u)//2
        if list[mid] == number:
            print(f'Found at position {(mid + 1)//2}')
            break
        else:
            if list[mid] < number:
                l = mid + 1
            else:
                u = mid - 1
    else:
        print("Not Found ")