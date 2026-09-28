from ..models.grid import Grid
from ..models.frontier import StackFrontier
from ..models.solution import NoSolution, Solution
from ..models.node import Node


class DepthFirstSearch:
    @staticmethod
    def search(grid: Grid) -> Solution:
        """Find path between two points in a grid using Depth First Search

        Args:
            grid (Grid): Grid of points

        Returns:
            Solution: Solution found
        """
        # Initialize root node
        root = Node("", state=grid.initial, cost=0, parent=None, action=None)

        # Initialize expanded with the empty dictionary
        expanded = dict()

        # Initialize frontier with the root node
        # TODO Complete the rest!!
        if grid.objective_test(root.state):
            return Solution(root, expanded)
        
        frontera = StackFrontier()
        frontera.add(root)

        while not frontera.is_empty():
            node = frontera.remove()

            if node.state in expanded:
                continue
            expanded[node.state] = True

            for accion in grid.actions(node.state):
                sucesor = grid.result(node.state, accion)
                if sucesor in expanded:
                    continue
                hijo = Node("", state = sucesor, cost = node.cost + grid.individual_cost(node.state, accion), parent=node, action=accion) 
                if grid.objective_test(sucesor):
                    return Solution(hijo, expanded)
                frontera.add(hijo)

        return NoSolution(expanded)
    