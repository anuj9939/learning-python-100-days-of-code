import time

timestamp = time.strftime('%H:%M:%S')
print(timestamp)
hour = int(time.strftime('%H'))
# print(timestamp)
minute = time.strftime('%M')
# print(timestamp)
second = time.strftime('%S')
# print(timestamp)
# if(hour>=0 | hour<12): 
#     print("Good Morning")
# elif(hour>=12 | hour<16):
#     print("Good After noon")
# elif(hour>=16 | hour<19):
#     print("Good Evening")
# elif(hour>=19 | hour<24):
#     print("Good Night")
# else:
#     print("Good Day")

if (0<=hour<12):
    print("Good Morning Sir")
elif (12<=hour<16):
    print("Good Afternoon Sir")
elif (16<=hour<19):
    print("Good Evening Sir")
elif (19<=hour<24):
    print("Good Night Sir")