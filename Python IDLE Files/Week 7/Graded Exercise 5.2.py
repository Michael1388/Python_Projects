
largest = None
smallest = None
while True:
    num = input("Enter a number: ")
    if num == "done":
        break
    try:
        fval = float(num)
    except:
        print('Invalid input')
    print(num)

print("Maximum", largest)
print("Minimum", smallest)