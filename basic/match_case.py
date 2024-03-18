# Match_Case = We have a if-else statement but we can also use of match statement in python because it is provide the more and clear output that use can easily understant.

num = int(input("Enter the number here :"))
match num:
    case 0:
        print("This is the case_no. 0")
    case 1:
        print("This  is the case_no.1")
    case 2:
        print("This is the case_no.2")
    case 3:
        print("This is the case_no.3")
    case 4:
        print("This is the case_no.4")
    case 5:
        print("This is the case_no.5")
    case _:
        print("This is the default case")
        
# We can error handling here - 

try:
    num = int(input("Enter the number here :"))
    match num:
        case 0:
            print("This is the case_no. 0")
        case 1:
            print("This  is the case_no.1")
        case 2:
            print("This is the case_no.2")
        case 3:
            print("This is the case_no.3")
        case 4:
            print("This is the case_no.4")
        case 5:
            print("This is the case_no.5")
        case _:
            print("This is the default case")
except Exception as e:  
    print("String is not valid here so please input the integer here :")
    
