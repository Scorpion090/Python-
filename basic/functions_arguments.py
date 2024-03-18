'''
There are four types of arguments of functions - 
1.Default arguments - 
2.Keyword arguments - 
3.required arguments - 
4.Variable length arguments - 

''' 

# 1. Defaut arguments - 
def avg(a = 9,b = 1):
    print("The average is " ,(a+b)/2)
    
avg()
# if we provide the arguments then this will be ingnore the default values - 
avg(3,6)
avg(3,)

# Another example of default arguments - 
def info(f_name = "Rohan ",l_name = "Rathore"):
    print(f_name + l_name )
info(f_name  = "Vishal ")


# 2. keyword argument - 
l = [1,2,3,4,5,6,6,8]
def median(l):
   if(len(l)%2==0):
       a = len(l)//2
       return (l[a-1] + l[a])/2 
   else:  
       return len(l)/2 
ans = median(l)
print(ans)

# Now This is the keyword arguments - 
a = int(input("Enter the number here :"))
b = int(input("Enter the number here :"))
def mean(a,b):
    return (a+b)/2 
ans = mean(a,b)   # here a and b is keyword arguments - 
print(f"The mean of {a} and {b} is = {ans}")


# 3. Required arguments - Required arguments is must to add in the function otherwise function will not be work - 

def sm(a, b):# here a and b is required argument.It is must to give the value of a and b-
    return (a+b)
r = sm(1, 2)
print(r)

# 4.Variable length arguments  - 
def sum2(*args):
    result = 0
    for i in args:
        result = result + i
    print(result)
l = (1,2,3,3,4,5,5)
sum2(*l)






