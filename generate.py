with open("main.py", "a") as myfile:
    myfile.write("def isEven(number):\n")
    for i in range(2147483647):
        myfile.write("    if number == {}: return {}\n".format(i, i%2==0))
