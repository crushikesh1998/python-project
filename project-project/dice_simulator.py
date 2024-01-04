import random

def dice_roll(dice,sides):

    roll=[]

    for i in range(0,dice):
        face = random.randint(1,sides)
        roll.append(face)
    return roll

dice=int(input("Dice: "))

if(dice<=0):
    print("Must have one dice!!")
    quit()

sides =int(input("Side: "))

if(sides<=0):
    print("Must have one side!!")
    quit()

roll =dice_roll(dice,sides)

print(roll)