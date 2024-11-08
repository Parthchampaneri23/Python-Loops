#Python program to check if a given number is an Armstrong number


def is_armstrong(num):
    num_str = str(num)
    n = len(num_str)
    sum = 0
    for digit in num_str:
        sum += int(digit) ** n
    return sum == num

num = int(input("Enter a number: "))
if is_armstrong(num):
    print(f"{num} is an Armstrong number")
else:
    print(f"{num} is not an Armstrong number")
