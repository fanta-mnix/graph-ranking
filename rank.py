def build_index(nodes):
    return {node: index for index, node in enumerate(nodes)}


def invert_index(index):
    return {value: key for key, value in index.items()}


def build_adjacency_matrix(graph, index):
    import numpy as np

    nodes = graph.keys()
    n = len(nodes)
    matrix = np.zeros((n, n), dtype=float)

    for source in nodes:
        i = index[source]
        possible_transitions = graph[source]
        for target in possible_transitions:
            j = index[target]
            matrix[i, j] = 1.0

    return matrix


def discrete_uniform(n):
    import numpy as np
    return np.repeat([1.0 / n], n)


def as_markov_matrix(adjacency):
    import numpy as np
    from scipy import sparse

    m, n = adjacency.shape
    assert m == n
    assert not sparse.issparse(adjacency)

    adjacency = adjacency.copy()
    dangling = ~np.any(adjacency , axis=1)
    adjacency[dangling, :] = 1.0
    markov_matrix = adjacency / adjacency.sum(axis=1).reshape(-1, 1)
    return markov_matrix.T


def solve(markov_matrix, p, follow, eps, max_iter):
    import numpy as np
    import logging
    from scipy import sparse, linalg

    def is_valid_matrix():
        probabilities = markov_matrix.sum(axis=0)
        ideal = np.ones(len(probabilities))
        return np.allclose(ideal, probabilities)

    m, n = markov_matrix.shape
    assert m == n
    assert len(p) == n
    assert is_valid_matrix()

    if not sparse.isspmatrix_csr(markov_matrix):
        markov_matrix = sparse.csr_matrix(markov_matrix)

    base = discrete_uniform(n)
    for i in range(max_iter):
        p_next = (1 - follow) * base + follow * markov_matrix.dot(p)
        delta = linalg.norm(p_next - p, 1)
        logging.debug("Delta: {:.4f}", delta)
        p = p_next
        if delta <= eps:
            break

    return p


def calculate_rank(graph, damp=0.85, eps=1e-4, max_iter=100):
    index = build_index(graph)
    adjacency = build_adjacency_matrix(graph, index)
    markov = as_markov_matrix(adjacency)
    p = discrete_uniform(len(graph))
    stable = solve(markov, p, damp, eps, max_iter)

    return sorted(zip(invert_index(index).values(), stable), key=lambda x: x[1], reverse=True)


__all__ = ['calculate_rank']
