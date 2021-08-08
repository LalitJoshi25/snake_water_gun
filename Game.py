import random

def gameWin(c, y):
    if c == y:
        return None
    elif c == 's':
        if y == 'w':
            return False
        elif y == 'g':
            return True
    elif c == 'w':
        if y == 'g':
            return False
        elif y == 's':
            return True
    elif c == 'g':
        if y == 's':
            return False
        elif y == 'w':
            return True


# computer side code
comp = random.randint(1,3)#built-in random function.random.randint(start,end)
print("comp Turn:- Snake(s), Water(w) and Gun(g)")
if comp == 1:
    comp = 's'
elif comp == 2:
    comp = 'w'
elif comp == 3:
    comp = 'g'

# for user
you = input("Your Turn:- Snake(s), Water(w) and Gun(g)")
# calling the function
a = gameWin(comp, you)
print(f"computer choose {comp}")
print(f"you choose {you}")

if a == None:
    print("Game is tie")
elif a:
    print("You win!!!")
else:
    print("You loose!!!")