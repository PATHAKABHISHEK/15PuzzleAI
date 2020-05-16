import copy

# Problem or Intial State
problem = [
    ["1", "2", "3", "4"],
    ["5", "6", " ", "8"],
    ["9", "10", "7", "12"],
    ["13", "14", "11","15"]
]

# Goal state
# goal = [
#     ["1", "2", "3", "4"],
#     ["5", "6", "7", "8"],
#     ["9", "10", "11", "12"],
#     ["13", "14", "15"," "]
# ]

goal = [
    ["1", "2", "3", "4"],
    ["5", "10", "6", "8"],
    ["9", " ", "7", "12"],
    ["13", "14", "11","15"]
]

# Types Of Action
# 1. Up
# 2. Down
# 3. Left
# 4. Right

notReachedGoal = True
visitedStates = []

class Node:
    def __init__(self, state, parent, action):
        self.state = state
        self.parent = parent
        self.action = action

# Depth First Search Approach
class StackFrontier:
    def __init__(self):
        self.frontier = []
    
    def addNode(self, node):
        self.frontier.append(node)
        

    def removeNode(self):
        node = self.frontier[0]
        visitedStates.append(node.state)
        if len(self.frontier) > 1:
            self.frontier = self.frontier[1: ]
        else:
            self.frontier = []
        return node


    def checkForGoal(self, node):
        
        if (node.state == goal):
            print("reached goal state")
            notReachedGoal = False
            return True
        return False

    def solve(self, node):
        spaceRowCoord = 0
        spaceColCoord = 0
        stateForSolving = copy.deepcopy(node.state)
        for i in range(0, 4):
            for j in range(0, 4):
                if(stateForSolving[i][j] == " "):
                    spaceRowCoord = i
                    spaceColCoord = j
        
        # print("spaceColCoord " + str(spaceColCoord))
        # print("spaceRowCoord " + str(spaceRowCoord))

        if(spaceRowCoord == 3 and spaceColCoord == 3):
            # down
            stateForSolving = copy.deepcopy(node.state)
            # print(stateForSolving)
            temp = node.state[2][3]
            stateForSolving[3][3] = temp
            stateForSolving[2][3] = " "

            # for m in visitedStates:
            #     print(m)

            if not stateForSolving in visitedStates:
                self.frontier.append(Node(stateForSolving, node, "down"))

            # right
            stateForSolving = copy.deepcopy(node.state)
            temp = node.state[3][2]
            stateForSolving[3][3] = temp
            stateForSolving[3][2] = " "
            
            if not stateForSolving in visitedStates:
                self.frontier.append(Node(stateForSolving, node, "right"))


        elif(spaceRowCoord == 0 and spaceColCoord == 0):
            # up
            stateForSolving = copy.deepcopy(node.state)
            temp = node.state[1][0]
            stateForSolving[0][0] = temp
            stateForSolving[1][0] = " "
            if not stateForSolving in visitedStates:
                self.frontier.append(Node(stateForSolving, node, "up"))

            # left
            stateForSolving = copy.deepcopy(node.state)
            temp = node.state[0][1]
            stateForSolving[0][0] = temp
            stateForSolving[0][1] = " "
            if not stateForSolving in visitedStates:
                self.frontier.append(Node(stateForSolving, node, "left"))



        elif(spaceRowCoord == 3 and spaceColCoord == 0):
            # down
            stateForSolving = copy.deepcopy(node.state)
            temp = node.state[2][0]
            stateForSolving[3][0] = temp
            stateForSolving[2][0] = " "
            if not stateForSolving in visitedStates:
                self.frontier.append(Node(stateForSolving, node, "down"))

            # left
            stateForSolving = copy.deepcopy(node.state)
            temp = node.state[3][1]
            stateForSolving[3][0] = temp
            stateForSolving[3][1] = " "
            if not stateForSolving in visitedStates:
                self.frontier.append(Node(stateForSolving, node, "left"))


        elif(spaceRowCoord == 0 and spaceColCoord == 3):
            # up
            stateForSolving = copy.deepcopy(node.state)
            temp = node.state[1][3]
            stateForSolving[0][3] = temp
            stateForSolving[1][3] = " "
            if not stateForSolving in visitedStates:
                self.frontier.append(Node(stateForSolving, node, "up"))

            # right
            stateForSolving = copy.deepcopy(node.state)
            temp = node.state[0][2]
            stateForSolving[0][3] = temp
            stateForSolving[0][2] = " "
            if not stateForSolving in visitedStates:
                self.frontier.append(Node(stateForSolving, node, "right"))

        elif(spaceRowCoord == 2 or spaceRowCoord == 1 and spaceColCoord == 0 or spaceColCoord == 3):
            # up
            stateForSolving = copy.deepcopy(node.state)
            temp = node.state[spaceRowCoord + 1][spaceColCoord]
            stateForSolving[spaceRowCoord][spaceColCoord] = temp
            stateForSolving[spaceRowCoord + 1][spaceColCoord] = " "
            if not stateForSolving in visitedStates:
                self.frontier.append(Node(stateForSolving, node, "up"))

            # down
            stateForSolving = copy.deepcopy(node.state)
            temp = node.state[spaceRowCoord - 1][spaceColCoord]
            stateForSolving[spaceRowCoord][spaceColCoord] = temp
            stateForSolving[spaceRowCoord - 1][spaceColCoord] = " "
            if not stateForSolving in visitedStates:
                self.frontier.append(Node(stateForSolving, node, "down"))
            
            # left
            if spaceColCoord == 0:
                stateForSolving = copy.deepcopy(node.state)
                temp = node.state[spaceRowCoord][spaceColCoord + 1]
                stateForSolving[spaceRowCoord][spaceColCoord] = temp
            stateForSolving[spaceRowCoord][spaceColCoord + 1] = " "
            if not stateForSolving in visitedStates:
                self.frontier.append(Node(stateForSolving, node, "left"))
            
             #  right
            if spaceColCoord == 3:
                stateForSolving = copy.deepcopy(node.state)
                temp = node.state[spaceRowCoord][spaceColCoord - 1]
                stateForSolving[spaceRowCoord][spaceColCoord] = temp
            stateForSolving[spaceRowCoord][spaceColCoord - 1] = " "
            if not stateForSolving in visitedStates:
                self.frontier.append(Node(stateForSolving, node, "right"))

        elif spaceRowCoord == 3 or spaceRowCoord == 1 and spaceColCoord >=1 and spaceColCoord <= 2:
            # right
            stateForSolving = copy.deepcopy(node.state)
            temp = node.state[spaceRowCoord][spaceColCoord - 1]
            stateForSolving[spaceRowCoord][spaceColCoord] = temp
            stateForSolving[spaceRowCoord][spaceColCoord - 1] = " "
            if not stateForSolving in visitedStates:
                self.frontier.append(Node(stateForSolving, node, "right"))
            
            # left
            stateForSolving = copy.deepcopy(node.state)
            temp = node.state[spaceRowCoord][spaceColCoord + 1]
            stateForSolving[spaceRowCoord][spaceColCoord] = temp
            stateForSolving[spaceRowCoord][spaceColCoord + 1] = " "
            if not stateForSolving in visitedStates:
                self.frontier.append(Node(stateForSolving, node, "left"))

            # up
             if spaceRowCoord == 0:
                stateForSolving = copy.deepcopy(node.state)
                temp = node.state[spaceRowCoord + 1][spaceColCoord]
                stateForSolving[spaceRowCoord][spaceColCoord] = temp
                stateForSolving[spaceRowCoord + 1][spaceColCoord] = " "
                if not stateForSolving in visitedStates:
                    self.frontier.append(Node(stateForSolving, node, "up"))

            # down
            if spaceRowCoord == 3:
                stateForSolving = copy.deepcopy(node.state)
                temp = node.state[spaceRowCoord - 1][spaceColCoord]
                stateForSolving[spaceRowCoord][spaceColCoord] = temp
                stateForSolving[spaceRowCoord - 1][spaceColCoord] = " "
                if not stateForSolving in visitedStates:
                    self.frontier.append(Node(stateForSolving, node, "down"))
        else:
            # up
            stateForSolving = copy.deepcopy(node.state)
            temp = node.state[spaceRowCoord + 1][spaceColCoord]
            stateForSolving[spaceRowCoord][spaceColCoord] = temp
            stateForSolving[spaceRowCoord + 1][spaceColCoord] = " "
            if not stateForSolving in visitedStates:
                self.frontier.append(Node(stateForSolving, node, "up"))

            # down
            stateForSolving = copy.deepcopy(node.state)
            temp = node.state[spaceRowCoord - 1][spaceColCoord]
            stateForSolving[spaceRowCoord][spaceColCoord] = temp
            stateForSolving[spaceRowCoord - 1][spaceColCoord] = " "
            if not stateForSolving in visitedStates:
                self.frontier.append(Node(stateForSolving, node, "down"))

            # left
            stateForSolving = copy.deepcopy(node.state)
            temp = node.state[spaceRowCoord][spaceColCoord + 1]
            stateForSolving[spaceRowCoord][spaceColCoord] = temp
            stateForSolving[spaceRowCoord][spaceColCoord + 1] = " "
            if not stateForSolving in visitedStates:
                self.frontier.append(Node(stateForSolving, node, "left"))

            # right
            stateForSolving = copy.deepcopy(node.state)
            temp = node.state[spaceRowCoord][spaceColCoord - 1]
            stateForSolving[spaceRowCoord][spaceColCoord] = temp
            stateForSolving[spaceRowCoord][spaceColCoord - 1] = " "
            if not stateForSolving in visitedStates:
                self.frontier.append(Node(stateForSolving, node, "right"))


my = StackFrontier()
my.addNode(Node(problem, None, None))

while(notReachedGoal):
    if len(my.frontier) == 0:
       pass
    else:
        node = my.removeNode()
        for i in my.frontier:
            print(i.state)
        print()
        print()
        if not my.checkForGoal(node):
            my.solve(node)