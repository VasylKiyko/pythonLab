import random

#create my own fuction to fill the list))
def fill_list(size):
    List = []
    i = 0
    while i < size:
        List.append(random.randint(0, 100))
        i = i + 1
    return List

#Calculate summ of elements in list
def list_sum(List):
    sum = 0
    for x in List:
        sum = sum + x
    return sum


number = input("Enter size of list: ")
List = fill_list(int(number))
Sum = list_sum(List)
avg = Sum / float(number)
print("Sum of your list`s elements is " + str(Sum) + " and it`s average is " + str(avg))