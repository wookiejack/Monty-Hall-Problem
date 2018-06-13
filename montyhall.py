import random, time

def play():
    start_time = time.time()
    doors = [1,2,3]

    door = doors[random.randint(0,2)]
    guess = doors[random.randint(0,2)]


    del doors[doors.index(door)]
    try:
        del doors[doors.index(guess)]
    except:
        del doors[random.randint(0,1)]

    goat = doors[0]
    del doors

    doors = [1,2,3]
    del doors[doors.index(goat)]

    if doors.index(guess) == 0:
        choice = 1
    elif doors.index(guess) == 1:
        choice = 0

    if doors[choice] == door:
        return True
    elif doors[choice] != door:
        return False

while 42:
    wins = 0
    losses = 0

    iterations = int(input("Iterations: "))

    start_time = time.time()
    for i in range(iterations):
        result = play()

        if result == True:
            wins = wins + 1
        if result == False:
            losses = losses + 1

    runtime = (time.time() - start_time)
    
    print("Total Wins: " + str(wins))
    print("Total Losses: " + str(losses))
    print("Runtime: " + str(runtime) + " seconds")
    print("\n")
