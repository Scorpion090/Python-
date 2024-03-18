with open("myfile3.txt","r") as f:
    i = 0
    while True:
        i = i + 1
        file = f.readline()
        if not file:
            break
        m1 = file.split(",")[0]
        m2 = file.split(",")[1]
        m3 = file.split(",")[2]
        print(f"Marks of student {i} in maths is {m1}")
        print(f"Marks of student {i} in English is {m2}")
        print(f"Marks of student {i} in physics is {m3}")
