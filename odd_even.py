#Ask the user for a number.
#Depending on whether the number is even or odd, print out an appropriate message to the user.

# def odd_even(number):
#     if number%2==0:
#         print("The number is even")
#     else:
#         print("The number is odd")

# num = int(input('Enter a number:'))
# odd_even(num)

#********************************************************************************************************

#************************************************************************************

# odd even in list

# Lets say you have a list of numbers . Separate the list with even list and odd list

def odd_even(lst):
    even_list=[]
    odd_list=[]
    for x in lst:
        if x%2==0:
            even_list.append(x)
        else:
            odd_list.append(x)
    print(even_list)# even_list
    print(odd_list)

my_list = [2,4,7,9,3,1,6,8]
odd_even(my_list)
