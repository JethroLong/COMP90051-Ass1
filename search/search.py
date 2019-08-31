# search.py
# ---------
# Licensing Information:  You are free to use or extend these projects for
# educational purposes provided that (1) you do not distribute or publish
# solutions, (2) you retain this notice, and (3) you provide clear
# attribution to UC Berkeley, including a link to http://ai.berkeley.edu.
# 
# Attribution Information: The Pacman AI projects were developed at UC Berkeley.
# The core projects and autograders were primarily created by John DeNero
# (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# Student side autograding was added by Brad Miller, Nick Hay, and
# Pieter Abbeel (pabbeel@cs.berkeley.edu).


"""
In search.py, you will implement generic search algorithms which are called by
Pacman agents (in searchAgents.py).
"""

import util

class SearchProblem:
    """
    This class outlines the structure of a search problem, but doesn't implement
    any of the methods (in object-oriented terminology: an abstract class).

    You do not need to change anything in this class, ever.
    """

    def getStartState(self):
        """
        Returns the start state for the search problem.
        """
        util.raiseNotDefined()

    def isGoalState(self, state):
        """
          state: Search state

        Returns True if and only if the state is a valid goal state.
        """
        util.raiseNotDefined()

    def getSuccessors(self, state):
        """
          state: Search state

        For a given state, this should return a list of triples, (successor,
        action, stepCost), where 'successor' is a successor to the current
        state, 'action' is the action required to get there, and 'stepCost' is
        the incremental cost of expanding to that successor.
        """
        util.raiseNotDefined()

    def getCostOfActions(self, actions):
        """
         actions: A list of actions to take

        This method returns the total cost of a particular sequence of actions.
        The sequence must be composed of legal moves.
        """
        util.raiseNotDefined()


def tinyMazeSearch(problem):
    """
    Returns a sequence of moves that solves tinyMaze.  For any other maze, the
    sequence of moves will be incorrect, so only use this for tinyMaze.
    """
    from game import Directions
    s = Directions.SOUTH
    w = Directions.WEST
    return  [s, s, w, s, w, w, s, w]

def depthFirstSearch(problem):
    """
    Search the deepest nodes in the search tree first.

    Your search algorithm needs to return a list of actions that reaches the
    goal. Make sure to implement a graph search algorithm.

    To get started, you might want to try some of these simple commands to
    understand the search problem that is being passed in:

    print("Start:", problem.getStartState())
    print("Is the start a goal?", problem.isGoalState(problem.getStartState()))
    print("Start's successors:", problem.getSuccessors(problem.getStartState()))
    """
    "*** YOUR CODE HERE IF YOU WANT TO PRACTICE ***"
    # Initialize a stack
    open = util.Stack()

    # Retrieve the init state
    initState = (problem.getStartState(), ['Stop'], 0)
    open.push(initState)
    closed = []

    while not open.isEmpty():
        currState = open.pop()
        currPos = currState[0]
        currPath = currState[1]
        currCost = currState[2]

        if problem.isGoalState(currPos):
            return currPath[1:]
        else:
            closed.append(currPos)
        if currState not in closed:
            successors = problem.getSuccessors(currPos)
            if len(successors) > 0:
                for each in successors:
                    if each[0] not in closed:
                        temp = (each[0], currPath+[each[1]], currCost+each[2])
                        open.push(temp)
    return False


def breadthFirstSearch(problem):
    """Search the shallowest nodes in the search tree first."""
    "*** YOUR CODE HERE IF YOU WANT TO PRACTICE ***"
    # Initialize a stack
    open = util.Queue()

    # Retrieve the init state
    init = (problem.getStartState(), ['Stop'], 0)
    open.push(init)
    closed = []
    while not open.isEmpty():
        currNode = open.pop()
        currState = currNode[0]
        currPath = currNode[1]
        currCost = currNode[2]

        if problem.isGoalState(currState):
            return currPath[1:]
        else:
            if currState not in closed:
                closed.append(currState)
                successors = problem.getSuccessors(currState)
                if len(successors) > 0:
                    for each in successors:
                        if each[0] not in closed:
                            temp = (each[0], currPath + [each[1]], currCost + each[2])
                            open.push(temp)
    return False


