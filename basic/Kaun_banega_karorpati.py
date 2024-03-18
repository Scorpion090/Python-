print("Que - 1. Who is the prime minister of India?")
l1 = ["Narendra modi","Soniya gandhi","Atal bihari wajpeyi","Rahul gandhi"]
ans = input("Enter the you answer here :")

Amount = 0
if(ans == "Narendra modi"):
    Amount = Amount + 100000
    
    print("Que - 2. Who is the chief minister of Madhya pradesh?")
    l2 = ["Shivraj singh chohan","Mohan yadav","Diraj singh","Vishal kumar"]
    
    ans2 = input("Enter the you answer here :")
    if(ans2 == "Mohan yadav"):
        Amount = Amount + 200000
        print("You have win the game you can take you amount", Amount)
    else:
        print("Wrong answer!","You can take Amount" , Amount)
    
else:
    print("Wrong answer!","You can take Amount" ,Amount)
