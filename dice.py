# import random library
import random

# define Dice functions.
def four_side():
    print(random.randint(1,4))

def six_side():
    print(random.randint(1,6))
    
def eight_side():
    print(random.randint(1,8))
        
def ten_side():
    print(random.randint(1,10))
        
def twelve_side():
    print(random.randint(1,12))

def twenty_side():
    print(random.randint(1,20))    

#--- Start of code ---

dice = ''
while dice != '4,6,8,10,12,20':
    dice = int(input('How many sides 4.6.8.10.12.20? '))
    if dice == 4:
        four_side()
        print('')
        again = input('Roll again?')
        if  again.lower() == '':
            break
        
    elif dice == 6:
        six_side()
        print('')
        again = input('Roll again?')
        if  again.lower() == '':
            break
    elif dice == 8:
        eight_side()
        print('')
        again = input('Roll again?')
        if  again.lower() == '':
            break
    elif dice == 10:
        ten_side()
        print('')
        again = input('Roll again?')
        if  again.lower() == '':
            break
    elif dice == 12:
        twelve_side()
        print('')
        again = input('Roll again?')
        if  again.lower() == '':
            break
    elif dice == 12:
        twelve_side()
        print('')
        again = input('Roll again?')
        if  again.lower() == '':
            break
    elif dice == 20:
        twenty_side()
        print('')
        again = input('Roll again?')
        if  again.lower() == '':
            break
print('bye')