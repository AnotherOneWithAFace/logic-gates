def main():
    print("This program emulates the function of an OR logic gate")
    print("enter either 1 or 0 twice, not ANYTHING ELSE")
    x = input()
    y = input()
    if x == "1":
        bool0 = True
    elif x == "0":
        bool0 = False
    else:
        bool0 = "empty"        
    if y == "0":
        bool1 = False
    elif y == "1":
        bool1 = True
    else:
        bool1 = "empty"    
    if bool0 and bool1 == False:
        print("Your answer is: 0")
    elif bool0  == True or bool1 == True:
        print("Your answer is: 1")
        
main()    
    
    