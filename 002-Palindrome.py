num=int(input("Enter number :"))
if num < 0:
    print("Number should greater than 0")
else:
    original = num
    reverse = 0
    while num > 0:
        digit = num % 10
        reverse = reverse * 10 + digit
        num = num // 10
    if original == reverse:
        print("Palindrome")
    else:
        print("Not Palindrome")
