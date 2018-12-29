# Codejam 2018, Round 2: Costume Change

from collections import defaultdict

class BipartiteGraph:
    def __init__(self, graph):

        # graph: Adjacency list as a dictionary
        self.graph = graph
        # Vertices in A
        self.A = set(graph.keys())
        # Vertices in B
        self.B = set().union(*graph.values())

    def DFS(self, i, match_B, seen):
        """Returns True if vertex i can be matched."""
        for j in self.B:
            if j in self.graph[i] and not seen[j]:
                seen[j] = True

                if match_B[j] is None or self.DFS(match_B[j], match_B, seen):
                    match_B[j] = i
                    return True

        return False

    def maximum_matching(self):
        """Find maximum matching given bipartite graph."""
        match_B = dict.fromkeys(self.B)
        result = 0

        for i in self.A:
            seen = dict.fromkeys(self.B, False)

            if self.DFS(i, match_B, seen):
                result += 1

        return result


def min_changes(stage, N):
    """Returns minimum costume changes needed."""
    matching_sum = 0

    for dancers in stage.values():
        graph = BipartiteGraph(dancers)
        matching_sum += graph.maximum_matching()

    return N*N - matching_sum

# I/O Code
num_cases = int(input())

for case in range(1, num_cases + 1):
    N = int(input())

    stage = defaultdict(lambda: defaultdict(set))
    # stage = defaultdict(list)
    for i in range(N):
        for j, c in enumerate(map(int, input().split())):
            # stage[c].append((i,j))
            stage[c][i].add(j)

    changes = min_changes(stage, N)
    print('Case #{}: {}'.format(case, changes))
