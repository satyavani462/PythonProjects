import random
while True:
    print(random.randint(1,6))
    again=input("want to roll the dice again?(y/n)")
    if(again.lower()=="y"):
        continue 
    else:
        break