def uniformCostSearch(problem):
    """Search the node of least total cost first."""
    "*** YOUR CODE HERE IF YOU WANT TO PRACTICE ***"
    util.raiseNotDefined()

def nullHeuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0

def aStarSearch(problem, heuristic=nullHeuristic):
    """Search the node that has the lowest combined cost and heuristic first."""
    "*** YOUR CODE HERE IF YOU WANT TO PRACTICE ***"
    util.raiseNotDefined()


def iterativeDeepeningSearch(problem):
    """Search the deepest node in an iterative manner."""
    "*** YOUR CODE HERE FOR TASK 1 ***"

    # Retrieve the init state
    # state model ( (position, depth), path, cost)
    initState = ( (problem.getStartState(), 0) , ['Stop'], 0)
    limit = 0
    while True:
        # Initialization each iteration
        open = util.Stack()
        open.push(initState)
        closed = {}

        while not open.isEmpty():
            currState = open.pop()
            currPos = currState[0][0]
            currDepth = currState[0][1]
            currPath = currState[1]
            currCost = currState[2]

            if problem.isGoalState(currPos):
                return currPath[1:]
            else:
                closed[currPos] = currCost

            successors = problem.getSuccessors(currPos)
            nextDepth = currDepth + 1
            if len(successors) > 0 and nextDepth <= limit:
                for each in successors:
                    nextCost = currCost + each[2]
                    if each[0] not in closed.keys() or nextCost < closed[each[0]]:
                        temp = ( (each[0], nextDepth), currPath + [each[1]], nextCost)
                        open.push(temp)
        limit += 1

    return False


def waStarSearch(problem, heuristic=nullHeuristic):
    """Search the node that has has the weighted (x 2) lowest combined cost and heuristic first."""
    "*** YOUR CODE HERE FOR TASK 2 ***"

    priorityFunc = lambda x: x[2] + 2*heuristic(x[0], problem)

    # initialize a priority queue
    open = util.PriorityQueue()
    closed = []

    # Retrieve the init state
    init = (problem.getStartState(), ['Stop'], 0)
    open.push(init, priorityFunc(init))
    while not open.isEmpty():
        currNode = open.pop()
        currState = currNode[0]
        currPath = currNode[1]
        currPathCost = currNode[2]
        if problem.isGoalState(currState):
            return currPath[1:]
        else:
            closed.append(currState)
        successors = problem.getSuccessors(currState)

        if len(successors) > 0:
            for each in successors:
                newPos = each[0]
                newPathCost = currPathCost + each[2]

                if newPos not in closed:
                    temp = (each[0], currPath + [each[1]], newPathCost)
                    open.update(temp, priorityFunc(temp))

    return False


def waStarSearch2(problem, heuristic=nullHeuristic):
    """
    Search the node that has has the weighted (x 2) lowest combined cost and heuristic first.
    this is an another weighted A* search algorithm version with reopening.

    This version works with "CapsuleSearchProblem2", "foodHeuristic2" and "CapsuleSearchAgent2" for TASK 3
    This can find a solution that satisfies the capsule-food constraint with expanding
    incredibly less nodes.

    """
    priorityFunc = lambda x: x[2] + 2*heuristic(x[0], problem)

    # initialize a priority queue
    open = util.PriorityQueue()

    # Retrieve the init state
    init = (problem.getStartState(), ['Stop'], 0)
    open.push(init, priorityFunc(init))
    bestG = {}
    while not open.isEmpty():

        currNode = open.pop()
        currState = currNode[0]
        currPath = currNode[1]
        currPathCost = currNode[2]

        if problem.isGoalState(currState):
            return currPath[1:]
        successors = problem.getSuccessors(currState)

        if len(successors) > 0:
            for each in successors:
                newPos = each[0]
                newPathCost = currPathCost + each[2]
                if newPos not in bestG.keys() or newPathCost < bestG[newPos]:
                    bestG[newPos] = newPathCost
                    temp = (each[0], currPath + [each[1]], newPathCost)
                    hval = heuristic(each[0], problem)
                    if hval < float('inf'):
                        open.update(temp, priorityFunc(temp))

    return False

# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch
ids = iterativeDeepeningSearch
wastar = waStarSearch
wastar2 = waStarSearch2
