import random

N=1000000
def montyhall(smart,verbose):
    gooddoor = random.randrange(3)
    if verbose : print("Good door :",gooddoor)
    guess1 = random.randrange(3)
    if verbose : print("First guess :",guess1)
    listbad = list(range(2+1))
    listbad.pop(gooddoor)
    baddoor=random.choice(listbad)
    if verbose : print("Bad door n°",baddoor," open")
    if smart:
        listbad = list(range(2+1))
        listbad.pop(guess1)
        guess2=listbad[0]
        if verbose : print("Changed choice to door ",guess2)
    else:
        guess2=guess1
        if verbose : print("Kept door n°",guess2)
    return guess2==gooddoor


cpt=0
for i in range(N):
    oui = montyhall(False,False)
    if oui: cpt=cpt+1

print("Chance Dumb:",cpt/N)

cpt=0
for i in range(N):
    oui = montyhall(True,False)
    if oui: cpt=cpt+1

print("Chance Smart:",cpt/N)
