# Problem or Intial State
problem = [
    ["1", "4", "7", "9"],
    ["15", "14", "13", "12"],
    ["3", "5", "6", "8"]
    ["2", "10", "11"," "]
]

# Goal state
goal = [
    ["1", "2", "3", "4"],
    ["5", "6", "7", "8"],
    ["9", "10", "11", "12"]
    ["13", "14", "15"," "]
]

notReachedGoal = True
visitedNodes = []

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
        node = self.frontier[-1]
        visitedNodes.append(node)
        self.frontier = self.frontier[1:]
        self.checkForGoal(node)

    def checkForGoal(self, node):
        if (node.state == goal):
            println("reached goal state")
            notReachedGoal = False

    def solev(self):
        pass

