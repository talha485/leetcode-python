found=False
numbers=[]
for i in range(5):
    num=int(input(f"Enter numbers{i+1}: "))
    numbers.append(num)
target=int(input("Enter number to check if it is found : "))
for num in numbers:
    if target == num:
        found=True
        break
if found:
    print("Target Found")
else:
    print("Target Not Found")
