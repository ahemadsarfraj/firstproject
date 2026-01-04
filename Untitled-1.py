
#qus3
#data=input("My name is:")
#print(data)
#data=input("enter your name:")
#print("my name is:",)
#a=int(input("first thing:"))
#b=int(input("second thing:"))
#c=int(input("third thing:"))
#print("the sum is=",a+b%c)
# num=int(input("first thing:"))

# if num%2==0:
#     print("even")
# else:
#     print("odd")
# num=int(input("first thing:"))

# if num>0:
#      print("positive")
# # elif num<0:
# #      print("negetive")
# else:
#      print("zero")
# age=int(input("enter your age:"))
# if age>=18:
#     print("you can vote")
# else:
#     print("you cant vote")
# for i in range(0,20):
#     print(i)
# num=int(input("enter a number:"))
# for i in range(1,10):
#     print(f"{num} + {i} = {num*i}")
# total=0
# for i in range(2, 100):
#     total=-i
# #     print("the sum is =", total)
# n=10
# total=n*(n-1)//2
# print ("the sum is =", total)
# /my_list = [1,2,5,4,5]
# total=0
# for num in my_list:
#     total +=num
#     print(total)
# my_list = [1,2,5,4,5]
# print(max(my_list))
# print(min(my_list))
# def add(a,b):
#     return a+b
# result=add(50, 70)
# print(result)
def factorial(n):
    fact =1
    for i in range(2 ,n+1):
        fact *=i
    return fact
print(factorial(5))