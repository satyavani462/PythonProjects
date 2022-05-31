import random
print("!!!******snake-water-gun*******!!!")
n=int(input("enter no.of rounds you wanna play..."))
options=['s','w','g']
c=0
u=0
round=1
while(round<=n):
    user=input("enter your choice:")
    comp=random.choice(options)
    print("comp==",comp)
    if(comp=='s'):
        if(user=='w'):
            c+=1
        elif(user=='g'):
            u+=1
    elif(comp=='g'):
        if(user=='s'):
            c+=1
        elif(user=='w'):
            u+=1
    elif(comp=='w'):
        if(user=='s'):
            u+=1
        elif(user=='g'):
            c+=1
    if(u>c):
        print("you won")
    elif(u<c):
        print("you lose")
    else:
        print("Draw")
    round+=1
if(u>c):
        print("you won")
elif(u<c):
        print("you lose")
else:
        print("Draw")
