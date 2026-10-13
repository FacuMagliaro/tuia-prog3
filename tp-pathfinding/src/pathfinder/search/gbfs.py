from ..models.grid import Grid
from ..models.frontier import PriorityQueueFrontier
from ..models.solution import NoSolution, Solution
from ..models.node import Node



class GreedyBestFirstSearch:
    @staticmethod
    def search(grid: Grid) -> Solution:
        root = Node("", state=grid.initial, cost=0, parent=None, action=None)
        reached = {}
        reached[root.state] = root.cost

        if grid.objective_test(root.state):
            return Solution(root, reached)

        frontier = PriorityQueueFrontier()
        frontier.add(root, grid.heuristic(root))

        while not frontier.is_empty():
            node = frontier.pop()
            if grid.objective_test(node.state):
                return Solution(node, reached)

            for action in grid.actions(node.state): 
                successor = grid.result(node.state, action)
                cost = node.cost + grid.individual_cost(node.state, action)

                if successor not in reached or cost < reached[successor]:
                    son = Node("", successor, cost, parent=node, action=action)
                    reached[successor] = cost
                    frontier.add(son, grid.heuristic(son))
                    
        return NoSolution(reached)
