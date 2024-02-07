# search.py
# ---------
# Licensing Information:  You are free to use or extend these projects for
# educational purposes provided that (1) you do not distribute or publish
# solutions, (2) you retain this notice, and (3) you provide clear
# attribution to UC Berkeley, including a link to http://ai.berkeley.edu.
# 


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
    print("Start:", problem.getStartState())
    print("Is the start a goal?", problem.isGoalState(problem.getStartState()))
    print("Start's successors:", problem.getSuccessors(problem.getStartState()))

    visited = set()  # Set to keep track of visited states
    frontier = util.Stack()  # Stack to store the states to be explored
    frontier.push((problem.getStartState(), []))  # Push the start state and an empty list of actions

    while not frontier.isEmpty():
        state, actions = frontier.pop()

        if problem.isGoalState(state):
            print("Goal state found", state, actions)
            return actions

        if state not in visited:
            visited.add(state)
            successors = problem.getSuccessors(state)
            print("Successors:", successors)
            for successor, action, _ in successors:
                frontier.push((successor, actions + [action]))

    return []  # Return an empty list if no solution is found
    

def breadthFirstSearch(problem):
    """Search the shallowest nodes in the search tree first."""
    
    visited = set()  # Set to keep track of visited states
    frontier = util.Queue()  # FIFO Queue to store the states to be explored
    frontier.push((problem.getStartState(), []))  # Push the start state and an empty list of actions

    while not frontier.isEmpty():
        state, actions = frontier.pop()
        print("State:", state, "Actions:", actions)

        if problem.isGoalState(state):
            print("Goal state found", state, actions)
            return actions

        if state not in visited:
            visited.add(state)
            successors = problem.getSuccessors(state)
            print("Successors:", successors)
            for successor, action, _ in successors:
                frontier.push((successor, actions + [action]))

    return []  # Return an empty list if no solution is found

def uniformCostSearch(problem):
    """Search the node of least total cost first."""

    visited = set()  # Set to keep track of visited states
    frontier = util.PriorityQueue()  # Priority Queue to store the states to be explored
    frontier.push((problem.getStartState(), []), 0)  # Push the start state and an empty list of actions with priority 0

    while not frontier.isEmpty():
        state, actions = frontier.pop()

        if problem.isGoalState(state):
            print("Goal state found", state, actions)
            return actions

        if state not in visited:
            visited.add(state)
            successors = problem.getSuccessors(state)
            print("Successors:", successors)
            for successor, action, stepCost in successors:
                new_actions = actions + [action]
                new_cost = problem.getCostOfActions(new_actions)
                frontier.push((successor, new_actions), new_cost)

    return []  # Return an empty list if no solution is found


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
