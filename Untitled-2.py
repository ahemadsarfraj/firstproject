# n=123456789
# total=0

# while n>1:
#     total = n%10
#     n//=10
#     print("the sum is =", total)
# n=12345
# print(sum(int(d) for d in str(n)))
# s=12345
# print(sum(int(d) for d in str(s)))
# n=1234522222222222
# s=str(n)
# print(len(s))
# print(s.count('2'))
# from collections import Counter
# print(Counter(s))
# # total=0
# while n>0:
#     total += 1
#     n//=10
#     print(total)
# n=567
# total=0
# while n>0:
#     total +=1
#     n//=10
#     print(total)
# n = "ahmadadbad"
# count =0
# for ch in n:
#     if ch in 'a':
#         count +=1
#         print( count)
# s="ahmadadbad"
# print(s.count('d'))
# s= "madam"
# rev="" 
# for ch in s:
#     rev= ch +rev
#     if s==rev:
#         print("palindrome")
#     else:
#         print("not palindrome")
# s = "sar123"
# total=0
# for ch in s:
#     if ch.isdigit():
#         total += int (ch)
#         print("sum=", total)
s = ("a man , a plan , a canal: panama")
clean=""
for ch in s:
    if ch.isalnum():
        clean += ch.lower()

        if clean == clean[::-1]:
            print("palindrome")
        else:
            print("not palindrome")