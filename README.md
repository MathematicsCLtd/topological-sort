# Topological Sort

An algorithm that approaches a Directed Acyclic Graph (DAG) in a specific order. All the vertexes of a graph are ordered on a line with the direct edges pointing left to right. The algorithm traverses the graph and processes the vertexes one after another.

## Implementation

The topological_sort function takes a directed acyclic graph represented as a dictionary, where the keys are nodes and the values are lists of their adjacent nodes. It returns a topologically sorted list of nodes. If the graph contains cycles, a ValueError is raised.

## Testing
* The first test case tests the algorithm on a simple DAG with 3 nodes. The expected result is a topological ordering of ['A', 'B', 'C'].
* The second test case tests the algorithm on a more complex DAG with 6 nodes. The expected result is a topological ordering of ['A', 'B', 'C', 'E', 'D', 'F'].
* The third test case tests the algorithm on a graph with a cycle. We expect the algorithm to raise a ValueError since the graph contains cycles.

## Use Cases
* Dependency resolution: In software development, it is common for programs or libraries to depend on other programs or libraries. Topological sorting can be used to determine the order in which dependencies should be installed or linked to ensure that they are available when needed. For example, if library A depends on library B, which in turn depends on library C, a topological sort can determine that library C must be installed first, followed by library B, and then library A.
* Task scheduling: In project management, tasks often have dependencies on other tasks that must be completed before they can begin. Topological sorting can be used to determine the order in which tasks should be scheduled to ensure that all dependencies are met. For example, if task A must be completed before task B can begin, and task B must be completed before task C can begin, a topological sort can determine that task A should be scheduled first, followed by task B, and then task C.
* Circuit design: In electrical engineering, circuits can have feedback loops that create cycles, which can cause problems. Topological sorting can be used to identify these cycles and ensure that circuits are designed in such a way that they are free of feedback loops.
* Data processing: In data processing, it is common to have large datasets with dependencies between data items. Topological sorting can be used to determine the order in which data should be processed to ensure that all dependencies are met.
