try:
    total =  3/0
except ZeroDivisionError:
    print("Zero Divison error throw.")

try:
    num = int("Anoop Kushwaha")
except ValueError:
    print("Invalid number")
print("Hi Anoop")