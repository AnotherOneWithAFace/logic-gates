def main():
    print("This program emulates the functionality of an AND logic gate")
    print("Enter either a 1 or a 0, twice")
    print("Don't enter anything other than 1 or 0")
    x = input()
    y = input()
    if x == "0":
        bool1 = False
    elif x == "1":
        bool1 = True
    if y == "1":
        bool2 = True
    elif y == "0":
        bool2 = False
    
    if bool2 and bool1 == True:
        print("Your answer is: 1")
    elif bool1 == True and bool2 == False or bool2 == True and bool1 == False:
        print("Your answer is: 0")
    elif bool1 and bool2 == False:
        print("Your answer is: 0")
    elif bool1 or bool2 == False:
        print("Your answer is: 0")

main()