f="experience.txt"
with open(f,"w")as file:
    file.write("Day 1: started\n")
    file.write("Day 2: networks")

with open(f,"r")as file:
    for i in file:
        print(i)
