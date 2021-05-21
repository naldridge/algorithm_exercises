

#Exercise 1 - Bubble Sort#


def sort_n_swap(nums):
    swapped = True
    while swapped:
        swapped = False
        for i in range(len(nums) - 1):
            if nums[i] > nums[i + 1]:
                nums[i], nums[i + 1] = nums[i + 1], nums[i]
                swapped = True
                print(nums)



list_of_nums = [6,3,2,1,4,5]
print(list_of_nums)
sort_n_swap(list_of_nums)
print("Sorted 'n Swapped!")


#Exercise 2 - Candies
('''
Given the list `candies` and the integer `extra_candies`, where `candies[i]` represents the 
number of candies that the `ith` kid has.
For each kid, check if there is a way to distribute the `extra_candies` amount to the kids 
such that they can have the greatest numhber of candies among them. Notice that multiple kids can 
have the greatest number of candies.


def kid_wins(nums):
    wins = True
    while wins:
        for i in range(len(nums))


candies = [2,3,5,1,3]
extra_candies = 3
expected output: [True,True,True,False,True]
''')
