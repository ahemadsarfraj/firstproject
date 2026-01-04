# # while True:
# #     num=int(input("enter the number: "))
# #     if num%8 ==0:
# #         print("divinal")
# #     else:
# #         print("nondivinal")

# # for i in range(9, 12):
# #     print(i)
# # i =1
# # while i<=10:
# #     print(i)
# #     i+=1
# for i in range(1, 51):
#     if i % 3 == 0 and i % 5 == 0:
#         print("FizzBuzz")
#     elif i % 3 == 0:
#         print("Fizz")
#     elif i % 5 == 0:
#         print("Buzz")
#     else:
#         print(i)

# text = input("enter the string: ")
# vowels = "aeiou"
# count = 0
# for ch in text.lower():
#       if ch in vowels:
#       count += 1
# print("number of vowels:", count)
# text = input("enter the string:")
# vowels = "aeiou"
# count = 0
# for ch in text.lower():
#     if ch in vowels:
#         count +=1
#         print("numbers of vowels:", count)
# def count_vowels(text):
#      vowels = "aeiou"
#      count = 0
#      for ch in text.lower():
#          if ch in vowels:
#              count +=1
#              return count
#              print(count_vowels("text"))
# text = input("Enter the string: ")
# vowels = "aeiou"
# count = 0

# for ch in text.lower():
#     if ch in vowels:
#         count += 1
#         print("Vowel found:", ch, " | Count:", count)
# names = ["Ali", "Ahmed", "Sara"]
# for name in names:
#     print(name)

# word = (input("inter the name:"))

# for ch in word:
#     print(ch)
# a = {1, 2, 3}
# b = {3, 4, 5}

# print(a | b)   # Union
# print(a & b)   # Intersection
# print(a - b)   # Difference
# def merge_sorted_lists(list1, list2):
#     i=0
#     j=0
#     result=[]
#     while i < len(list1) and j < len(list2):
#         if list1[i] < list2[j]:
#             result.append(list1[i])
#             i+=1
#         else:
#             result.append(list2[j])
#             j+=1

#     while i < len(list1):
#         result.append(list1[i])
#         i += 1

#     while j < len(list2):
#         result.append(list2[j])
#         j += 1        
    
#     return result
# list1 = [1, 3, 5, 7]
# list2 = [2, 4, 6, 8]

# print(merge_sorted_lists(list1, list2))
# def my_function(fname):
#     print(fname + " refness")
# name = ["ali", "ahmad", "sara"]
 
# for name in name:
#     my_function(name)
# def my_function(name):
#     print("hello", name)

# my_function("email")
# def my_function(fname, iname):
#     print(fname + "", iname)

# my_function("sarfraj", "ansari")
# def my_function(name  = "sarfraj"):
#     print("my name is", name)

# my_function("email")
# my_function()
# def my_function(name , animal):
#     print(" i have a" , animal)
#     print("my", animal + "s name is", name)

# my_function("gasper" , "dog")
# def my_function(name , age , animal):
#     print("i hvea a" , age, "year old", animal , "named", name)
    
# my_function("dog" , 5, "gasper") 
# def my_function(fruits):
#   for fruit in fruits:
#     print(fruit, end=" ")  

# my_fruits=["apple", 'bsna']
# # my_function(my_fruits)
# def my_function(a , b):
#     return a + b
    
# sum = my_function(4, 5)    
# print(sum)
# sum = my_function(7, 5)    
# print(sum)
# def my_function(a , b):
#   return a*b

# x = int(input("enter first number:"))
# y = int(input("enter secound number:"))
# print(my_function(x , y))
# def remove_duplicates(list):
#     seen =set ()
#     result =[]
#     for item in list:
#       if item not in seen:
#         result.append(item)
#         seen.add(item)
#     return result
# print(remove_duplicates([1, 2 , 2 , 3 , 4 , 5 , 5 , 6 ]))
# print(remove_duplicates([1,1,2,3,4,5,5,5,6,6,7,7]))      

def remove_duplicates(list):
    seen = set()
    result = []
    for item in list:
        if item not in seen:
            result.append(item)
            seen.add(item)

    return result
user_input = input("inter the numbers:")
print(remove_duplicates(user_input))    
number = list(map(int, user_input.split(",")))