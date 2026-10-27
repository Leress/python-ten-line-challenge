from random import randint
stats = [int(randint(1,20)),int(randint(1,40)),0,False]
while stats[2]<=10 and stats[3] == False:
    force = int(input(f"Gravity: {stats[0]},Chances: {stats[2]} Enter Force (whole interger):"))
    if force == (stats[0] * stats[1]): stats[3] = True
    print("Too High")  if force > (stats[0] * stats[1]) else print("too low")
    stats[2] +=1
print("Good take off") if (stats[3]) else print("You failed to get away, and were captured")     