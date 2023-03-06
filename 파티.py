import heapq

num = int(1e9) 

def root(graph, start):
    save = [num] * (len(graph) + 1)
    save[start] = 0
    
    heap = []
    heapq.heappush(heap, (0, start))
    
    while heap:
        km, now = heapq.heappop(heap)
        
        if save[now] < km:
            continue
            
        for node, weight in graph[now]:
            cost = km + weight
            
            if cost < save[node]:
                save[node] = cost
                heapq.heappush(heap, (cost, node))
                
    return save
                
def find():
    N, M, X = map(int, input().split()) 
    graph = [[] for _ in range(N + 1)]
    
    for _ in range(M):
        a, b, t = map(int, input().split())
        graph[a].append((b, t))
        
    end = 0
    for i in range(1, N + 1):
        if i == X:
            continue
            
        from_x = root(graph, X) 
        to_i = root(graph, i) 
        
        t_time = from_x[i] + to_i[X] 
        
        end = max(end, t_time)
        
    return end

print(find())
