import heapq

# Number of vertices
V = 9

# Adjacency list (exactly as in diagram)
graph = {
    0: [(1,4), (7,8)],
    1: [(0,4), (2,8), (7,11)],
    2: [(1,8), (3,7), (8,2), (5,4)],
    3: [(2,7), (4,9), (5,14)],
    4: [(3,9), (5,10)],
    5: [(2,4), (3,14), (4,10), (6,2)],
    6: [(5,2), (7,1), (8,6)],
    7: [(0,8), (1,11), (8,7), (6,1)],
    8: [(2,2), (6,6), (7,7)]
}

def dijkstra(source):
    dist = {i: float('inf') for i in range(V)}
    dist[source] = 0
    
    pq = [(0, source)]  # (distance, node)
    
    while pq:
        current_dist, u = heapq.heappop(pq)
        
        if current_dist > dist[u]:
            continue
        
        for v, weight in graph[u]:
            if dist[v] > dist[u] + weight:
                dist[v] = dist[u] + weight
                heapq.heappush(pq, (dist[v], v))
    
    return dist


# Run Dijkstra from node 0
result = dijkstra(0)

# Display in table format
print("Shortest distances from node 0:")
print("---------------------------------")
print("Node\tDistance")

for node in sorted(result):
    print(f"{node}\t{result[node]}")

# Save to file
with open("dijkstra_output.txt", "w") as f:
    f.write("Shortest distances from node 0:\n")
    f.write("---------------------------------\n")
    f.write("Node\tDistance\n")
    for node in sorted(result):
        f.write(f"{node}\t{result[node]}\n")

print("\nOutput saved to dijkstra_output.txt")