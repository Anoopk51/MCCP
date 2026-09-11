'''
1. 
'''
# num = int(input("Enter the number "))
l=[2,3,4,5]
try :
    # print(l[len(l)])
    print(l[0])
    print("Error are not occur.")
except:
    print("Please resolve error")

'''
2.
'''

try:
    result = 10/0
except ZeroDivisionError:
    print("Cannot divide by zero.")
