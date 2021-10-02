
"""
Make MST by kruskal algorithm
you can calculate minimum weight of MST by this code
"""
def find(node) -> int:
    node_ = node
    #After iteration, node variable reach to root node.
    while node != disjoin_set[node]: # iterate until node reaches to root node 
        node = disjoin_set[node]
    
    while node_ != disjoin_set[node_]: #compressing the path to end node
        p_node = disjoin_set[node_]
        disjoin_set[node_] = node # make node_ and every parents of it as a child of root
        node_ = p_node
    return node

def union(u,v) -> None:
    u_root = find(u)
    v_root = find(v)
    #union by rank 
    if tree_rank[u_root] > tree_rank[v_root]:
        disjoin_set[v_root] = u_root
        tree_rank[u_root] += tree_rank[v_root]
    else:
        disjoin_set[u_root] = v_root
        tree_rank[v_root] += tree_rank[u_root]
    return

#n is number of nodes m is number of edges
n = 6; m = 9
edges = [
    #each element in tuple means start node , end node, weight
    (1,2,5),
    (1,3,4),
    (2,3,2),
    (2,4,7),    
    (3,4,6),    
    (3,5,11),    
    (4,5,3),    
    (4,6,8),
    (5,6,8)
    ]
disjoin_set = [i for i in range(n + 1)] #set for union-find 
tree_rank = [1 for _ in range(n + 1)] #the height of each trees
res,edge_count = 0,0

#use kruskal algorithm
for u,v,w in sorted(edges, key = lambda k: k[2]):
    #if count of edges in tree exceed n-1 break iteration since we found MST
    if edge_count >= n - 1:
        break
    u_root = find(u); v_root = find(v)
    if u_root == v_root: continue #if each nodes has same root two nodes in tree
    union(u,v)
    res += w; edge_count += 1

#print the minumun weight of MST
print(res)