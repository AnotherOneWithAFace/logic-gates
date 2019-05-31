def main():
    
    print("This program emulates the function of a NOT logic gate.")
    print("Input 1 or 0 for the program to do its thing!")
    i = input()
    if i == "0":
        print("Your answer is: 1")
    elif i  == "1":
        print("Your answer is: 0")

    elif i != "0" or i != "1":
        print("You must enter 1 or 0!")
        

main()
