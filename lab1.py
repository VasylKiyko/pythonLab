import random

#create my own function to fill the list))
def fill_list(size):
    return [random.randint(0, 100) for x in range(size)]


#Calculate summ of elements in list
def list_sum(List):
    sum = 0
    for x in List:
        sum = sum + x
    return sum

if __name__ == '__main__':
    number = input("Enter size of list: ")
    List = fill_list(int(number))
    Sum = list_sum(List)
    avg = Sum / float(number)
    print("Sum of your list`s elements is " + str(Sum) + " and it`s average is " + str(avg))
