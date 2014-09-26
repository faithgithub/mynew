__author__ = 'zxh'
graph = {'A': ['B', 'C'],
             'B': ['C', 'D'],
             'C': ['D'],
             'D': ['C'],
             'E': ['F'],
             'F': ['C']}
def find_path(graph,start,end,path=None):
    path = [] if not path else path
    path = path+[start]
    if start==end:
        return path
    if not graph.has_key(start):
        return None
    for node in graph[start]:
        if node not in path:
            new_path =  find_path(graph,node,end,path)
            if new_path:
                return new_path
    return None
#print find_path(graph,'A','D')
def find_all_paths(graph, start, end, path=None):
    path = [] if not path else path
    path = path + [start]
    if start == end:
        return [path]
    if not graph.has_key(start):
        return []
    paths = []
    for node in graph[start]:
        if node not in path:
            newpaths = find_all_paths(graph, node, end, path)
            for newpath in newpaths:
                #print paths,newpath
                paths.append(newpath)
    return paths
print find_all_paths(graph,'A','D')
def find_shortest_path(graph, start, end, path=None):
    path = [] if not path else path

    path = path + [start]
    if start == end:
        return path
    if not graph.has_key(start):
        return None
    shortest = None
    for node in graph[start]:
        if node not in path:
            newpath = find_shortest_path(graph, node, end, path)
            if newpath:
                print shortest
                if not shortest or len(newpath) < len(shortest):
                    shortest = newpath
    return shortest
#print find_shortest_path(graph,'A','D')