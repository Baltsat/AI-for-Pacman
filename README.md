# AI-for-Pacman
Project for constructing different AI algorithms to control pygame Pacman.
At first, we implement DFS, BFS, UCS, .


## Create a virtual environment
Run in the terminal:
```bash
git clone https://github.com/Baltsat/AI-for-Pacman; 
virtualenv venv; 
source venv/bin/activate; 
pip3 install -r requirements_AIC.txt;
cd search_AIC;
```

## Execute

- To run a UI
```bash
python3 pacman_AIC.py
```

- To run a simple agent
```bash
python3 pacman_AIC.py --layout testMaze --pacman GoWestAgent
```

You should have in the terminal:

| Pacman emerges victorious! | Score: 503     |
|---------------------------|----------------|
| Average Score             | 503.0          |
| Scores                    | 503.0          |
| Win Rate                  | 1/1 (1.00)     |
| Record                    | Win            |



![Init program](imgs/Init_program.png)


To see the list of all options and their default values use:
```bash
python3 pacman_AIC.py -h
```



# First Agent: Goal Based Agent = Search Agent

## Depth-first search (DFS)

We implement DFS algorithm in the *depthFirstSearch* function in *search.py*. Our algorithm returns a list of action that reaches the goal.

- Expands the deepest unexpanded node first.
- Instance of the graph-search algorithm, depth-first search uses a LIFO queue instead of FIFO queue.
- Can be implemented with a recursive function that calls itself on each of its children in turn.

We test our code using:
```bash
python3 pacman_AIC.py -l tinyMaze -p SearchAgent
```
```bash
python3 pacman_AIC.py -l mediumMaze -p SearchAgent
```
```bash
python3 pacman_AIC.py -l bigMaze -p SearchAgent -z .5
```

Or all in once:
```bash
python3 pacman_AIC.py -l tinyMaze -p SearchAgent; python3 pacman_AIC.py -l mediumMaze -p SearchAgent; python3 pacman_AIC.py -l bigMaze -p SearchAgent -z .5
```


## Breadth-first Search (BFS)

We implement DFS algorithm in the *breadthFirstSearch* function in *search.py*. Our algorithm returns a list of action that reaches the goal.

- Expands the shallowest nodes first.
- Complete.
- Optimal for unit step costs.
- Has exponential space time and space complexity.

We test our code using:
```bash
python3 pacman_AIC.py -l tinyMaze -p SearchAgent -a fn=bfs -z .5
```
```bash
python3 pacman_AIC.py -l mediumMaze -p SearchAgent -a fn=bfs
```
```bash
python3 pacman_AIC.py -l bigMaze -p SearchAgent -a fn=bfs -z .5
```
```bash
python3 pacman_AIC.py -l mediumScaryMaze -p SearchAgent -a fn=bfs -z .5
```


## Uniform Cost Search (UCS)

We implement DFS algorithm in the *breadthFirstSearch* function in *search.py*. Our algorithm returns a list of action that reaches the goal.

- Expands the node with lowest path cost g(n).
- Goal test is applied to a node when it is selected for expansion rather than when it is first generate, the first goal node that is generated may be on a suboptimal path.
- A test is added in case a better path is found to a node currently on the frontier.

We test our code using:
```bash
python3 pacman_AIC.py -l mediumMaze -p SearchAgent -a fn=ucs
```
```bash
python3 pacman_AIC.py -l mediumDottedMaze -p StayEastSearchAgent
```
```bash
python3 pacman_AIC.py -l mediumScaryMaze -p StayWestSearchAgent
```

## Finding All the Corners Problem

In corner mazes, there are four dots, one in each corner. Our new search problem is to find the shortest path through the maze that touches all four corners (whether the maze actually has food there or not).



We test our code using:
```bash
python3 pacman_AIC.py -l tinyCorners -p SearchAgent -a fn=bfs,prob=CornersProblem
```
```bash
python3 pacman_AIC.py -l mediumCorners -p SearchAgent -a fn=bfs,prob=CornersProblem
```



# Credits 

*Licensing Information:*
You are free to use or extend these projects for educational purposes provided that (1) you do not distribute or publish solutions, (2) you retain this notice, and (3) you provide clear attribution to UC Berkeley, including a link to http://ai.berkeley.edu.
