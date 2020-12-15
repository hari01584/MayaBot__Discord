from random import randrange, uniform


def getImFeeling(name):
    irand = randrange(0, 10)

    if(irand==0):
        return ("Hey {} Hottie, Can You Accompany Me To Bed?".format(name))
    if(irand==1):
        return ("My darling, let's spend the night together! My lovely {}".format(name))
    if(irand==2):
        return ("Oh yeah i didnt get enough last time! Lets do it again {}".format(name))
    if(irand==3):
        return ("Uhh your toolbox is so small, i will breakup {}".format(name))
    if(irand==4):
        return ("Dammn {}, you are so hot and sexy even thousand girl's can't satisfy you!".format(name))
    if(irand==5):
        return ("Come to my home tommorow, this little sister will warm bed with you, ".format(name))
    if(irand==6):
        return ("You suck {}, you dont have what it takes to be the best men satisfying me!".format(name))
    if(irand==7):
        return ("You aint handsome.. you are ugly ".format(name))
    if(irand==8):
        return "Hey handsome {}, would you like to go on a date?"
    if(irand==9):
        return "Dont come near me, you smell stinks {} ASSHOLE!!"
    if(irand==10):
        return "Braahhhh I dont know who you are, but you better shut up, because i dont like you {}"

    return irand
