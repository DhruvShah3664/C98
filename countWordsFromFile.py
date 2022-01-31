def countwff():
    s = input("enter the file name:" )
    nofw= 0
    file = open(s , "r")

    for line in file:
        words = line.split()
        nofw = nofw+len(words)
    print("Number of words: ")
    print(nofw)

countwff()