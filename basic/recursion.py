# Recursion - Again and again calling a function inside the function is called recursion .

# This will be not work because this is a infinite recursion function - 
num = int(input("Enter the number here:"))
def recur(num):
    return num * recur(num-1)
ans = recur(num)
print(ans)

# This  is correct - 
num = int(input("Enter the number here:"))
def recur(num):
    if(num == 0 or num == 1):
        return 1
    else:
        return num * recur(num-1)
ans = recur(num) 
print(ans)

# Calculate the fibonachi series - 
n = int(input("Enter the number here :"))
def fibo(num):
    a = 0
    b = 1
    for i in range(num):
        c = a + b 
        print(c)
        a = b
        b = c
fibo(n)

       
