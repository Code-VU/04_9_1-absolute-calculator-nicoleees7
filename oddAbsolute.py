def calculateAbsolute():
    # This first line is provided for you
    in_num  = input("Enter a number: ")

    if int(in_num) < 21:
        diff = abs(int(in_num) - 21)
    else:
        diff = abs((int(in_num) - 21) * 2)

    print("Result:", diff)
    # end assignment

## If you want to test locally run > python payCalculator.py

if __name__ == "__main__":
    calculateAbsolute()
