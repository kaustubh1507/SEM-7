import numpy as np


def page_rank(links, num_iterations=100, d=0.85):
    """
    Compute the PageRank of nodes in a graph.

    Parameters:
    - links: Dictionary where the keys are nodes, and the values are lists of nodes
             the key node links to.
    - num_iterations: Number of iterations to run the algorithm (default is 100).
    - d: Damping factor (default is 0.85), representing the probability that a
         random surfer continues clicking links rather than jumping to a random page.

    Returns:
    - PageRank scores for each node.
    """
    # Initialize the nodes and number of nodes
    nodes = list(links.keys())
    N = len(nodes)

    # Create an initial PageRank vector (all nodes start with equal rank)
    ranks = np.ones(N) / N

    # Create the link matrix (adjacency matrix representation of the graph)
    link_matrix = np.zeros((N, N))
    for i, node in enumerate(nodes):
        for target in links[node]:
            if target in nodes:
                j = nodes.index(target)
                link_matrix[j, i] = 1 / len(links[node])

    # Iterate to calculate PageRank
    for _ in range(num_iterations):
        ranks = (1 - d) / N + d * link_matrix.dot(ranks)

    # Return PageRank scores for each node
    return {nodes[i]: ranks[i] for i in range(N)}


# Example Usage
if __name__ == "__main__":
    # Define a simple link structure (web graph)
    web_graph = {
        'A': ['B', 'C'],
        'B': ['C'],
        'C': ['A'],
        'D': ['C']
    }

    # Compute PageRank
    page_ranks = page_rank(web_graph, num_iterations=100, d=0.85)

    # Display the PageRank scores
    print("PageRank Scores:")
    for node, rank in page_ranks.items():
        print(f"{node}: {rank:.4f}")
