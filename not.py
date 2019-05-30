def main():
    
    print("This program emulates the function of a NOT logic gate.")
    print("Input 1 or 0 for the program to do its thing!")
    i = input()
    while i == "0":
        print("Your answer is: 1")
        break
    while i  == "1":
        print("Your answer is: 0")
        break

    if i == "20":
        print("You must enter 1 or 0!")
        
    if i == "3":
        print("You must enter either 1 or 0!")

main()
