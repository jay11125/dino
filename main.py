import linear_search as ls
import binary_search as bn

print("Hi There . . . .")
print("1 -> Linear Search")
print("2 -> Binary Search")
try:
    no = int(input("Please enter the number of the function you want to perform from above functions -> "))
except ValueError:
    no = int(input("Please enter an integer"))
if no == 1:
    lst = input("Enter a list . . . ")
    print(f'Your list is = {lst}')
    num = input("Enter a number you want to linear search -> ")
    ls.lin_search(num, lst)
if no == 2:
    lst = input("Enter a list . . . ")
    print(f'Your list is = {lst}')
    num = input("Enter a number you want to binary search -> ")
    bn.bin_search(num, lst)

else:
    print("Please enter a valid number")


