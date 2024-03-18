num = int(input("Enter the any number here:"))
def squere(num):
    """ This function takes the user input andreturn the squere of user input :"""
    return num * num
ans = squere(num)
print(ans)
# We can print docstring something like this - 
print(squere.__doc__)

# We can only apply the docstring right above the function body and right below the function name otherwise docstring wil be not print .

PEP8 - 'Pep8 stands for "python inhensment proposal" which is used to maintain our python program.'

# The Zen of python - 
import this
