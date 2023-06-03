from random import randint

class Inventory:
    def __init__(self, resources, robots):
        self.resources = resources
        self.robots = robots


def genRecipes():
    # generate recipes
    recipes = {
        'wood': [randint(1, 3), 0, 0, 0],
        'stone': [randint(4, 6), 0, 0, 0],
        'iron': [randint(3, 5), randint(2, 4), 0, 0],
        'gold': [randint(1, 3), randint(3, 5), randint(1, 5), 0],
        'platinum': [randint(1, 6), randint(1, 6), randint(1, 6), randint(1, 6)],
    }
    return recipes


def advanceTurn(player):
    print("Turn advanced.")
    print("You made: ")
    for k in player.robots:
        # generate resources equivalent to how many robots
        # the player has of that resource
        player.resources[k] += player.robots[k]
        # display resource made
        if player.robots[k] != 0:
            print(f"{player.robots[k]} {k}")

    return player


def buyRobot(player, recipes):
    # choose which robot to buy
    robotToBuy = ''
    while robotToBuy not in ['wood', 'stone', 'iron', 'gold', 'platinum']:
        robotToBuy = input("Enter which robot to buy: ")

    # check if player has enough resources
    invalid = False
    currentResources = [player.resources[k] for k in player.resources]
    for i, requiredResource in enumerate(recipes[robotToBuy]):
        if currentResources[i] < requiredResource:
            invalid = True

    # if player has the required resources
    if not invalid:
        print(f"1 {robotToBuy} was bought.")
        # increment the robot
        player.robots[robotToBuy] += 1
        # subtract the resources
        currentResources = [player.resources[k] for k in player.resources]
        for i, resourceNum in enumerate(recipes[robotToBuy]):
            currentResources[i] -= resourceNum

        player.resources = {
            'wood': currentResources[0],
            'stone': currentResources[1],
            'iron': currentResources[2],
            'gold': currentResources[3],
            'platinum': currentResources[4],
        }

    else:
        print("Not enough resources.")
    
    return player


def viewRecipes(recipes):
    # display recipes for each robot
    resources = ['wood', 'stone', 'iron', 'gold', 'platinum']
    for k in recipes:
        print(f"{k} robot: ")
        for i, resourceNum in enumerate(recipes[k]):
            print(f"{resourceNum} {resources[i]}",end=', ')
        print("")


def viewInventory(player):
    # display current resources
    print("You have: ")
    for k in player.resources:
        print(f"{player.resources[k]} {k}")

    print("")

    # display current robots
    for k in player.robots:
        print(f"{player.robots[k]} {k} robots")


def help():
    print(f'''
          Commands:
          t - advance to next turn, makes robots produce resources
          b - buy a robot
          r - view recipes to buy robots
          i - view inventory, shows current resources and robots
          h - help menu
          q - quit game
          ''')


def gameLoop(player, recipes):
    # enter game loop
    # keep running until player generates a platinum
    command = ''
    turnsTaken = 0
    while player.resources["platinum"] == 0 and command != 'q':
        command = input("\nEnter command: \n")
        while command not in ['t', 'b', 'r', 'i', 'q', 'h']:
            print("Invalid command, enter 'h' to see the commands menu.")
            command = input("\nEnter command: \n")

        match command:
            case 't': 
                player = advanceTurn(player)
            case 'b':
                player = buyRobot(player, recipes)
            case 'r':
                viewRecipes(recipes)
            case 'i':
                viewInventory(player)
            case 'h':
                help()
            # if command == 'q', then while loop will quit

        turnsTaken += 1

    # if player won, and has not quit
    if command != 'q':
        print("You won!")
        print("Final inventory: ")
        viewInventory(player)
        print(f"Turns taken: {turnsTaken}")


def main():
    # player starts with 0 resources, 1 wood robot
    initResources = {
        'wood': 0,
        'stone': 0,
        'iron': 0,
        'gold': 0,
        'platinum': 0,
    }
    initRobots = {
        'wood': 1,
        'stone': 0,
        'iron': 0,
        'gold': 0,
        'platinum': 0,
    }
    player = Inventory(initResources, initRobots)
    recipes = genRecipes()
    gameLoop(player, recipes)


if __name__ == "__main__":
    main()