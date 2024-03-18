# This is the program of creating the calculator for mathematical calculations.

num = int(input("Enter the number here:"))
num2 = int(input("Enter the number here:"))
sign  = input("Enter the sign here:")

if(sign=="+"):
    print("The sum of num and num2 is  = ",num+num2)
    
elif(sign=="-"):
    print("The subtract of num and num2 is  = ",num-num2)
elif(sign=="*"):
    print("The multiplication of num and num2 is  = ",num*num2)
elif(sign=="/"):
    print("The devision of num and num2 is  = ",num/num2)
elif(sign=="//"):
    print("The flor devision of num and num2 is  = ",num//num2)
    
