from collections import defaultdict

def topological_sort(graph):
    """
    Perform a topological sort on a directed acyclic graph (DAG).

    Args:
        graph (dict): A dictionary representing a DAG, where the keys are nodes and the values are lists of their
                      adjacent nodes.

    Returns:
        list: A topologically sorted list of nodes.

    Raises:
        ValueError: If the graph contains cycles.
    """
    in_degree = defaultdict(int)
    for node in graph:
        for neighbor in graph[node]:
            in_degree[neighbor] += 1

    queue = [node for node in graph if in_degree[node] == 0]
    result = []
    while queue:
        node = queue.pop(0)
        result.append(node)
        for neighbor in graph[node]:
            in_degree[neighbor] -= 1
            if in_degree[neighbor] == 0:
                queue.append(neighbor)

    if len(result) != len(graph):
        raise ValueError("Graph contains cycles.")

    return result

