def bfs(graphs, start, goal):
    if goal not in graphs:
        print("wrong node entered")
        return
    explored = []
    if start in goal:
        print('root node itself is goal')
        return explored

    queue = [start]

    # keep looping until there are nodes still to be checked
    while queue:
        # pop shallowest node (first node) from queue
        node = queue.pop(0)
        if node in goal:
            print('Goal Found:', node)
            print('TRAVERSAL ORDER:')
            for v in explored:
                print("-", v, "-")
            print("-", node, "-")
            print("\n")
            # return "success"
        if node not in explored:
            # add node to list of checked nodes
            explored.append(node)
            neighbours = graphs[node]

            # add neighbours of node to queue
            for neighbour in neighbours:
                queue.append(neighbour)
    return explored


n = int(input("enter number of nodes : "))
graph = {}
for i in range(n):
    keys = input("enter the node : ")
    word = input("enter the child nodes (without any space) : ")
    graph[keys] = list(word)
starting_node = input("enter the root node : ")
goal_nodes = int(input("enter how many goal nodes you want to traverse : "))
for i in range(1, goal_nodes + 1):
    i = input("enter " + str(i) + " goal node : ")
    bfs(graph, starting_node, i)
