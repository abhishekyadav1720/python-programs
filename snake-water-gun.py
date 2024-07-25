import random
def check(choose, comp):
    if comp == choose:
        return "draw"
    elif( comp == 0 and choose == 2):
        return "win"
    elif( comp == 1 and choose == 0):
        return "win"
    elif( comp == 2 and choose == 1):
        return "win"
    else:
        return "loose"

choose = int(input("choose 0 for snake, 1 for water, 2 for gun"))
comp = random.randint(0,2) 
score = check(choose, comp)
print(score)

