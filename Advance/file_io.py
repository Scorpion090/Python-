# f = open('pp.py','r')
# test = f.read()
# print(test)
# f.close()

f = open('myfile2.txt','w')
text = f.write("This is our main  file of myfile.txt")

# if we use of with keyword the we don't need  to close of the file it is automatically close file from with keyword - 
with open("myfile3.txt","w") as f:
    f.write("This is my third file")
    

