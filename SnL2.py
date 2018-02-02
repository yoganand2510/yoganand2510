#Snake n ladder program
import random
count=0
while(count<=100):
    n=input("enter 'r' to roll a dice")
    if(n=='r'):
        r=random.randint(1,6)
        count=count+r
        print("your random number is ",r)
        print("you r in position",count)
    if(count>100):
        print("try again")
        count=count-r
    elif count==8:
        count=37
        print("u have climbed the ladder n reached 37")
        print("you are in position",count)
    elif count==11:
        count=2
        print("u have been biten by a snake so u go down to 2")
        print("you r in position",count)
    elif count==13:
        count=34
        print("u have climbed the ladder n reached to 34")
        print("you are in position",count)
    elif count==25:
        count=4
        print("you were bitten by a snake so go down to 4")
        print("you are in position",count)
    elif count==38:
        count=9
        print("you were bitten by a snake so u go down to 9")
        print("you are in position",count)
    elif count==40:
        count=68
        print("you climbed up a ladder n reached 68")
        print("you are in position",count)
    elif count==52:
        count=81
        print("you have climbed up a ladder n reached 81")
        print("you are in position",count)
    elif count==65:
        count=46
        print("you were bitten by a snake so go down to 46")
        print("you are in position",count)
    elif count==76:
        count=97
        print("you climbed up a ladder n reached to 97")
        print("you are in position",count)
    elif count==89:
        count=70
        print("you were bitten by a snake so go down to 70")
        print("you are in position",count)
    elif count==93:
        count=64
        print("you were bitten by a snake so go down to 64")
        print("you are in position",count)
    elif count==100:
        print("you won")
        break
    else:
        print("continue the game")
