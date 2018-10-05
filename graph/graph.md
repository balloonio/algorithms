Connected Component:
Union Find (undirected graph or weakly connected component in directed graph)
Kosaraju's Algorithm (DFS, put V into stack by finish time, reverse graph, explore SCC based on stack order)

Minimum Spanning Tree:
Kruskal's algorithm (sort edge, union find, connected component)
Prim's algorithm (keep pulling from hashheap of vertice distance)

Bipartite
BFS/DFS coloring to check if it is Bipartite
Hungarian algorithm (maximum matching)

Shortest Path
BFS (Weightless edge shortest path)
Dijkstra's Algorithm (single source, non-negative weight, simple to Prim's, keep pulling from hashheap of vertice distance)

Maximum Flow
Ford Fulkerson method Edomonds Karp algorithm (BFS + parent map + visited map)
