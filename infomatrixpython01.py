#Q1] Write a Python Program to demonstrate-
#a]Replace the value of a key in a dictionary with a new updated value.
#b]Make a list of n integer elements -sort positive,negative,and zeros in different lists and return count and print each list.
#c]check if a value is present in dict

#a]
d = {'A': 100, 'B': 400, 'C': 600}
d.update({'A': 200})
print (d)

#b]

def sort_numbers(input_list):
    positive_numbers = []
    negative_numbers = []
    zeros = []
    for num in input_list:
        if num > 0:
            positive_numbers.append(num)
        elif num < 0:
            negative_numbers.append(num)
        else:
            zeros.append(num)
    positive_count = len(positive_numbers)
    negative_count = len(negative_numbers)
    zero_count = len(zeros)

    print("Positive numbers:", positive_numbers)
    print("Count of positive numbers:", positive_count)
    print("Negative numbers:", negative_numbers)
    print("Count of negative numbers:", negative_count)
    print("Zeros:", zeros)
    print("Count of zeros:", zero_count)
    return positive_count, negative_count, zero_count

n = int(input("Enter the number of elements: "))
input_list = []
for i in range(n):
    num = int(input(f"Enter element {i+1}: "))
    input_list.append(num)
positive_count, negative_count, zero_count = sort_numbers(input_list)

#c]

def is_value_present(dictionary, value):
    return value in dictionary.values()
my_dict = {'a': 1, 'b': 2, 'c': 3}
search_value = 2
if is_value_present(my_dict, search_value):
    print(f"{search_value} is present ")
else:
    print(f"{search_value} is not present ")

# Q2. Consider list1=[5,7,3,0,-9,1], make the following changes-
#-append 2
#-add -2 on the 2nd position
#-print the list in reverse
#-pop -9 
#-sort the list

list1 = [5, 7, 3, 0, -9, 1]
list1.append(2)
print(list1)
list1.insert(1, -2)
print(list1)
print(list1[::-1])
list1.remove(-9)
print(list1)
list1.sort()
print(list1)

#Q5. WAP to count the number of words in a string

def count_words(string):
    words = string.split()
    num_words = len(words)
    return num_words

input_string = "Tarun is always great"
word_count = count_words(input_string)
print("Number of words:", word_count)

#Q6. WAP to find the first 10 prime numbers using a user defined function

lower_value = int(input ("Please, Enter the Lowest Range Value: "))  
upper_value = int(input ("Please, Enter the Upper Range Value: "))  
  print ("The Prime Numbers in the range are: ")  
for number in range (lower_value, upper_value + 1):  
    if number > 1:  
        for i in range (2, number):  
            if (number % i) == 0:  
                break  
        else:  
            print (number)

#Q7. WAP to extract 5th, 7th,9th character from a string and merge it to form a new string/list.

def extract_merge(string):
    if len(string) >= 9:
        new_string = string[4] + string[6] + string[8]
        return new_string
    else:
        return "String is short"
input_string = "infomatrixxxxx"
result = extract_merge(input_string)
print("Input String:", input_string)
print("Merged characters:", result)

#Q8. Write a program to merge two lists having common element and remove the common element from the list.

def merge_lists_removecommon(list1, list2):
    set1 = set(list1)
    set2 = set(list2)
    common_elements = set1.intersection(set2)
    list1 = [xxx for xxx in list1 if xxx not in common_elements]
    list2 = [xxx for xxx in list2 if xxx not in common_elements]
    merged_list = list1 + list2
    return merged_list
list1 = [1, 2, 3, 4, 69]
list2 = [3, 4, 5, 6, 96]
merged_list = merge_lists_removecommon(list1, list2)
print("Merged list after removing common elements:", merged_list)

#Q4. str1 = 'I am 25 years and 10 months old'
#Remove all letters from the string and print the new string and 
#also the list/String containing the removed letters. 
#(Check Python doc for String functions else feel free to create user defined function)

str1 = 'I am 25 years and 10 months old'
removed_letters = ''
new_string = ''\
for char in str1:
    if char.isalpha():
        removed_letters += char  
    else:
        new_string += char  
print("New string without letters:", new_string)
print("Removed letters:", removed_letters)

#Q3. Write a Program to print the following pattern using for loop
#* * * * *
#* * * *
#* * *
#* *
#*
#* *
#* * *
#* * * *
#* * * * *

num_rows = 5
for i in range(num_rows, 0, -1):
    print("* " * i)


            














