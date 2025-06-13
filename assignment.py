# def remove_duplicates(lst):
#     return list(set(lst))

# print(remove_duplicates([1, 2, 2, 3, 4, 4, 5]))
# merge Two Dictionaries
# def merge_dict():
#     d1={'a':1,'b':2}
#     d2={'b':3,'c':4}
#     merged={**d1,**d2}
#     print(merged)
# merge_dict()    
#find max frequency character
# from collections import Counter
# s="helllo word"
# Counter=Counter(s)
# print(Counter.most_common(1))
#check anagram
# def is_anagram(s1,s2):
#     if (sorted(s1))==(sorted(s2)):
#         return True
# print(is_anagram("listen","silent"))        
        # flatten a Nested List
# def flatten(lst):
#     saty_list = []
#     for list in lst:
#         for item in list:
#             saty_list.append(item)
#     return saty_list

# print(flatten([[1, 2], [3, 4], [5]]))



# find second Largest Number
# def second_largest(numbers):
#     lst=[5,2,9,1,5,6]
#     lst.sort()
#     lst.pop()
#     return lst[-1]
# print(second_largest([5,2,9,1,5,6]))
# count Vowels in a string
# def count_vowels(s):
#     vowels=['a','e','i','o','u','A','E','I','O','U']
#     count=0
#     for ch in s:
#         if ch in vowels:
#              count=count+1
#     return count 
# print(count_vowels("Python is fun"))   
# nhi hua
# reverse dictinary
# def reverse_dict(d):
#     d={'a':1,'b':2}
#     reverse_dict = {value: key for key, value in d.items()}
#     return reverse_dict
# print(reverse_dict({'a':1,'b':2}))

#check if list is palindrome
# def is_palindrome(lst):
#         if lst==lst[::-1]:
#                 return True
#         else:
#                 return False
# print(is_palindrome([1,2,3,2,1]))

# tuple of squares
# def squares_tuple(n):
    
#     a=list()
#     for x in range(n):
#         a.append(x**2)
    # print(tuple(a))
# print(squares_tuple(5))
# def square_tuple(n):
#         return tuple([x**2 for x in range(n)])
# print(square_tuple(5))

# x = {
#     'a':[1,2,3,4 , {
#         '1':2,
#         '2':4,
#         '3':[1,2,3,4,5, {
#             '7':8,
#             '9':[10,11,12,13]
#         }]
#     }]

# }




# print(x['a'][4]['3'][5]['9'][3])
