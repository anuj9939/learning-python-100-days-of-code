
import os
path = os.getcwd()+'\Day 49 File Handling\\'


# WRITING A FILE

# f = open('myfile.txt', 'a')
# f.write('Hello, world!')
# f.close()

with open(path+'myfile.txt', 'a') as f:
    f.write("Hey I am inside with")

# READING A FILE
f = open(path+'myfile.txt', 'r')
# print(f)
text = f.read()
print(text)
f.close()
# print(path)
