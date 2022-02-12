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
    "*** YOUR CODE HERE ***"
    startState = problem.getStartState()
    stack = util.Stack()
    stack.push((startState, 0, [('None', startState)]))
    visited = set()
    best = None #(bestCost, bestPath)
    visited.add(startState)
    while(not stack.isEmpty()):
        currentState, currentCost, path = stack.pop()
        if problem.isGoalState(currentState):
            if best == None or best[1] > currentCost:
                best = (currentCost, path)
        else:
            successors = problem.getSuccessors(currentState)
            for (successorState, action, successorCost) in successors:
                if not successorState in visited:
                    visited.add(successorState)
                    stack.push((successorState, currentCost + successorCost, path + [(action, successorState)] ))
    (bestCost, bestPath) = best
    (actions, states) = unzip(bestPath)
    print(actions.pop(0))
    return actions

    # currentState = problem.getStartState()
    # stack = util.Stack()
    # visited = set()
    # visited.add(currentState)
    # path = [] #[(action,cost)]
    # bestPath = None
    # while (not stack.isEmpty()) or (currentState == problem.getStartState()):
    #     print(stack.list)
    #     if problem.isGoalState(currentState): #found goal -- new bestPath?
    #         cost = calculateCost(path)
    #         if bestPath == None or cost < calculateCost(bestPath):
    #             bestPath = path
    #         #update path and currentstate
    #     else:
    #         successors = problem.getSuccessors(currentState)
    #         if len(successors) == 0: #back track
    #             path.pop()
    #         else:
    #             for (successorState, action, cost) in successors:
    #                 if not successorState in visited:
    #                     visited.add(successorState)
    #                     stack.push((successorState, action, cost))
    #             (currentState, action, cost) = stack.pop()
    #             path.append((action, cost))
    # (actions, costs) = unzip(bestPath)
    # return actions

#takes a path, which is a list of (action, cost) tuples, and calculates the sum of all the costs
def calculateCost(path):
    total = 0
    for (action, cost) in path:
        total += cost
    return total
      
def unzip(lst):
    xList = []
    yList = []
    for (x,y) in lst:
        xList.append(x)
        yList.append(y)
    return (xList,yList)

def breadthFirstSearch(problem):
    """Search the shallowest nodes in the search tree first."""
    "*** YOUR CODE HERE ***"
    util.raiseNotDefined()

def uniformCostSearch(problem):
    """Search the node of least total cost first."""
    "*** YOUR CODE HERE ***"
    util.raiseNotDefined()

def nullHeuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0

def aStarSearch(problem, heuristic=nullHeuristic):
    """Search the node that has the lowest combined cost and heuristic first."""
    "*** YOUR CODE HERE ***"
    util.raiseNotDefined()


# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch
