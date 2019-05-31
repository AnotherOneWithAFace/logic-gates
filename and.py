def main():
    print("This program emulates the functionality of an AND logic gate")
    print("Enter either a 1 or a 0, twice")
    x = input()
    y = input()
    if x == "0":
        bool1 = False
    else:
        bool1 = True
    if y == "1":
        bool2 = True
    else:
        bool2 = False
    
    if bool2 and bool1 == True:
        print("Your answer is: 1")
    else:
        print("Your answer is 0")
    
main()