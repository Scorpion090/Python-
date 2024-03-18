a = 10   # global variable 
def func():
    global a
    a = 7     # Local variable
    print(a)
func()
print(a)