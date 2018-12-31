# Codejam 2018, Round 3: Name-Preserving Network

import sys
from random import sample

def generate_regular_graph(N, K=4):
    """
    Generate a K-regular graph with N vertices.
    Returns an adjacency matrix. (N*K must be even)
    """
    assert (N*K) % 2 == 0 and N > K

    edges = set()
    while len(edges) < (N*K)//2:
        verts = sample([i % N for i in range(N*K)], N*K)
        edges = set((i, j) if i < j else (j, i) 
                    for i, j in zip(verts[::2], verts[1::2]) if i != j)

    graph = [[0] * N for _ in range(N)]
    for i, j in edges:
        graph[i][j] = graph[j][i] = 1

    return graph

def matrix_power(M, n):
    """Returns M**n for a symmetric square matrix M for n > 0."""
    def symmetric_matmul(A, B):
        """Matrix multiplication of NxN symmetric matrices."""
        N = len(A)
        C = [[0] * N for _ in range(N)]

        for i in range(N):
            for j in range(N):
                C[i][j] = sum([a*b for a, b in zip(A[i], B[j])])

        return C

    if n == 1:
        return M
    else:
        P = matrix_power(M, n//2)
        C = symmetric_matmul(P, P)

        if n % 2 == 0:
            return C
        else:
            return symmetric_matmul(C, M)

def signature(graph):
    """Find signature of a graph."""
    return [tuple(sorted(r)) for r in matrix_power(graph, 7)]

def create_special_graph(N):
    """Generate a graph of N vertices with a unique signature."""
    graph = generate_regular_graph(N)
    while len(set(signature(graph))) != N:
        graph = generate_regular_graph(N)
    return graph

def read_new_graph():
    """Read edge list from judge into an adjacency matrix."""
    N = int(input())
    if N < 0: sys.exit()

    graph = [[0] * N for _ in range(N)]
    for _ in range(2*N):
        i, j = tuple(map(int, input().split()))
        graph[i-1][j-1] = 1
        graph[j-1][i-1] = 1

    return graph

def find_permutation(graph_0, graph_1):
    """Compare signatures of two graphs. Send permutation to judge."""
    sig_0 = signature(graph_0)
    sig_1 = signature(graph_1)

    permutation = []
    for vertex_sig in sig_0:
        permutation.append(str(sig_1.index(vertex_sig) + 1))

    print(" ".join(permutation), flush=True)

def process_case(N):
    # Generate a 4-regular graph of N vertices
    graph = create_special_graph(N)

    # Send edges to judge
    print('{}'.format(N), flush=True)
    for i in range(N):
        for j in range(i+1, N):
            if graph[i][j]:
                print('{} {}'.format(i+1, j+1), flush=True)

    # Read edges from judge into a graph
    new_graph = read_new_graph()

    # Determine permutation and send to judge
    find_permutation(graph, new_graph)

# I/O Code
num_cases = int(input())

for case in range(1, num_cases + 1):
    N = min(map(int, input().split()))
    if N < 0: break
    process_case(N)

sys.exit()
