while True:
    n = int(input("Enter the value of number: "))
    if n < 0:
        print("we only allow positive number. please try again.")
        continue
    if n == 0:
        break
    print("square number", n, "is", n*n)
