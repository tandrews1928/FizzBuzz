for i in range (1, 101):
    hit = False
    if (i % 3 == 0): #multiple of 3?
        print("Fizz", end = "") #the end = "" is so that there will be no newline
        hit = True
    if (i % 5 == 0): #multiple of 5?
        print("Buzz", end = "")
        hit = True
    if (not hit):
        print(i, end = "") #print number if not a multiple of 3 or 5
    print("") #newline