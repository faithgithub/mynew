__author__ = 'wxy'
for start in xrange((10 - 2) / 2, -1, -1):
    print start
graph = {'A': ['B', 'C'],
             'B': ['C', 'D'],
             'C': ['D'],
             'D': ['C'],
             'E': ['F'],
             'F': ['C']}
def find_path(graph,start,end,path=None):
    path = [] if not  path else path
    path = path+[start]
    if start==end:
        return path
    for node in graph[start]:
        if node not in start:
            new_path = find_path(graph,node,end,path)
            if new_path:
                return new_path
    return None
#print find_path(graph,'A','D')
def find_all_paths(graph, start, end, path=None):
    path = [] if not  path else path
    path = path+[start]
    if start==end:
        return [path]
    paths = []
    for node in graph[start]:
        if node != start:
            new_paths = find_all_paths(graph,node,end,path)
            for i in new_paths:
                paths.append(i)
    print 'a',paths
    return paths
print find_all_paths(graph,'A','D')