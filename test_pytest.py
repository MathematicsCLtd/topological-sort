import pytest
import algorithm    # The code to test

def test_topological_sort_simple_DAG():
    graph = {
        'A': ['B', 'C'],
        'B': ['C'],
        'C': []
    }
    expected_result = ['A', 'B', 'C']
    assert algorithm.topological_sort(graph) == expected_result

def test_topological_sort_complex_DAG():
    graph = {
        'A': ['B', 'C'],
        'B': ['D', 'E'],
        'C': ['D'],
        'D': ['F'],
        'E': ['F'],
        'F': []
    }
    expected_result = ['A', 'B', 'C', 'E', 'D', 'F']
    assert algorithm.topological_sort(graph) == expected_result

def test_topological_sort_cycle_graph():
    graph = {
        'A': ['B'],
        'B': ['C'],
        'C': ['D'],
        'D': ['A']
    }
    with pytest.raises(ValueError):
        algorithm.topological_sort(graph)