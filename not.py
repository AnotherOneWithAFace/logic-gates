def intro():
    print("This program emulates the functionality of a NOT gate")
    print("Input 1 or 0 for the program to do its thing!")
   
 
def repeat(i):
    if i != "1" or i != "0":
        print("You need to enter either 1 or 0!")
        main()

def main():
    intro()
    i = input()
    if i == "0":
        print("Your answer is: 1")
    elif i  == "1":
        print("Your answer is: 0")

    else:
        repeat(i)


main()