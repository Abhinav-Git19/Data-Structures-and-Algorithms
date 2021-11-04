
paths = []
orders = []
def dfs(g,vi,path):

    paths.append(path)
    orders.append(vi)

    for nv in g[vi]:
        if nv not in path:
            path.append(nv)
            dfs(g,nv,path)
    


graph = [[1,2],[0,2,3],[0,1,4],[1,4],[3,2,5],[4]]

dfs(graph,0,[0])

print('Paths:')
print(paths)

print('Orders:')
print(orders)

