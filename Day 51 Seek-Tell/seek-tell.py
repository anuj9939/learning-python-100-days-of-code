import os
path = os.getcwd()+'\Day 51 Seek-Tell\\'
# with open(path+'file.txt', 'r') as f:
#     # Move to the 10th byte in the file
#     f.seek(10)
#     # Read the next 5 bytes
#     data = f.read(5)
#     print(data)

# with open(path+'file.txt', 'r') as f:
#     # Read the first 10 bytes
#     data = f.read(10)
#     print(data)
#     # Save the current position
#     current_position = f.tell()
#     # Seek to the saved position
#     f.seek(current_position)
#     print(f.read())
#     print(current_position)

with open(path+'sample.txt', 'w') as f:
    f.write('Hello World3!')
    f.truncate(5)

with open(path+'sample.txt', 'r') as f:
    print(f.read())
